import argparse
import csv

import numpy as np

import rot_matrix_solve as d_basis

# Translation Basis Definitions
# All sync positions are defined row wise (x, y, z)
MAT_B1 = np.array([
    [2.22711,	-0.226531,	-0.0671484], # x = 2.22711, y = -.226531, z = -.-0671484...
    [6.45367,  -3.57227,    0.0133328],
    [3.50909,  -2.01472, -0.0777887]
]).T

MAT_R1 = np.array([
    [0.901928,   0.23471,    0.121155],
    [5.50031,   -2.74337,    0.381287],
    [2.3099,  -1.40638,   0.134852]
]).T

MAT_R2 = np.array([
    [1.38289, 0.205411,   0.186091],
    [4.36434,   -0.0080363,   0.432257],
    [6.31585,  0.684121, 0.626229]
]).T

MAT_B2 = np.array([
    [2.72829,   -0.283092,    -0.0316143],
    [5.64502,  -0.762065,    0.0183434],
    [7.31903,  -0.230759,  0.0504592]
]).T
# End Basis Definitions


X_POS = 4
Y_POS = X_POS + 1
Z_POS = X_POS + 2

NULL_MARKER = 2222

R2B_OUTPUT_FILE = 'output/road_proj_to_back.csv'

'''
    Usage:
        python3 move_road_to_back.py <road_csv_file>
'''

#
#   Defines all arguments taken in by command line
#       Road and Back are the calibration positions used
#       road_csv_path: str  |   CSV data file containing AprilTag output for the road camera
#


def define_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('road_csv_path', help="road data file", type=str)
    return parser


"""
    road_csv_row: array |   A single non-header row from the AprilTag road camera output   
        Extracts and returns the (x: float, y: float, z: float) tuple from the row of csv data
    Structure:
        frameId | detectionId | Hamming Distance | Distance | X | Y | Z | Yaw | Pitch | Roll
"""


def extract_pos_from_csv(road_csv_row):
    return (float(road_csv_row[X_POS]), float(road_csv_row[Y_POS]), float(road_csv_row[Z_POS]))


"""
    road_csv_row: array |   Single non-header row from AprilTag road camera output
        Interest specifically in (x, y, z) data contained in said row
    R: 3x3 rotation matrix (np.array)   |   Rotation matrix used to rotate road coordinate space
        into back coordinate space (it's unlikely that the cameras will be oriented the same)
    T: 3-tuple   |  Translate vector used to move between origin of road and back coordinate spaces
        
    R & T are defined in this transformation

    road coordinate space -> transformed by [R | T] -> back coordinate space

    Mathematically, R * road + [T T T T ...] = back 
        where road and back are 3xN matrices and the transform matrix consists of N columns of T
"""


def get_r2b_proj_pos(road_csv_row, R, T):
    road_pos = np.asarray(extract_pos_from_csv(road_csv_row))

    back_pos_no_translate = np.matmul(R, road_pos)

    return back_pos_no_translate + T


'''
    r2b_csv_file: file handle |     File handle on the output data file to pipe the projected road vector positions to
    r2b_vec:    3-tuple |   (back ^x, back ^y, back ^z) projection calculated by <back ^vec> = <road csv vec> + <proj vec>  
'''


def write_to_r2b_file(r2b_csv_file, frameId, detectionId, total_dist, r2b_vec, hammingDistance=-1):
    r2b_csv_file.write(str(frameId) + '\t' + str(detectionId) + '\t' + str(total_dist) +
                       '\t' + str(r2b_vec[0]) + '\t' + str(r2b_vec[1]) + '\t' + str(r2b_vec[2]) + '\n')


def magnitude(vector):
    return pow(pow(vector[0], 2) + pow(vector[1], 2) + pow(vector[2], 2), .5)


def write_header(r2b_proj_csv_file):
    r2b_proj_csv_file.write('frameId' + '\t' + 'detectionId' + '\t' +
                            'distance' + '\t' + 'projX' + '\t' 'projY' + '\t' + 'projZ' + '\n')


def main():
    # Gets the parser object after initializing the required parameters
    parser = define_arguments()
    args = parser.parse_args()  # Gets the parsed arguments

    road_csv_path = args.road_csv_path  # Extracts the path to the road_csv data file

    r2b_proj_csv_file = None
    try:
        r2b_proj_csv_file = open(R2B_OUTPUT_FILE, 'w+')
    except:
        print('Unable to open output R2B data file @ %s' % R2B_OUTPUT_FILE)

    write_header(r2b_proj_csv_file)

    (R, T, _) = d_basis.calc_basis_change(MAT_R1, MAT_B1, MAT_R2, MAT_B2)
    trans_vec = d_basis.calc_trans_vec_from_mat(T)

    print("Yielded Rotation")
    print(R)

    print("Yielded Translation")
    print(trans_vec)

    with open(road_csv_path, 'r') as road_csv:
        csv_reader = csv.reader(road_csv, delimiter='\t')
        next(csv_reader, None)  # Skips the header row of the CSV file
        for row in csv_reader:
            # Casts the frameId value in the first column to an int
            frameId = int(row[0])
            detectionId = row[1]
            if int(detectionId) == NULL_MARKER:  # Checks if the row is a frame terminator row
                write_to_r2b_file(r2b_proj_csv_file, frameId, detectionId,
                                  2222, (NULL_MARKER, NULL_MARKER, NULL_MARKER))
            else:
                r2b_proj_vec = get_r2b_proj_pos(row, R, trans_vec)
                write_to_r2b_file(r2b_proj_csv_file, frameId, detectionId, magnitude(
                    r2b_proj_vec), r2b_proj_vec)


if __name__ == '__main__':
    main()

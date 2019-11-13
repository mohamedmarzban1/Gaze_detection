from visualize_2 import Visualize_2
from scripts import standardize_visualize
from scripts import Calibration
from preprocessing import LabelingScript

APRIL_TAG_HAT = "/root/2019-11-05/output/AprilTag_Cap.csv"
APRILTAG_CALIBRATION_BACK = "/root/2019-11-05/output/AprilTag_Calib_Back.csv"
HAT_CENTER_OF_MASS = "meshsave_back_2.mat"
REFERENCE_CALIBRATION_BACK = "config/MarkersAppended2019-6-20BackStandardv2.pickle"
KABASCH_TRANSFORM_PICKLE_PATH = "config/KabaschRotTrans.pickle"

ID_FILE_PATH = "/root/2019-11-05/face_and_eyes/FE2019-11-05/id.csv"

VISUALIZE_FRAMES_OUTPUT = '/root/2019-11-05/output/visualize_frames.csv'

ANGLES_ID_OUTPUT = '/root/2019-11-05/output/AnglesId.csv'


# ##### Calibrate the back camera to obtain the transformation rotation and trasnlation mastrices
# # echo "Calculating transformation matrices w.r.t the reference saved back coordinates and outputting to $KabaschRotTrans"
# # cd scripts/
# # python3 Calibration.py "../../$AprilTag_Calib_Back"    "../../$Ref_Calib_Back" "../../$KabaschRotTrans"  &

# cd visualize_2/ #we have to enter visualize_2 directory because files are saved there
# echo "Calculating center of mass. Output to $OP_VIS"
# python3 Visualize_2.py  "../$HAT_BACK" $OP_VIS &

# echo "Standardizing visualize_2 output by writing pose_all matrix from meshsave to a csv file & adding a frame column"
# python3 scripts/standardize_visualize.py    $HAT_BACK   $OP_VIS


if __name__ == "__main__":
    # Calculates transformation between our
    print("Running calibration between our back camera's frame and reference back")
    Calibration.calibrate(APRILTAG_CALIBRATION_BACK,
                          REFERENCE_CALIBRATION_BACK, KABASCH_TRANSFORM_PICKLE_PATH)
    print("Running visualize to calculate Center of Mass for the head using head tags")
    Visualize_2.calculate_head_COM(APRIL_TAG_HAT, HAT_CENTER_OF_MASS)
    print("Running standardize visualize to append a frame marker")
    standardize_visualize.sync_back_and_visualize(
        HAT_CENTER_OF_MASS, APRIL_TAG_HAT, VISUALIZE_FRAMES_OUTPUT)
    LabelingScript.label(REFERENCE_CALIBRATION_BACK, ID_FILE_PATH,
                         VISUALIZE_FRAMES_OUTPUT, KABASCH_TRANSFORM_PICKLE_PATH, ANGLES_ID_OUTPUT)
    exit()

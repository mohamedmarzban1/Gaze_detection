from subprocess import Popen
import argparse

APRILTAG_DEMO_EXECUTABLE_PATH = '../apriltag/build/bin/apriltags_demo'

FOCUS = 1000
PIXEL_WIDTH = 1920
PIXEL_HEIGHT = 1080

CAP_SIZE = 0.032
TAG_SIZE = 0.04

CAP_OUTPUT_FILE = 'output/AprilTag_Hat.csv'
BACK_CALIB_OUTPUT_FILE = 'output/AprilTag_Back.csv'


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('calib_start_frame',
                        help='Start frame of back calibration', type=int)
    parser.add_argument('calib_end_frame',
                        help='End frame of back calibration', type=int)
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()

    calib_start_frame = args.calib_start_frame
    calib_end_frame = args.calib_end_frame

    apriltag_back = Popen([APRILTAG_DEMO_EXECUTABLE_PATH], shell=True)

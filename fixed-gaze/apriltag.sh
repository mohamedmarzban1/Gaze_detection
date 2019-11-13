#!/bin/bash
if [ $# -lt 3 ]; then
    echo "Usage: $0 <back video path> <sync frame start> <sync frame end>" >&2
    exit 1
fi

BACK_VIDEO_PATH=$1
START=$2
END=$3

APRIL_TAG=../apriltag/build/bin/apriltags_demo
OUTPUT_FOLDER="output/"

HAT_BACK="output/AprilTag_Hat.csv"
AprilTag_Calib_Back="output/AprilTag_CalibBack.csv"

# checks if output folder exists
if [ ! -d "$OUTPUT_FOLDER" ]; then
    echo "Creating output folder."
    mkdir $OUTPUT_FOLDER # creates if it doesn't exist
fi

# checks if APRIL_TAG
if [ ! -f "$APRIL_TAG" ]; then
    echo "Couldn't find AprilTag at $APRIL_TAG, building source."
    cd "../apriltag"
    make
    cd "../fixed-gaze"
else
    echo "Could AprilTag at $APRIL_TAG."
fi

echo "Back video file is:   $BACK"

#### Runs AprilTag with Back behind the scenes for cap
#$APRIL_TAG -F 1000 -W 1920 -H 1080 -S 0.032 -I $BACK_VIDEO_PATH -O "$HAT_BACK" -d -f &

#### Runs AprilTag with Back behind the scenes for calibration
#### Uses $START AND $END defined above to decide the start and end of calibration frames
$APRIL_TAG -F 1000 -W 1920 -H 1080 -S 0.04 -I $BACK_VIDEO_PATH -O "$AprilTag_Calib_Back" -b $START -e $END -d -f &

wait
echo ""

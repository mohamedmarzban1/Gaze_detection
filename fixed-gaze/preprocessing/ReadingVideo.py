"""
Created on Thu Nov  8 19:14:19 2018

@author: mfm160330, aps170830
"""
import numpy as np
import cv2
import os
import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('video', help='Path to video', type=str)
    parser.add_argument(
        'output', help='Directory to output images out to', type=str)
    parser.add_argument(
        'startMinute', help='Start minute to clip from', type=int)
    parser.add_argument(
        'startSecond', help='Start second to clip from', type=int)
    parser.add_argument('endMinute', help='End minute to clip to', type=int)
    parser.add_argument('endSecond', help='End second to clip to', type=int)

    return parser.parse_args()


##===== Intialize the start and end minute/second to be extracted from the video ===#
FirstFrameFlag = 1
MinuteStart = 0
SecStart = 0  # 41

MinuteEnd = 4
SecEnd = 55  # 24

#ReadVideoLocation = 'F:/TestDrive2Oct18/Face Camera'
# 'G:/Multi-sensors gaze Data Collection/TestDrive2018-12-03/Face/F4.MP4'
VideoName = 'G:/Multi-sensors gaze Data Collection/Drive 2019-7-23/Face/GH030193.MP4'
WriteLocation = 'G:/FixedGazeImages/Gaze points Data/G2019-7-23'
ImagesName = 'D2019-7-23'
FR = 60

# 180 #(face14Oct18: 50, face1Dec: 100   mirror:150 ) #Vertical Crop Start
vCropS = 80
vCropE = 1000  # (face14Oct18: 1000,  mirror:950) #Vertical crop end
hCropS = 500  # (face14Oct18: 500,  mirror:800)
hCropE = 1550  # (face14Oct18: 1600, mirror:1650)

if __name__ == "__main__":
    args = parse_args()
    output_images(args.video, args.output, args.startSecond,
                  args.startMinute, args.endMinute, args.endSecond, FR)
    exit()

##========Read Video =======##


def output_images(video_name, write_location, minute_start, second_start, minute_end, second_end, frame_rate):
    cap = cv2.VideoCapture(video_name)
    msStart = (minute_start * 60 + second_start) * 1000
    cap.set(cv2.CAP_PROP_POS_MSEC, msStart)

    frame_end = (minute_end * 60 + second_end) * frame_rate

    count = 0
    should_read_more_frames = True
    while(cap.isOpened() & should_read_more_frames):
        _, frame = cap.read()

        if frame is None:
            count += 1
            continue

        frameCropped = frame[vCropS:vCropE, hCropS:hCropE]

        currentFrameNumber = cap.get(
            cv2.CAP_PROP_POS_FRAMES)  # current frame number
        second_name = np.mod(second_start+np.floor(count/60), 60)
        minute_name = minute_start + np.floor(second_start/60 + count/3600)
        # SecFracName is 1/60 (1 frame) seconds
        secondFractionName = np.mod(count, 60)

        cv2.imwrite(WriteLocation+"/"+ImagesName+"-%d-%d-%d-%d.jpg" %
                    (count, minute_name, second_name, secondFractionName), frameCropped)
        should_read_more_frames = bool(frame_end - currentFrameNumber)
        count += 1

    cap.release()
    cv2.destroyAllWindows()
    print("Finished without Errors")

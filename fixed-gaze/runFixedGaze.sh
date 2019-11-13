#!/bin/bash

HAT_BACK="output/AprilTag_Hat.csv"
OP_VIS="visualize_2/meshsave_back_2.mat"
AprilTag_Calib_Back="output/AprilTag_CalibBack.csv"
Ref_Calib_Back="config/MarkersAppended2019-6-20.pickle"
KabaschRotTrans="output/KabaschRotTrans.pickle"

##### Calibrate the back camera to obtain the transformation rotation and trasnlation mastrices
# echo "Calculating transformation matrices w.r.t the reference saved back coordinates and outputting to $KabaschRotTrans"
# cd scripts/
# python3 Calibration.py "../../$AprilTag_Calib_Back"    "../../$Ref_Calib_Back" "../../$KabaschRotTrans"  &

cd visualize_2/ #we have to enter visualize_2 directory because files are saved there
echo "Calculating center of mass. Output to $OP_VIS"
python3 Visualize_2.py  "../$HAT_BACK" $OP_VIS &

wait
cd ..
echo "Standardizing visualize_2 output by writing pose_all matrix from meshsave to a csv file & adding a frame column"
python3 scripts/standardize_visualize.py    $HAT_BACK   $OP_VIS

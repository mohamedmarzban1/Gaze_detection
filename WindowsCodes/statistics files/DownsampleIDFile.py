# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 22:34:10 2019

@author: mfm160330
"""
import pandas as pd
import csv
# In this file the goal is to downsample the Continuous And the Augmented Data Only

InputIdFile = "C:/Users/mfm160330/OneDrive - The University of Texas at Dallas/ADAS data/OutputFiles/AugmentedNine.csv"
DownSampleCount = 4
DownSampledIDFile = "C:/Users/mfm160330/OneDrive - The University of Texas at Dallas/ADAS data/OutputFiles/AugmentedNineDownFour.csv"


#====== Open the Downsampled ID file =========#
csv_output = open(DownSampledIDFile, 'w+')
header = "DataSetID\tImagePath\tImageID\tElevClass\tAzimClass\tElev\tAzim\n"
csv_output.write(header)

# ========= Read the input ID file ==============#
AllLabeledImagesFile = pd.read_csv(InputIdFile, sep='\t')
AllLabeledImagesFile = AllLabeledImagesFile.T
numRowsInput = AllLabeledImagesFile.shape[1]


for indx in range(numRowsInput): 
    row = AllLabeledImagesFile[indx]
    if indx % DownSampleCount == 0:
        with open(DownSampledIDFile, 'a+') as csv_output:
            filewriter = csv.writer(csv_output, delimiter='\t', quotechar='|', quoting=csv.QUOTE_MINIMAL)            
            filewriter.writerow(row)
 


# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 00:13:06 2019
@author: mfm160330

Go over all rows in a csv file, if the ID was not found as a file in the a specific folder, it will be ignored.
If the ID was found, the row will be added to a another CSV file.
"""
import os
import pandas as pd


#===== Intialize parameters ============#
InputIdFilePath = "C:/Users/mfm160330/OneDrive - The University of Texas at Dallas/ADAS data/OutputFiles/DenseTest2019-7-10And11.csv"  #input
#ImageReadLocation = "G:/AugmnetedHSV/Face" #input

# ========= Read the input ID file ==============#
AllLabeledImagesFile = pd.read_csv(InputIdFilePath, sep='\t')
AllLabeledImagesFile = AllLabeledImagesFile.T
numRowsInput = AllLabeledImagesFile.shape[1]

MissingFiles = []
for indx in range(numRowsInput): 
    row = AllLabeledImagesFile[indx]
    ImagePath = str(row['ImagePath'])
    ImageID = str(row['ImageID'])
    #if ImagePath == 'G:/AugmnetedHSV/':
    filename = ImagePath +'/Face/'+'F'+ImageID
    FileExists = os.path.isfile(filename)
    if not FileExists:
        print(filename, '/n')
        MissingFiles.append(filename)





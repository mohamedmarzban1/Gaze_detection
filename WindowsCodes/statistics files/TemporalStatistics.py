# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 16:20:07 2019
## Angles change over time
@author: mfm160330
In this file we will read the ID file and show how the angles change over time.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

IDFilePath = "G:/ContGazeImages/FaceAndEyes/CFE2019-7-10/CFE2019-7-10FinalFormatIDFile.csv"

# Dense classificiation Parameters:
# Make sure (ElevEnd -Elevstart)/res is an integar 
ElevStart = 75 # in degrees
ElevEnd = 111 #in degrees
AzimStart = -55 # in degrees
AzimEnd = 45 # in degrees
res = 2 #Resolution of Elevation and Azimuth Angles classes in degrees
#===================================#

numElevClasses = (ElevEnd - ElevStart)/res + 2
numAzimClasses = (AzimEnd - AzimStart)/res + 2


IDs, DataSets, labels = [], [] ,[]
dfInput = pd.read_csv(IDFilePath, sep='\t')
#dfInput.index = range(dfInput.shape[0])
dfInput = dfInput.T
############# create 4 empty arrays and then update them in the for loops
#countArry  =
#AzimArray = 

Elev = np.empty([dfInput.shape[1],1])
Azim = np.empty([dfInput.shape[1],1])
ImageID = []
ImageCount = np.empty([dfInput.shape[1],1])
ElevClass = np.empty([dfInput.shape[1],1])
AzimClass = np.empty([dfInput.shape[1],1])

for j in range(dfInput.shape[1]):
    row = dfInput[j]
    ImageID.append(str(row['ImageID']))
    TmpSplit = ImageID[j].split("_c")
    ImageCount[j] = int(TmpSplit[1].split("_f")[0])
    
    Elev[j] = float(row['Elev'])*180/np.pi
    Azim[j] = float(row['Azim'])*180/np.pi


    if Elev[j] < ElevStart:
        ElevClass[j] = 0 
    elif Elev[j] > ElevEnd:
        ElevClass[j] = numElevClasses-1
    else:
        ElevClass[j] = np.ceil((Elev[j]-ElevStart)/res)    
        #print('ElevClass =',ElevClass, '\n')    
    
    
    if Azim[j] < AzimStart:
        AzimClass[j] = 0
    elif Azim[j] > AzimEnd:
        AzimClass[j] = numAzimClasses-1
    else:
        AzimClass[j] = np.ceil((Azim[j]-AzimStart)/res)        
    
plt.plot(ImageCount/60, Azim)



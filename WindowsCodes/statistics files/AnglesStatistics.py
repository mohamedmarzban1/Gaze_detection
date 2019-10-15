# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 13:45:16 2019

Data statistics
Output the max, min, average, median, standard deviation, histogram of azimuth and Elevation Angles
@author: mfm160330
"""



import os
import pandas as pd
import csv
import numpy as np 
import matplotlib.pyplot as plt


#===== Intialize parameters ============#

ReadLocation = "C:/Users/mfm160330/OneDrive - The University of Texas at Dallas/ADAS data/FaceAndEyes/FE2018-12-3" #input
#ReadLocation = "G:/ContGazeImages/FaceAndEyes/CFE2019-7-9" #input
FileName = "AnglesIDfile.csv" #input
#FileName = "CFE2019-7-9IDFileCleaned.csv" #input
ParkingOrDriving = "Parking"
date = "2018-12-3"
binwidth = 2
#========================

InputIdFilePath = ReadLocation +"/"+ FileName
ImageReadLocation = ReadLocation +"/Face" 

# ========= Read the input ID file ==============#
AllLabeledImagesFile = pd.read_csv(InputIdFilePath, sep='\t')
#AllLabeledImagesFile = AllLabeledImagesFile.T
numRowsInput = AllLabeledImagesFile.shape[0]
headers = list(AllLabeledImagesFile)
Elev = AllLabeledImagesFile['Elev']
Azim = AllLabeledImagesFile['Azim']

#AnglesDF = AllLabeledImagesFile[["Elev", "Azim"]]
ElevSummary = Elev.describe()
AzimSummary = Azim.describe()

AzimDegrees = Azim*180/np.pi
ElevDegrees = Elev*180/np.pi
#AnglesDegrees = AnglesDF*180/np.pi

#AzimAx = AnglesDegrees.hist(bins=10)

fig1 = plt.figure()
ax1 = fig1.add_subplot(111)


#ElevAx = ElevDegrees.plot.hist(bins=10)
plt.hist(ElevDegrees, bins=np.arange(min(ElevDegrees), max(ElevDegrees) + binwidth, binwidth))
plt.xlabel('Angles (in degrees)')
plt.ylabel('counts')
plt.title('Elevation Angle '+ ParkingOrDriving+'  , '+date+' data')
plt.savefig(ParkingOrDriving+"HistElevation"+date+".png")

fig2 = plt.figure()
ax2 = fig2.add_subplot(111)

plt.hist(AzimDegrees, bins=np.arange(min(AzimDegrees), max(AzimDegrees) + binwidth, binwidth))
plt.xlabel('Angles (in degrees)')
plt.ylabel('counts')
plt.title('Azimuth Angle '+ ParkingOrDriving+'  , '+date+' data')
plt.savefig(ParkingOrDriving+"HistAzimuth"+date+".png")





zz=1

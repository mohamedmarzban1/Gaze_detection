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
from mpl_toolkits.mplot3d import Axes3D


#===== Intialize parameters ============#
ReadLocation1 = "C:/Users/mfm160330/OneDrive - The University of Texas at Dallas/ADAS data/FaceAndEyes"
Sub1 = [] #["FE2018-12-3", "FE2018-12-1", "FE2019-5-22", "FE2019-5-30", "FE2019-6-11", "FE2019-6-14", "FE2019-7-11", "FE2019-7-15" , "FE2019-7-23"]
ReadLocation2 = "C:/Users/mfm160330/OneDrive - The University of Texas at Dallas/ADAS data/" #"G:/ContGazeImages/FaceAndEyes"
Sub2 = ["OutputFiles"] #["CFE2019-5-22", "CFE2019-5-30", "CFE2019-6-11", "CFE2019-6-14", "CFE2019-6-21", "CFE2019-7-11", "CFE2019-7-15", "CFE2019-7-19", "CFE2019-7-23"]
IdFileName = "AugmentedNineV3.csv" #"DenseNine.csv" #"AugmentedNineDownFour.csv"  # "AnglesIDfile.csv" #"AugmentedNine.csv" 

ParkingOrDriving = "All"
date = "NineFixedNineCont"
binwidth = 2
binWidthClasses = 1
numElevClasses = 14
numAzimClasses = 38

#========================



#==== Read and concatenate all ID files =========#
dfAngles = pd.DataFrame()
Sub1_idx = 0
for i in range(len(Sub1)+len(Sub2)):
    if i < len(Sub1):
        InputIdFilePath = ReadLocation1 + "/" + Sub1[i] + "/" + IdFileName
        Sub1_idx = Sub1_idx + 1
    else:
        InputIdFilePath = ReadLocation2 + "/" + Sub2[i-Sub1_idx] + "/" + IdFileName
    
    dfAngles = [dfAngles, pd.read_csv(InputIdFilePath, sep='\t')]
    dfAngles =  pd.concat(dfAngles)


numRowsInput = dfAngles.shape[0]
headers = list(dfAngles)
Elev = dfAngles['Elev']
Azim = dfAngles['Azim']
ElevClass = dfAngles['ElevClass']
AzimClass = dfAngles['AzimClass']

ElevSummary = Elev.describe()
AzimSummary = Azim.describe()

AzimDegrees = Azim#*180/np.pi
ElevDegrees = Elev#*180/np.pi

fig1 = plt.figure()
ax1 = fig1.add_subplot(111)

# histogram for Elevation classes
ElevBins = np.arange(-0.5,numElevClasses+0.5,binWidthClasses) #
ElevHist = np.histogram(ElevClass, bins = ElevBins) #np.histogram(ElevDegrees, bins = ElevBins)
plt.hist(ElevClass, bins= ElevBins)
plt.xlabel('class number')
plt.ylabel('counts')
plt.title('Elevation classes Histogram')
plt.savefig('Elevation classes Histogram'+".png", dpi = 96)

#histogram for Azimuth classes
AzimBins = np.arange(-0.5, numAzimClasses + 0.5,binWidthClasses)  #AzimBins = np.arange(-64,72,binwidth)
AzimHist = np.histogram(AzimClass, bins = AzimBins) #np.histogram(AzimDegrees, bins = AzimBins)
fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
plt.hist(AzimClass, bins= AzimBins)
plt.xlabel('class number')
plt.ylabel('counts')
plt.title('Azimuth classes histogram')
fig2.savefig('Azimuth classes Histogram'+".png", dpi = 96)

# histogram for Elevation Angles
ElevBinsAngles = np.arange(70,142,binwidth)
ElevHistAngles = np.histogram(ElevDegrees, bins = ElevBinsAngles)
figxx = plt.figure()
axXX = figxx.add_subplot(111)
plt.hist(ElevDegrees, bins = ElevBinsAngles)
plt.xlabel('Angles (in degrees)')
plt.ylabel('counts')
plt.title('Elevation angles histogram')
figxx.savefig('Elevation angles histogram'+".png", dpi = 96)

#histogram for Azimuth angles
AzimBinsAngles = np.arange(-64,72,binwidth)
AzimHistAngles = np.histogram(AzimDegrees, bins = AzimBinsAngles)
figx = plt.figure()
axX = figx.add_subplot(111)
plt.hist(AzimDegrees, bins=AzimBinsAngles)
plt.xlabel('Angles (in degrees)')
plt.ylabel('counts')
plt.title('Azimuth angles histogram')
figx.savefig('Azimuth angles histogram Downsampled'+".png", dpi=96)





# ====== plt a 3D histogram for actual angles====================#
fig3 = plt.figure()
ax3 = fig3.add_subplot(111, projection='3d')
hist, xedges, yedges = np.histogram2d(ElevDegrees, AzimDegrees, bins=[ElevBinsAngles,AzimBinsAngles])


# Construct arrays for the anchor positions of the 16 bars.
xpos, ypos = np.meshgrid(xedges[:-1] + 0.25, yedges[:-1] + 0.25, indexing="ij")
xpos = xpos.ravel()
ypos = ypos.ravel()
zpos = 0

# Construct arrays with the dimensions for the 16 bars.
dx = dy = 0.5 * np.ones_like(zpos)
dz = hist.ravel()

ax3.bar3d(xpos, ypos, zpos, dx, dy, dz, zsort='average')
plt.xlabel('Elevation Angle (in degrees)')
plt.ylabel('Azimuth Angle (in degrees)')
#plt.zlabel('counts')
plt.show()
plt.draw()
fig3.savefig("Joint Angles DownSampled"+".png", dpi= 96)
#================================================================#


#======= plt a 3D histogram for classes ========================#
fig4 = plt.figure()
ax4 = fig4.add_subplot(111, projection='3d')
ElevBins4 = np.arange(-0.5,numElevClasses + .5,binWidthClasses)
AzimBins4 = np.arange(-0.5,numAzimClasses + .5,binWidthClasses)
hist4, xedges4, yedges4 = np.histogram2d(ElevClass, AzimClass, bins=[ElevBins4,AzimBins4])


# Construct arrays for the anchor positions of the 16 bars.
xpos4, ypos4 = np.meshgrid(xedges4[:-1] + 0.25, yedges4[:-1] + 0.25, indexing="ij")
xpos4 = xpos4.ravel()
ypos4 = ypos4.ravel()
zpos4 = 0

# Construct arrays with the dimensions for the 16 bars.
dx4 = dy4 = 0.5 * np.ones_like(zpos4)
dz4 = hist4.ravel()

plt.xlabel('Elevation class number')
plt.ylabel('Azimuth class number')
#plt.zlabel('counts')
ax4.bar3d(xpos4, ypos4, zpos4, dx4, dy4, dz4, zsort='average')
plt.show()
plt.draw()
fig4.savefig("Joint Classes Downsampled"+".png", dpi=96)





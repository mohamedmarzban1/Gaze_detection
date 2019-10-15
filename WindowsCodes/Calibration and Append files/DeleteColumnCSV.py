# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 17:34:04 2019

@author: mfm160330
"""

"""
Created on Sun Mar 17 23:05:04 2019
Deletes a column in a csv file
@author: mfm160330
"""
import pandas as pd

idFile = 'G:/ContGazeImages/FaceAndEyes/CFE2019-5-30/AnglesIDfileHalfCleaned.csv' #'id.csv'
writePath = 'G:/ContGazeImages/FaceAndEyes/CFE2019-5-30/AnglesIDfile.csv'


f= pd.read_csv(idFile, sep='\t')
keep_col = ['DataSetID', 'ImageID',	'Rho', 'Elev', 'Azim', 'Xcom', 'Ycom', 'Zcom', 'Xtarget', 'Ytarget', 'Ztarget',	'Face_X1', 'Face_Y1', 'Face_X2', 'Face_Y2', 'LEye_X1', 'LEye_Y1', 'LEye_X2', 'LEye_Y2', 'REye_X1', 'REye_Y1',	'REye_X2', 'REye_Y2', 'labels']


new_f = f[keep_col]
new_f.to_csv(writePath, index=False, sep='\t')
import os
import sys
from osgeo import gdal, ogr, osr
import numpy as np

####################
## Script to crop and copy features in overlap area of already edited tiles to current working tile automatically

###########################

### DEFINE FUNCTIONS

## get list of neighboring AOI shapes
# def get_neighborAOI_list(self):
	# neighborWM_lst = []
	# operator needs to paste neighboring watermask(s) into script 
	# print("Please paste finalized watermask of neighbor AOI(s) below one by one. End by pressing Enter")
	# WMneighborshp = input('Path to finalized neighbor watermasks <*___G4_watermask.shp>: ')		
	# 
	# while WMneighborshp != '':
		# neighborWM_lst.append(WMneighborshp)
		# WMneighborshp = input('Path to WM Neighbor AOI(s) <*___G4_AOI_nNachbar.shp>: ')	
		# 
		# print neighbortile_lst
		# return neighbortile_lst
		
## combine neighboring AOI shapes to single shape
def merge_neighborAOI_list(self,neighborAOI_lst):
	pass
	
	
	
		
		
#########################################


		
neighborshp_lst = []
#operator needs to paste neighboring AOI into script 
print("Please paste finalized watermask of neighbor AOI(s) below one by one.")
WMneighborshp = input('Path to WM Neighbor AOI(s) <*___G4_AOI_nNachbar.shp>: ')		
		
#neighbors = get_ready_tiles_list()	


## Get path to AOI_to_edit
print("Please paste AOI to edit shapefile of current project below.")
AOI2edit = input('Path to AOI to edit shapefile <*___G4_AOI_to_edit.shp>: ')

## Get path to watermask file 
print("Please paste watermask of current project AOI(s) below.")
WM2edit = input('Path to WM to edit shapefile <*___G4_watermask.shp>: ')


## check if mulitple neighbor AOIs contained in neighborshp_lst and combine to single shp
if len(neighborshp_lst) > 1:
	
 
## set working/output dir same as input shp path


## copy old watermask as backup and save new as _watermask
 

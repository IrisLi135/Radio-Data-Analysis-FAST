#!/home/liyufeng/anaconda3/bin/python
#-*-coding:utf-8-*-
#Yufeng Li@copyright

#usage example: 
#python readfile_fromfits.py *.fits
#########################################
from astropy.io import fits
import numpy as np
from numpy import *
from pylab import *
import os
import argparse
#########################################
### get input from user##################
warnings.filterwarnings('ignore')    
np.core.arrayprint._line_width = 200
parser = argparse.ArgumentParser(description="Input")
parser.add_argument('name', type=str, help = 'The fits file name.')
args = parser.parse_args()
print(parser.parse_args())
#########################################
#######read input########################
file_name = str(args.name)
#########################################
##open file and read data
fits_read = fits.open(file_name)
fits_data = fits_read[1].data['DATA']

##Observation Date
Obs_Date = fits_read[0].header['DATE-OBS']
##Observation start frequency
Obs_Freq_start = fits_read[0].header['OBSFREQ']-fits_read[0].header['OBSBW']/2
##Observation end frequency
Obs_Freq_end = fits_read[0].header['OBSFREQ']+fits_read[0].header['OBSBW']/2
##Frequency channels
Obs_Freq_channel = fits_read[0].header['OBSNCHAN']
##Frequency bin for each channel
Freq_per_sample = fits_read[1].header['CHAN_BW']

##rows in this file
Nsubint = fits_read[1].header['NAXIS2']
##samples per row
Nsample = fits_read[1].header['NSBLK']
##Time bin for each sample
Time_per_sample = fits_read[1].header['TBIN']
##Data shape
Data_shape = shape(fits_data)
##Number of polarizations
Obs_Pol = fits_read[1].header['NPOL']

##Output
print('Observation Date:', Obs_Date)
print('Duration of this file:', Nsubint*Time_per_sample*Nsample, 'seconds,', Nsubint,'rows,', Nsample, 'samples/row', )
print('Observation Frequency band:', Obs_Freq_start, 'MHz', 'to', Obs_Freq_end, 'MHz,',    Obs_Freq_channel,'channels')
print('Polarization numbers:', Obs_Pol)
print('Data shape:', Data_shape, '(rows, samples/row, Polarization, frequency channels, ...)')
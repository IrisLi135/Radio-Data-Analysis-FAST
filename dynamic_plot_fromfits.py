#!/bin/python
#-*-coding:utf-8-*-
#Yufeng Li@copyright

"""
Generate the time frequency plot from '.fits' file.
"""

#usage example: 
#python dynamic_plot_fromfits.py 32 1 '/home' '*.fits'
#32: example of down sampling 
#1:  1st polarization channel
#########################################
from astropy.io import fits
from matplotlib import pyplot as plot
import numpy as np
from numpy import *
import os
import argparse
#########################################
### get input from user##################
warnings.filterwarnings('ignore')    
parser = argparse.ArgumentParser(description="Input")
parser.add_argument("down_sample", type=int, help="Down sampling in time domain")
parser.add_argument("Pol", type=int, help="Polarization channel")
parser.add_argument("path", type=str, help="The path of fits file.")
parser.add_argument('name', type=str, help = 'The name of fits file.')
args = parser.parse_args()
print(parser.parse_args())
#########################################
#######read input########################
time_domain_downsampling = args.down_sample
pol = args.Pol
file_path = args.path
file_name = args.name
#########################################
fits_read = fits.open(file_path+file_name)
fits_data = fits_read[1].data['DATA']

data_pol = (fits_data[:,:,pol-1,:,0].squeeze().reshape((-1,d)))[::time_domain_downsampling, :]
m, n = shape(data_pol)

#the duration of single file
file_duration = fits_read[1].header['TBIN'] * fits_read[1].header['NSBLK'] * fits_read[1].header['NAXIS2']

time_series = file_duration*(int(file_name[23:27])-1)+ linspace(0, file_duration, num = m)
time_ticks_downsampling = int(256)
time_ticks = np.round(time_series[::time_ticks_downsampling],2)

freq_series = np.round(np.linspace(1000, 1500, num = 10),2)
############################################
#############plot###########################
figure(figsize = (10, 8))
im = imshow(data_pol.T, aspect='auto',cmap=get_cmap("hot"),origin="lower" )
xlabel('Time(s)')
ylabel('Frequency(MHz)')
yticks(linspace(0, n, 10), freq_series)
xticks(linspace(0, m, len(time_ticks)), time_ticks)
colorbar()
title(file_name[19:22]+'/'+'Pol'+str(pol))
savefig('dynamic_plot/'+file_name[19:27]+'pol'+ str(pol)+'.png',dpi = 200)
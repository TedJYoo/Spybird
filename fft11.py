#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 16 01:15:05 2018

@author: T.Yoo
"""

import matplotlib.pyplot as plt
from scipy.io import wavfile as wav
import numpy as np
import glob
intensity0_1000hz = []
intensity1000_2000hz = []
intensity2000_3000hz = []
intensity3000_4000hz = []
 
def average(x):
    return(sum(x)/len(x))


def append_intensities(file):
    rate, data = wav.read("%s" % file)
    first_bin = []
    second_bin=[]
    third_bin=[]
    fourth_bin=[]
    y1 = data[:,0]
    CK4 = abs(np.fft.rfft(y1))
    for i in CK4[0:1000]:
        first_bin.append(i)
    for j in CK4[1000:2000]:
        second_bin.append(j)
    for k in CK4[2000:3000]:
        third_bin.append(k)
    for l in CK4[3000:4000]:
        fourth_bin.append(l)
    intensity0_1000hz.append(average(first_bin))
    intensity1000_2000hz.append(average(second_bin))
    intensity2000_3000hz.append(average(third_bin))
    intensity3000_4000hz.append(average(fourth_bin))

for filename in glob.glob('*.wav'):
    append_intensities(filename)

    
plt.figure(1)
plt.plot(range(len(intensity0_1000hz)),intensity0_1000hz,color="red", label = "0-1000Hz")
#plt.plot(range(len(intensity1000_2000hz)),intensity1000_2000hz)
#plt.plot(range(len(intensity2000_3000hz)),intensity2000_3000hz)
plt.plot(range(len(intensity3000_4000hz)),intensity3000_4000hz,"blue", label = "3000-4000Hz")
plt.title("Relative Intensity of Frequencies vs Time on May 11, at 2:47pm")
plt.xlabel("Minutes after 1447 (Military Time)")
plt.ylabel("Relative Intensity")
plt.figure(2)
plt.plot(range(len(intensity0_1000hz)),intensity0_1000hz,color="red")
#plt.plot(range(len(intensity1000_2000hz)),intensity1000_2000hz)
#plt.plot(range(len(intensity2000_3000hz)),intensity2000_3000hz)
plt.plot(range(len(intensity3000_4000hz)),intensity3000_4000hz,"blue")
plt.title("Relative Intensity of Frequencies vs Time on May 11, at 2:47pm")
plt.xlabel("Minutes after 1447 (Military Time)")
plt.ylabel("Relative Intensity")
plt.xlim(0,10)
plt.show()
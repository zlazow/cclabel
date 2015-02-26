import Image, ImageDraw
from skimage.filter import threshold_otsu, threshold_adaptive
from skimage.util import img_as_ubyte
import numpy as np
from numpy import array
import sys
import math, random
from itertools import product
from ufarray import *
from matplotlib import pyplot as plt
import copy
from fractions import gcd
import numpy.ma as ma

# Open the image
filename=raw_input("Filename: ")
img = Image.open(filename)
arr = array(img)
#need to mask out background and water
#arr = ma.masked_equal(fresh_array,255)

height,width = arr.shape

#blockx = width/100 
#blocky = height/100
#xcount = 0
#ycount = 0

#1) create blocks
blocks=height*width/1000
xblock=width/blocks
yblock=height/blocks

for y in range(blocks):
    for x in range(blocks):
        if x == blocks-1:
            slic = arr[x*xblock:, y*yblock:y*yblock+yblock]
        elif y == blocks-1:
            slic = arr[x*xblock:x*xblock+xblock, y*yblock:]
        elif(x==(xblock-1) and (y == yblock-1)):
            slic = arr[x*xblock:, y*yblock:]
        else:
            slic = arr[x*xblock:x*xblock+xblock, y*yblock:y*yblock+yblock]
            
        #2) create histogram-like thing and find 75th-percentile
        val = np.percentile(slic,80)
        
            
        #3) Binarize the image
        w,h = slic.shape
        for r in range(h):
            for c in range(w):
                if slic[c,r]<=val:
                    arr[c+(x*xblock),r+(y*yblock)]=255
                else:
                    arr[c+(x*xblock),r+(y*yblock)]=0
        
            




        
img1 = Image.fromarray(arr)

img1.show()
filename = "BWAP_"+filename
img1.save(filename)


from PIL import Image
import numpy as np
from numpy import array
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt


filename = raw_input("Filename: ")
img = Image.open(filename)
arr = array(img)


# the histogram of the data
n, bins, patches = plt.hist(arr, 50, normed=1, facecolor='green', alpha=0.75)

plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.title("NDVI")
plt.axis([80, 160, 0, .06])
plt.grid(True)

plt.show()
#count = 0.0
#size = arr.shape[0] * arr.shape[1]
#for y in range(arr.shape[1]):
#    for x in range(arr.shape[0]):
#        if np.all(arr[x,y]):
#            count +=1
#
#print count/size
#print count
#print size 



#filename2 = raw_input("Filename2: ")
#img2 = Image.open(filename2)
#arr2 = array(img2)

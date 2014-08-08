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
plt.axis([10, 255, 0, .4])
plt.grid(True)

plt.show()



#filename2 = raw_input("Filename2: ")
#img2 = Image.open(filename2)
#arr2 = array(img2)

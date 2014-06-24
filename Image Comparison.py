from PIL import Image
import numpy as np
from numpy import array

filename = raw_input("Filename: ")
img = Image.open(filename)
arr = array(img)

filename2 = raw_input("Filename2: ")
img2 = Image.open(filename2)
arr2 = array(img2)

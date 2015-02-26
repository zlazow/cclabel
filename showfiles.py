import gdal
from gdalconst import *
import os.path
import Image
import numpy as np

script_dir = os.path.dirname(os.path.abspath(__file__))
dataset = gdal.Open(os.path.join(script_dir, 'near_barge_QB_2007.tif'))

#print 'Driver: ', dataset.GetDriver().ShortName,'/', \
#    dataset.GetDriver().LongName
#print 'Size is ',dataset.RasterXSize,'x',dataset.RasterYSize, \
#    'x',dataset.RasterCount
#print 'Projection is ',dataset.GetProjection()
band = dataset.GetRasterBand(4)
print 'Band Type=',gdal.GetDataTypeName(band.DataType)

min = band.GetMinimum()
max = band.GetMaximum()
if min is None or max is None:
    (min,max) = band.ComputeRasterMinMax(1)
print 'Min=%.3f, Max=%.3f' % (min,max)
print '\n'

narray = band.ReadAsArray()
print narray.shape[0], narray.shape[1]
#scanline = band.ReadRaster( 0, 0, band.XSize, 1,band.XSize, 1, band.DataType)
#value = struct.unpack('f' * band.XSize, scanline)

#
#for x in xrange(1, dataset.RasterCount + 1):
#    band = dataset.GetRasterBand(x)
#    array = band.ReadAsArray()
##img=Image.fromarray(array)
##img.show()
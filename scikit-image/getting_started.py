# Name: Esuabom David Dijemeni
# Date: 20/04/2015
# Purpose: Get started with scikit-image

import skimage
#from skimage import data

#camera = data.camera()
#type(camera)
#print type(camera)
#print camera.shape


#coins = data.coins()
#from skimage import filters
#threshold_value = filters.threshold_otsu(coins)
#print threshold_value

import os
filename = os.path.join(skimage.data_dir, 'moon.png')
from skimage import io
moon = io.imread(filename)
print moon

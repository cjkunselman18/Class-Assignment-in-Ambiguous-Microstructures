# -*- coding: utf-8 -*-

from skimage import io
from skimage.filters import threshold_otsu
from skimage.color import rgb2gray
import matplotlib.pyplot as plt
from scipy import ndimage



binary_image_list_precipitate = []

# Create a list of binary microstructures
for i in range(1,145):
    filename = '...Precipitate\\P_%s.jpg' % (i)
    im = io.imread(filename)
    gray = rgb2gray(im)
    thresh = threshold_otsu(gray)
    binary_image_list_precipitate.append(gray > thresh)

binary_image_list_bicontinuous = []
for i in range(1,49):
    filename = '...Bicontinuous\\B_%s.jpg' % (i)
    im = io.imread(filename)
    gray = rgb2gray(im)
    thresh = threshold_otsu(gray)
    binary_image_list_bicontinuous.append(gray > thresh)

binary_image_list_unknown = []
for i in range(1,53):
    filename = '...Unknown\\U_%s.jpg' % (i)
    im = io.imread(filename)
    gray = rgb2gray(im)
    thresh = threshold_otsu(gray)
    binary_image_list_unknown.append(gray > thresh)

# Uncomment the line below to view one of the binarized images
# plt.imshow(binary_image_list_precipitate[0])

# P_22, P_92, P_102, and P_129, need some noise removed
remove_noise_22 = ndimage.binary_opening(binary_image_list_precipitate[21])
remove_noise_92 = ndimage.binary_opening(binary_image_list_precipitate[91])
remove_noise_102 = ndimage.binary_opening(binary_image_list_precipitate[101])
remove_noise_129 = ndimage.binary_opening(binary_image_list_precipitate[128])

# Replace noisy microstructures
binary_image_list_precipitate[21] = remove_noise_22
binary_image_list_precipitate[91] = remove_noise_92
binary_image_list_precipitate[101] = remove_noise_102
binary_image_list_precipitate[128] = remove_noise_129

# -*- coding: utf-8 -*-

import warnings
warnings.filterwarnings('ignore')
from pymks import PrimitiveBasis
from pymks.stats import autocorrelate
from pymks.tools import draw_autocorrelations


# Create list of autocorrelations corresponding to the binary image lists
two_point_correlations_precipitate = []

# Two states (black and white); using primitive basis for microstructure function
p_basis = PrimitiveBasis(n_states=2, domain=[0, 1]) 

for i in range(0,144):
    two_point_correlations_precipitate.append(autocorrelate(binary_image_list_precipitate[i].reshape((1,512,512)), p_basis, periodic_axes = (0,1), autocorrelations = [(0,0)]))
    # assuming both axes are periodic and only calculating the black autocorrelations
      
two_point_correlations_bicontinuous = []
for i in range(0,48):
    two_point_correlations_bicontinuous.append(autocorrelate(binary_image_list_bicontinuous[i].reshape((1,512,512)), p_basis, periodic_axes = (0,1), autocorrelations = [(0,0)]))


two_point_correlations_unknown = []
for i in range(0,52):
    two_point_correlations_unknown.append(autocorrelate(binary_image_list_unknown[i].reshape((1,512,512)), p_basis, periodic_axes = (0,1), autocorrelations = [(0,0)]))

# Uncomment the line below to draw an autocorrelation. Only change the first index to move down the list
# draw_autocorrelations(two_point_correlations_precipitate[0][0],autocorrelations=[(0,0)])


# Now we are going to calculate black phase volume fraction and normalize the two-point correlations
vol_frac_precipitate = []
vol_frac_bicontinuous = []
vol_frac_unknown = []

for i in range(0,144):
    vol_frac_precipitate.append(1-sum(sum(binary_image_list_precipitate[i]))/262144)
    two_point_correlations_precipitate[i] = (two_point_correlations_precipitate[i] - vol_frac_precipitate[i]**2)/(vol_frac_precipitate[i] - vol_frac_precipitate[i]**2)
    
for i in range(0,48):
    vol_frac_bicontinuous.append(1-sum(sum(binary_image_list_bicontinuous[i]))/262144)
    two_point_correlations_bicontinuous[i] = (two_point_correlations_bicontinuous[i] - vol_frac_bicontinuous[i]**2)/(vol_frac_bicontinuous[i] - vol_frac_bicontinuous[i]**2)
    
for i in range(0,52):
    vol_frac_unknown.append(1-sum(sum(binary_image_list_unknown[i]))/262144)
    two_point_correlations_unknown[i] = (two_point_correlations_unknown[i] - vol_frac_unknown[i]**2)/(vol_frac_unknown[i] - vol_frac_unknown[i]**2)


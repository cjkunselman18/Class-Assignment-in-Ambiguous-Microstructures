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


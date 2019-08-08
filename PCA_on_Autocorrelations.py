# -*- coding: utf-8 -*-

from sklearn.decomposition import PCA
import numpy as np


# The IPCA function is going to require a matrix with samples as rows and features as columns. The next few steps create 
# this matrix from the training set.
train_reshape = np.ones((153,512,512))
labeled_train = np.array(labeled_train)
for i in range(0,153):
    train_reshape[i,:,:] = labeled_train[i,0,:,:,0]

pca_matrix = np.ones((153,262144))

for i in range(0,153):
    pca_matrix[i,:] = train_reshape[i,:,:].flatten()
    
# This runs IPCA
pca = PCA(3)
pca.fit(pca_matrix)

# Project training set into PCA space   
projected_train = pca.transform(pca_matrix)

# Now, do the same thing for the test set and the initially unlabeled samples
test_reshape = np.ones((39,512,512))
labeled_test = np.array(labeled_test)
for i in range(0,39):
    test_reshape[i,:,:] = labeled_test[i,0,:,:,0]

test_matrix = np.ones((39,262144))

for i in range(0,39):
    test_matrix[i,:] = test_reshape[i,:,:].flatten()

projected_test = pca.transform(test_matrix)


unknown_reshape = np.ones((52,512,512))
two_point_correlations_unknown = np.array(two_point_correlations_unknown)
for i in range(0,52):
    unknown_reshape[i,:,:] = two_point_correlations_unknown[i,0,:,:,0]

unknown_matrix = np.ones((52,262144))

for i in range(0,52):
    unknown_matrix[i,:] = unknown_reshape[i,:,:].flatten()
    

projected_unknown = pca.transform(unknown_matrix)


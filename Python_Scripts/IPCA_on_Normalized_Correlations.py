# -*- coding: utf-8 -*-

from sklearn.decomposition import IncrementalPCA
import numpy as np


# The IPCA function is going to require a matrix with samples as rows and features as columns. The next few steps create 
# this matrix from the labeled training and initially unlabeled sets.

train_reshape = np.ones((153,512,512))
labeled_train = np.array(labeled_train)

for i in range(0,153):
    train_reshape[i,:,:] = labeled_train[i,0,:,:,0]

    
unknown_reshape = np.ones((52,512,512))
two_point_correlations_unknown = np.array(two_point_correlations_unknown)

for i in range(0,52):
    unknown_reshape[i,:,:] = two_point_correlations_unknown[i,0,:,:,0]


unknown_matrix = np.ones((52,262144))


for i in range(0,52):
    unknown_matrix[i,:] = unknown_reshape[i,:,:].flatten()


pca_matrix = np.ones((153+52,262144))


for i in range(0,153):
    pca_matrix[i,:] = train_reshape[i,:,:].flatten()

    
pca_matrix[153:(153+52),:] = unknown_matrix



# This runs IPCA and fits it to the training/unlabeled sets. It really is not necessary to do a batch size of 20 (you could run
# all of the data in one batch), but this is just a demonstration of how you can run PCA incrementally
ipca = IncrementalPCA(50, batch_size=20)
ipca.fit(pca_matrix)



# Here we see how much variance is explained by the 50 PCs
explained_variance = sum(ipca.explained_variance_ratio_)



# Here we project the training and unlabeled sets into the new PCA space
projected_train = ipca.transform(pca_matrix[0:153,:])
projected_unknown = ipca.transform(pca_matrix[153:205,:])



# Now, do the same thing for the test set
test_reshape = np.ones((39,512,512))
labeled_test = np.array(labeled_test)

for i in range(0,39):
    test_reshape[i,:,:] = labeled_test[i,0,:,:,0]

test_matrix = np.ones((39,262144))

for i in range(0,39):
    test_matrix[i,:] = test_reshape[i,:,:].flatten()

projected_test = ipca.transform(test_matrix)


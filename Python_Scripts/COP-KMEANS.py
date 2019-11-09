# -*- coding: utf-8 -*-

from copkmeans.cop_kmeans import cop_kmeans
import random

must_link = []

precip_sample = np.where(np.array(label_list_train)== 1)[0][0]
bicontin_sample = np.where(np.array(label_list_train)== -1)[0][0]

# The first sample in the training set has label "1", and we want it to be linked
# to every other sample in the training set with the same label
for i in range(precip_sample + 1,153):
    if label_list_train[i] == 1:
        must_link.append((precip_sample,i))

# This is the same idea       
for i in range(bicontin_sample + 1,153):
    if label_list_train[i] == -1:
        must_link.append((bicontin_sample,i))
        
# We do not want anything with different labels to be linked
cannot_link = [(precip_sample,bicontin_sample)]

random.seed(18)
# This command runs the method; clusters are the label assignments
clusters, centers = cop_kmeans(dataset=processed_no_test, k=2, ml=must_link,cl=cannot_link)

# remember this is an unsupervised process with no real label information going into it;
# the algorithm will give two clusters, but we have to look into it to see which cluster
# labels correspond to our initial labels
precip_cluster_label = clusters[precip_sample]
bicontin_cluster_label = clusters[bicontin_sample]

for i in range(0,205):
    if clusters[i] == precip_cluster_label:
        clusters[i] = 1
    else:
        clusters[i] = -1
        



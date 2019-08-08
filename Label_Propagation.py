# -*- coding: utf-8 -*-

from math import sqrt
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import minimum_spanning_tree
from sklearn.semi_supervised import LabelPropagation

# Currently our labeled data is not in any order -- grouping the samples by label will help later
labels_p = []
labels_b = []
for i in range(0,153):
    if label_list_train[i] == 1:
        labels_p.append(i)
        
for i in range(0,153):
    if label_list_train[i] == -1:
        labels_b.append(i)

# we are creating a graph where every data point is a node and every data point is connected to every other data point by an edge
# equal to the weight of the distance between them
node_matrix = np.ones((153,3))
node_matrix[0:len(labels_p),:] = processed_train[labels_p,:]
node_matrix[len(labels_p):153,:] = processed_train[labels_b,:]

adjacency_matrix = np.ones((153,153))

for i in range(0,153):
    for j in range(0,153):
        adjacency_matrix[i,j] = sqrt((node_matrix[i,0] - node_matrix[j,0])**2 + (node_matrix[i,1] - node_matrix[j,1])**2 + (node_matrix[i,2] - node_matrix[j,2])**2)
    
# now we apply Kruskal's algorithm
adjacency_matrix = csr_matrix(adjacency_matrix)
adjacency_matrix.toarray().astype(float)
min_tree = minimum_spanning_tree(adjacency_matrix)
min_tree = min_tree.toarray().astype(float)

# this is where the ordering above comes in; due to the nature of Kruskal's algorithm, no larger edge can be added after a smaller edge, so we know that
# we are looking for the smallest edge between samples with different labels
min_tree_cut1 = min_tree[0:len(labels_p),len(labels_p):153]
min_tree_cut2 = min_tree[len(labels_p):153,0:len(labels_p)]
cross_class_edges1 = np.nonzero(min_tree_cut1)
cross_class_edges2 = np.nonzero(min_tree_cut2)

edge_magnitude_list = []
if len(cross_class_edges1[0]) != 0:
    for i in range(0,len(cross_class_edges1[0])):
        edge_magnitude_list.append(min_tree_cut1[cross_class_edges1[0][i],cross_class_edges1[1][i]])

if len(cross_class_edges2[0]) != 0:
    for i in range(0,len(cross_class_edges2[0])):
        edge_magnitude_list.append(min_tree_cut2[cross_class_edges2[0][i],cross_class_edges2[1][i]])

# sigma is this distance divided by 3; we convert to gamma because that is the parameter that the algorithm takes
sigma = np.amin(np.array(edge_magnitude_list))/3
gamma = 1/sigma/sigma


# Now to apply label propagation

# This method is built for the unlabeled samples to have label "-1," so we need to change the bicontinuous to label "0" and the 
# initially unlabeled to "-1"
label_prop_labels = []
for i in range(0,153):
    if label_list_train[i] == 1:
        label_prop_labels.append(1)
    else:
        label_prop_labels.append(0)
        
for i in range(153,205):
    label_prop_labels.append(-1)
    
# run method with gamma determined above 
label_prop = LabelPropagation('rbf', gamma=gamma,max_iter=10000)
label_prop.fit(processed_no_test,label_prop_labels)
label_propagation_out = label_prop.transduction_
label_propagation_unknown_labels = label_propagation_out[153:205]

# Now we change labels back to be consistent
for i in range(0,52):
    if label_propagation_unknown_labels[i] == 0:
        label_propagation_unknown_labels[i] = -1


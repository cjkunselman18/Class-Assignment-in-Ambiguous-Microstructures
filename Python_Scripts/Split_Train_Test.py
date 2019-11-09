# -*- coding: utf-8 -*-

from sklearn.model_selection import train_test_split

# Precipitate is "1" and Bicontinuous is "-1"
label_list = []
for i in range(0,144):
    label_list.append(1)
    
for i in range(0,48):
    label_list.append(-1)
    
# This is to keep track of which data point corresponds to which image
image_number_list = []
for i in range(0,144):
    image_number_list.append(i+1)
    
for i in range(0,48):
    image_number_list.append(i+1)
    
# We combine all labeled correlations here
labeled_correlations = two_point_correlations_precipitate[0:144]
labeled_correlations[144:192] = two_point_correlations_bicontinuous
    
# This splits the correlations into training (80%) and test (20%) sets
# Setting "random_state" allows for reproducibility - if you change it, you can get a different split
labeled_train, labeled_test, label_list_train, label_list_test, image_number_train, image_number_test = train_test_split(labeled_correlations,label_list,image_number_list,test_size=39,random_state=2018)


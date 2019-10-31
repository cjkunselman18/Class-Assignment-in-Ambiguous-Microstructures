# -*- coding: utf-8 -*-

from sklearn.semi_supervised import LabelPropagation
warnings.filterwarnings("always")
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
    
# similar to the situation in the paper, gamma values around 1 converge to reasonable solutions while larger values 
# (such as gamma=10) cause numerical issues (indicated by the warning that is thrown) and smaller values (such as gamma = 0.1) 
# cause all labels to be "1"
label_prop = LabelPropagation('rbf', gamma=1,max_iter=100000)
label_prop.fit(processed_no_test,label_prop_labels)
label_propagation_out = label_prop.transduction_
label_propagation_unknown_labels = label_propagation_out[153:205]

# Now we change labels back to be consistent
for i in range(0,52):
    if label_propagation_unknown_labels[i] == 0:
        label_propagation_unknown_labels[i] = -1

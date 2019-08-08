# -*- coding: utf-8 -*-

# find initial labels for first iteration
unknown_labels = baseline_svm.predict(processed_unknown)

# update the training label list
label_list_retrain = label_list_train + list(unknown_labels)

# and append the training set
processed_no_test = np.ones((2055,3))
processed_no_test[0:1536,:] = processed_train
processed_no_test[1536:2055,:] = processed_unknown

# create a new classification object with the same kernel/hyperparameters, and retrain
svm_retrain = clf.best_estimator_
svm_retrain.fit(processed_no_test, label_list_retrain)

# make a new prediction on the initially unlabeled samples
unknown_labels_again = svm_retrain.predict(processed_unknown)

# if there is no change, this value should be 0 and we are done
convergence_check = np.amax(abs(unknown_labels - unknown_labels_again))==0
iterations = 1

# if not done, this loop will run until convergence is reached
while convergence_check == False and iterations < 101 :
    unknown_labels = unknown_labels_again[:]
    label_list_retrain = label_list_train + list(unknown_labels)
    svm_retrain = clf.best_estimator_
    svm_retrain.fit(processed_no_test, label_list_retrain)
    unknown_labels_again = svm_retrain.predict(processed_unknown)
    convergence_check = np.amax(abs(unknown_labels - unknown_labels_again))==0
    iterations = iterations + 1
    
self_train_labels = unknown_labels_again[:]
print(iterations)


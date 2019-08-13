# -*- coding: utf-8 -*-

# Check the first criterion

label_prop_labels_test = label_prop_labels[0:192]

    
# run method with gamma determined above 
label_prop_test = LabelPropagation('rbf', gamma=gamma,max_iter=10000)
label_prop_test.fit(processed[0:192,:],label_prop_labels_test)
label_propagation_out_test = label_prop_test.transduction_
label_propagation_test_labels = label_propagation_out_test[153:192]

# Now we change labels back to be consistent
for i in range(0,39):
    if label_propagation_test_labels[i] == 0:
        label_propagation_test_labels[i] = -1
        
# and we check to see if they are the same
criterion_check = np.amax(abs(np.array(label_list_test) - label_propagation_test_labels)==0)
print(criterion_check)

# Check the second criterion
label_list_prop = label_list_train + list(label_propagation_unknown_labels)

# tune kernel/hyper-parameters
print("# Tuning hyper-parameters for accuracy")
print()

clf = GridSearchCV(SVC(probability = True), tuned_parameters, cv=5,
                       scoring='accuracy' )
clf.fit(processed_no_test, label_list_prop)

print("Best parameters set found on development set:")
print()
print(clf.best_params_)
print()
print("Grid scores on development set:")
print()
means = clf.cv_results_['mean_test_score']
stds = clf.cv_results_['std_test_score']
for mean, std, params in zip(means, stds, clf.cv_results_['params']):
    print("%0.3f (+/-%0.03f) for %r"
            % (mean, std * 2, params))

# Test accuracy
prop_svm = clf.best_estimator_
predicted_test_labels_prop = prop_svm.predict(processed_test)
mat = confusion_matrix(label_list_test, predicted_test_labels_prop)
plt.figure(0)
sns.heatmap(mat.T, square=True, annot=True, fmt='d', cbar=False,xticklabels=[-1,1],yticklabels=[-1,1])
plt.xlabel('True Label')
plt.ylabel('Predicted Label')

# Training accuracy
predicted_train_labels_prop = prop_svm.predict(processed_train)
mat = confusion_matrix(label_list_train, predicted_train_labels_prop)
plt.figure(1)
sns.heatmap(mat.T, square=True, annot=True, fmt='d', cbar=False,xticklabels=[-1,1],yticklabels=[-1,1])
plt.xlabel('True Label')
plt.ylabel('Predicted Label')

# For the provided problem, this criterion is not passed because the training accuracy is less than 100%.
# The gamma value found from the heuristic above is an order of magnitude smaller than that of the entire dataset
# considered in the paper; thus, raising the gamma value for this problem may allow this criterion to be passed for
# this smaller dataset





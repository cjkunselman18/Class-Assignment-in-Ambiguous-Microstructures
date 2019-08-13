# -*- coding: utf-8 -*-

# Only the Modified Yarowsky and the S4VM methods passed the criteria, so 
# only their votes will count for the updated training set. However, feel free 
# add the votes of other methods for your subset 

unknowns_add_to_training = []
unknown_labels_for_training = []

# add extra methods here with "and list_name == -1/1"
for i in range(0,52):
    if self_train_labels[i] == -1 and s4vm_labels == -1:
        unknowns_add_to_training.append(i)
        unknown_labels_for_training.append(-1)
    elif self_train_labels[i] == 1 and s4vm_labels == 1:
        unknowns_add_to_training.append(i)
        unknown_labels_for_training.append(1)

# Number of samples in the subset
print(len(unknowns_add_to_training))

# Now, to train an SVM with the updated training set
updated_label_list_train = label_list_train + unknown_labels_for_training
processed_updated_train = np.ones((153+len(unknowns_add_to_training),3))
processed_updated_train[0:153,:] = processed_train
processed_updated_train[153:(153+len(unknowns_add_to_training)),:] = processed_unknown[unknowns_add_to_training,:]

# tune kernel/hyper-parameters
print("# Tuning hyper-parameters for accuracy")
print()

clf = GridSearchCV(SVC(probability = True), tuned_parameters, cv=5,
                       scoring='accuracy' )
clf.fit(processed_updated_train, updated_label_list_train)

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
updated_svm = clf.best_estimator_
predicted_test_labels_updated = updated_svm.predict(processed_test)
mat = confusion_matrix(label_list_test, predicted_test_labels_updated)
plt.figure(0)
sns.heatmap(mat.T, square=True, annot=True, fmt='d', cbar=False,xticklabels=[-1,1],yticklabels=[-1,1])
plt.xlabel('True Label')
plt.ylabel('Predicted Label')

# Training accuracy
predicted_train_labels_updated = updated_svm.predict(processed_train)
mat = confusion_matrix(label_list_train, predicted_train_labels_updated)
plt.figure(1)
sns.heatmap(mat.T, square=True, annot=True, fmt='d', cbar=False,xticklabels=[-1,1],yticklabels=[-1,1])
plt.xlabel('True Label')
plt.ylabel('Predicted Label')



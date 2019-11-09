# First we determine where all four semi-supervised methods agree
sum_list = []

for i in range(0,52):
    sum_list.append(label_propagation_unknown_labels[i]+self_train_labels[i]+clusters[i+153]+s4vm_labels[i])
    

unknowns_add_to_training = []
unknown_labels_for_training = []
for i in range(0,52):
    if sum_list[i] == 4 or sum_list[i] == -4:
        unknowns_add_to_training.append(i)
    if sum_list[i] == 4:
        unknown_labels_for_training.append(1)
    if sum_list[i] == -4:
        unknown_labels_for_training.append(-1)
    
# then we add this subset with correpsonding labels to the training set        
training_with_unknowns = np.ones((153+len(unknowns_add_to_training),50))
training_with_unknowns[0:153,:] = processed_train
training_with_unknowns[153:(153+len(unknowns_add_to_training)),:] = processed_unknown[unknowns_add_to_training,:]

# Now we optimize hyperparameters and train the updated SVM as we did the baseline SVM
training_with_unknowns_labels = label_list_train + unknown_labels_for_training

print("# Tuning hyper-parameters for accuracy")
print()

clf = GridSearchCV(SVC(probability = True), tuned_parameters, cv=cv,
                       scoring='accuracy' )
clf.fit(training_with_unknowns, training_with_unknowns_labels)

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

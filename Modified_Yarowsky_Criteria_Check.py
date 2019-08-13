# -*- coding: utf-8 -*-

# Check the first criterion

# We already know that the baseline classifier labels the test set correctly, 
# so we can skip the inital label assignment

label_list_train_and_test = label_list_train = label_list_test

svm_test_retrain = clf3.best_estimator_
svm_test_retrain.fit(processed[0:192,:])

MY_test_labels = svm_test_retrain.predict(processed_test)

convergence_check = np.amax(abs(np.array(label_list_test) - MY_test_labels)) == 0

iterations = 1

# if not done, this loop will run until convergence is reached
while convergence_check == False and iterations < 101 :
    test_labels = MY_test_labels[:]
    test_list_retrain = label_list_train + list(test_labels)
    svm_retrain = clf3.best_estimator_
    svm_retrain.fit(processed[0:192,:], test_list_retrain)
    MY_test_labels = svm_retrain.predict(processed_test)
    convergence_check = np.amax(abs(test_labels - MY_test_labels))==0
    iterations = iterations + 1
    

criterion_check = np.amax(abs(np.array(label_list_test) - MY_test_labels)) == 0
print(criterion_check)

# Check the second criterion
label_list_MY = label_list_train + self_train_labels

# tune kernel/hyper-parameters
print("# Tuning hyper-parameters for accuracy")
print()

clf = GridSearchCV(SVC(probability = True), tuned_parameters, cv=5,
                       scoring='accuracy' )
clf.fit(processed_no_test, label_list_MY)

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
MY_svm = clf.best_estimator_
predicted_test_labels_MY = MY_svm.predict(processed_test)
mat = confusion_matrix(label_list_test, predicted_test_labels_MY)
plt.figure(0)
sns.heatmap(mat.T, square=True, annot=True, fmt='d', cbar=False,xticklabels=[-1,1],yticklabels=[-1,1])
plt.xlabel('True Label')
plt.ylabel('Predicted Label')

# Training accuracy
predicted_train_labels_MY = MY_svm.predict(processed_train)
mat = confusion_matrix(label_list_train, predicted_train_labels_MY)
plt.figure(1)
sns.heatmap(mat.T, square=True, annot=True, fmt='d', cbar=False,xticklabels=[-1,1],yticklabels=[-1,1])
plt.xlabel('True Label')
plt.ylabel('Predicted Label')


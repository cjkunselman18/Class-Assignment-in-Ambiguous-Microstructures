# Optimize hyperparameters for SVM trained over output of Modified Yarowsky
print("# Tuning hyper-parameters for accuracy")
print()

clf = GridSearchCV(SVC(probability = True,max_iter=10000), tuned_parameters, cv=cv,
                       scoring='accuracy' )
clf.fit(processed_no_test, label_list_train + list(self_train_labels))

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

# Train SVM and determine test accuracy
st_svm = clf.best_estimator_
predicted_test_labels_st = st_svm.predict(processed_test)
mat = confusion_matrix(label_list_test, predicted_test_labels_st)
plt.figure(0)
sns.heatmap(mat.T, square=True, annot=True, fmt='d', cbar=False,xticklabels=[-1,1],yticklabels=[-1,1])
plt.xlabel('True Label')
plt.ylabel('Predicted Label')
plt.title('Modified Yarowsky')

# Repeat for Label Propagation
print("# Tuning hyper-parameters for accuracy")
print()

clf = GridSearchCV(SVC(probability = True,max_iter=10000), tuned_parameters, cv=cv,
                       scoring='accuracy' )
clf.fit(processed_no_test, label_list_train + list(label_propagation_unknown_labels))

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


lp_svm = clf.best_estimator_
predicted_test_labels_lp = lp_svm.predict(processed_test)
mat = confusion_matrix(label_list_test, predicted_test_labels_lp)
plt.figure(1)
sns.heatmap(mat.T, square=True, annot=True, fmt='d', cbar=False,xticklabels=[-1,1],yticklabels=[-1,1])
plt.xlabel('True Label')
plt.ylabel('Predicted Label')
plt.title('Label Propagation')

# Repeat for COP-KMEANS
print("# Tuning hyper-parameters for accuracy")
print()

clf = GridSearchCV(SVC(probability = True,max_iter=10000), tuned_parameters, cv=cv,
                       scoring='accuracy' )
clf.fit(processed_no_test, label_list_train + list(clusters[1536:2055]))

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


ckm_svm = clf.best_estimator_
predicted_test_labels_ckm = ckm_svm.predict(processed_test)
mat = confusion_matrix(label_list_test, predicted_test_labels_ckm)
plt.figure(2)
sns.heatmap(mat.T, square=True, annot=True, fmt='d', cbar=False,xticklabels=[-1,1],yticklabels=[-1,1])
plt.xlabel('True Label')
plt.ylabel('Predicted Label')
plt.title('COP-KMEANS')

# Repeat for S4VM
print("# Tuning hyper-parameters for accuracy")
print()

clf = GridSearchCV(SVC(probability = True,max_iter=10000), tuned_parameters, cv=cv,
                       scoring='accuracy' )
clf.fit(processed_no_test, label_list_train + list(s4vm_labels))

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
tsvm_svm = clf.best_estimator_
predicted_test_labels_tsvm = tsvm_svm.predict(processed_test)
mat = confusion_matrix(label_list_test, predicted_test_labels_tsvm)
plt.figure(0)
sns.heatmap(mat.T, square=True, annot=True, fmt='d', cbar=False,xticklabels=[-1,1],yticklabels=[-1,1])
plt.xlabel('True Label')
plt.ylabel('Predicted Label')
plt.title('S4VM')

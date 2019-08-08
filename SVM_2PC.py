# -*- coding: utf-8 -*-

# 2 Principal Components

print("# Tuning hyper-parameters for accuracy")
print()

clf = GridSearchCV(SVC(probability = True), tuned_parameters, cv=5,
                       scoring='accuracy' )
clf.fit(processed_train[:,0:2], label_list_train)

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
svm_2D = clf.best_estimator_
predicted_test_labels_2D = svm_2D.predict(processed_test[:,0:2])
mat = confusion_matrix(label_list_test, predicted_test_labels_2D)
plt.figure(0)
sns.heatmap(mat.T, square=True, annot=True, fmt='d', cbar=False,xticklabels=[-1,1],yticklabels=[-1,1])
plt.xlabel('True Label')
plt.ylabel('Predicted Label')

# Training accuracy
predicted_train_labels_2D = svm_2D.predict(processed_train[:,0:2])
mat = confusion_matrix(label_list_train, predicted_train_labels_2D)
plt.figure(1)
sns.heatmap(mat.T, square=True, annot=True, fmt='d', cbar=False,xticklabels=[-1,1],yticklabels=[-1,1])
plt.xlabel('True Label')
plt.ylabel('Predicted Label')


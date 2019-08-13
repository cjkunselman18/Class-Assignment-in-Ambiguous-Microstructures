# -*- coding: utf-8 -*-

# Check the first criterion

clusters_test, centers_test = cop_kmeans(dataset=processed[0:192,:], k=2, ml=must_link,cl=cannot_link)

# remember this is an unsupervised process with no real label information going into it;
# the algorithm will give two clusters, but we have to look into it to see which cluster
# labels correspond to our initial labels
precip_cluster_label_test = clusters_test[precip_sample]
bicontin_cluster_label_test = clusters_test[bicontin_sample]

for i in range(0,192):
    if clusters_test[i] == precip_cluster_label_test:
        clusters_test[i] = 1
    else:
        clusters_test[i] = -1
        
cop_kmeans_labels_test = clusters_test[153:192]

criterion_check = np.amax(abs(np.array(label_list_test) - np.array(cop_kmeans_labels_test))) == 0
print(criterion_check)
# Failed for the provided problem

# Check the second criterion 
label_list_cop = label_list_train + cop_kmeans_labels

# tune kernel/hyper-parameters
print("# Tuning hyper-parameters for accuracy")
print()

clf = GridSearchCV(SVC(probability = True), tuned_parameters, cv=5,
                       scoring='accuracy' )
clf.fit(processed_no_test, label_list_cop)

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
cop_svm = clf.best_estimator_
predicted_test_labels_cop = cop_svm.predict(processed_test)
mat = confusion_matrix(label_list_test, predicted_test_labels_cop)
plt.figure(0)
sns.heatmap(mat.T, square=True, annot=True, fmt='d', cbar=False,xticklabels=[-1,1],yticklabels=[-1,1])
plt.xlabel('True Label')
plt.ylabel('Predicted Label')

# Training accuracy
predicted_train_labels_cop = cop_svm.predict(processed_train)
mat = confusion_matrix(label_list_train, predicted_train_labels_cop)
plt.figure(1)
sns.heatmap(mat.T, square=True, annot=True, fmt='d', cbar=False,xticklabels=[-1,1],yticklabels=[-1,1])
plt.xlabel('True Label')
plt.ylabel('Predicted Label')

# Similar to the results in the paper on the full dataset, this method failed both criteria, but it 
# did not fail the second by much


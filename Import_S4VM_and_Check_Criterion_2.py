# -*- coding: utf-8 -*-

import xlrd

# read in new labels
book = xlrd.open_workbook("S4VM_Prediction.xlsx")
sheet = book.sheet_by_index(0)
s4vm_labels = []
for i in range(0,52):
    s4vm_labels.append(sheet.cell_value(i+1,0))
    
# update training set
label_list_s4vm = label_list_train + s4vm_labels

# tune kernel/hyper-parameters
print("# Tuning hyper-parameters for accuracy")
print()

clf = GridSearchCV(SVC(probability = True), tuned_parameters, cv=5,
                       scoring='accuracy' )
clf.fit(processed_no_test, label_list_s4vm)

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
s4vm_svm = clf.best_estimator_
predicted_test_labels_s4vm = s4vm_svm.predict(processed_test)
mat = confusion_matrix(label_list_test, predicted_test_labels_s4vm)
plt.figure(0)
sns.heatmap(mat.T, square=True, annot=True, fmt='d', cbar=False,xticklabels=[-1,1],yticklabels=[-1,1])
plt.xlabel('True Label')
plt.ylabel('Predicted Label')

# Training accuracy
predicted_train_labels_s4vm = s4vm_svm.predict(processed_train)
mat = confusion_matrix(label_list_train, predicted_train_labels_s4vm)
plt.figure(1)
sns.heatmap(mat.T, square=True, annot=True, fmt='d', cbar=False,xticklabels=[-1,1],yticklabels=[-1,1])
plt.xlabel('True Label')
plt.ylabel('Predicted Label')



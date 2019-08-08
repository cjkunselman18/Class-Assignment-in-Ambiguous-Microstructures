# -*- coding: utf-8 -*-

# 1 Principal Component
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix
import seaborn as sns; sns.set()
from sklearn import preprocessing
import warnings
warnings.filterwarnings("ignore")

# We first need to standardize the data, and then separate it back into training/test/unlabeled (another
# option would be to standardize the training data and then transform the test and initially unlabeled sets)
unprocessed = np.ones((244,3))
unprocessed[0:153] = projected_train[:,0:3]
unprocessed[153:192] = projected_test[:,0:3]
unprocessed[192:244] = projected_unknown[:,0:3]
processed = preprocessing.scale(unprocessed)
processed_train = processed[0:153,:]
processed_test = processed[153:192,:]
processed_unknown = processed[192:244,:]



# Kernel/Hyper-parameter selection
# Note that if there is a tie, linear kernels, and lower values of C and gamma will be used

tuned_parameters = [{'kernel': ['linear'], 'C': [1, 10, 100, 1000,10000]},{'kernel': ['rbf'], 'gamma': [1e-3, 1e-4,1e-2,1e-1],
                     'C': [1,10,100, 1000,10000]}]




print("# Tuning hyper-parameters for accuracy")
print()

clf = GridSearchCV(SVC(probability = True), tuned_parameters, cv=5,
                       scoring='accuracy' )
clf.fit(processed_train[:,0].reshape(-1,1), label_list_train)

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
svm_1D = clf.best_estimator_
predicted_test_labels_1D = svm_1D.predict(processed_test[:,0].reshape(-1,1))
mat = confusion_matrix(label_list_test, predicted_test_labels_1D)
plt.figure(0)
sns.heatmap(mat.T, square=True, annot=True, fmt='d', cbar=False,xticklabels=[-1,1],yticklabels=[-1,1])
plt.xlabel('True Label')
plt.ylabel('Predicted Label')

# Training accuracy
predicted_train_labels_1D = svm_1D.predict(processed_train[:,0].reshape(-1,1))
mat = confusion_matrix(label_list_train, predicted_train_labels_1D)
plt.figure(1)
sns.heatmap(mat.T, square=True, annot=True, fmt='d', cbar=False,xticklabels=[-1,1],yticklabels=[-1,1])
plt.xlabel('True Label')
plt.ylabel('Predicted Label')



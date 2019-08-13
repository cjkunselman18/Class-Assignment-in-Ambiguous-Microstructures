
% read in data from excel document
data = readtable('Processed Autocorrelation Data.xlsx');
labels = readtable('Processed Autocorrelation Data Labels.xlsx');

% the above command turns the data into tables -- use this to get arrays
data = table2array(data);
labels = table2array(labels);

% get inputs from read-in data
X_train = data(1:153,:);
X_unknown = data(193:244,:);
labels_train = labels(1:153);

% parameters - C1 is from the baseline SVM, and the rest are defaults
C1 = 10;
C2 = 0.1;
gamma = 0;
sampleTime = 100;

% run S4VM; "prediction_unlabeled" is the predicted labels for the unlabeled set
% the linear kernel is from the baseline SVM
addpath('libsvm-mat-2.89-3-box constraint');
prediction_unlabeled = S4VM(X_train,labels_train,X_unknown,'Linear',C1,C2,sampleTime,gamma);

% check the first criterion - that the S4VM method labels the test set correctly
X_test = data(154:192,:);
prediction_test = S4VM(X_train,labels_train,X_test,'Linear',C1,C2,sampleTime,gamma);

% if this is true, the method passes
max(abs(prediction_test - labels(154:192))) == 0
% for the problem as structured, it passes!

% write to new excel document so we can load these results back into python
prediction_table = array2table(prediction_unlabeled)
filename = 'S4VM_Prediction.xlsx'
writetable(prediction_table,filename)

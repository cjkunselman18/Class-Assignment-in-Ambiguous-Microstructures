This repository complements the paper "Semi-supervised Learning Approaches to Class Assignment in Ambiguous Microstructures" by providing
an example of the workflow on a small sample (10%) of the dataset. There are two options for you to explore this workflow:

1) Use the provided Jupyter Notebook and run the code cell-by-cell, or
2) Follow this guide to run each script in order.

To run the all of the python code, you will need the following packages:
scikit-image,
matlibplot,
SciPy,
scikit-learn v0.19.2 (PyMKS will not work if you have a newer version),
PyMKS (http://pymks.org/en/latest/rst/README.html),
numpy,
seaborn,
xlrd,
xlsxwriter,
statsmodels,
math,
and copkmeans (https://github.com/Behrouz-Babaki/COP-Kmeans).


The S4VM method is implemented in MATLAB and requires code from the authors 
(http://lamda.nju.edu.cn/code_S4VM.ashx?AspxAutoDetectCookieSupport=1). If you do not have access to MATLAB, there is an R implementation
which you can try which I have not tried (https://rdrr.io/cran/RSSL/man/S4VM.html). There is also an Excel spreadsheet in this repository
with results from this method on the specific problem posed in this example which can easily be imported into python.

If you choose to use the Jupyter notebook, you can stop here, open it up, and follow the instructions to run this example. If you choose
to run the scripts separately, follow the instructions below.

1) Download and save all of the files. Open Preprocess_Microstructure_Images.py and update the file paths for the dataset (the images in 
Example_Microstructures.zip). Run this script. The data is now binarized and ready for characterization.

2) Open Characterization_Normalized_Black_Autocorrelation.py. If you would like to a visualization of the black autocorrelation metric, uncomment the appropriate line in the script. Run this script. All normalized black autocorrelations are now calculated.

3) Open Split_Train_Test.py. Similar to the paper, this example is set for a test set of about 20% of the initially labeled samples and
the random seed is set for reproducibility. I recommend not changing these values until you run through the example at least once. Also,
changes to test set size will require changes to many other scripts. Run this script. You now have labeled training and test sets.

4) Open either PCA_on_Normalized_Correlations.py or IPCA_on_Normalized_Correlations.py. The dataset in this example is small enough for you to use regular PCA, but if you want to follow the paper method more closely, you can use IPCA instead. PCA is performed on a combination of the labeled training and ambiguous sets, and the labeled test set is projected into the resulting subspace. Run one of these scripts (this example assumes regular PCA is used). The feature space is now reduced to fifty dimensions. Note that using IPCA (and tweaking the batch size) can change hyperparameter selection in the next step.

5) Open Train_Baseline_SVM.py. This is the SVM trained only on the initially labeled training set. Run this script. Training and test error estimates can be calculated from the resulting confusion matrices.

6) Open Modified_Yarowsky.py and run. The remaining semi-supervised methods can be completed in any order. For Label Propagation and COP-KMEANS, just open the .py files and execute. As mentioned above, S4VM is implemented in MATLAB. If you do not want to bother with transferring data, the results for the specific example set up in this code are in S4VM_Label_Prediction.xlsx. If you want to go through the whole process, open Export_S4VM.py and run. This will produce an excel files called Processed Auto Correlation Data.xlsx and Processed Auto Correlation Data Labels.xlsx. Put these files into the same folder as the code for the S4VM method. Open Matlab_S4VM.m in Matlab and run. This will produce an excel file called S4VM_Label_Prediction.xlsx (and it should match the file available in this respository if you are following the example). Close MATLAB and move this file to your working directory for python. Open Import_S4VM_Results.py and run. You now have labels for the ambiguous set from all four semi-supervised methods.

7) Open Train_Updated_SVM.py and run. This script will identify the subset of ambiguous points which have a labelling consensus from the methods in step (6), add this subset to the training set, and train a new SVM over this appended training set. Then open McNemar_Test.py and run. This script constructs the contingency table for the baseline and updated SVMs and performs McNemar's test. If you followed the provided example exactly, the sum of discordant pairs is only 1, so the exact version of the test is used.



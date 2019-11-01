from statsmodels.stats.contingency_tables import mcnemar

# First we need to see where the baseline and updated SVMs make correct and incorrect predictions
baseline_test_contingency = []
updated_test_contingency = []
for i in range(0,39):
    if (predicted_test_labels_baseline[i] == label_list_test[i]):
        baseline_test_contingency.append(1)
    else:
        baseline_test_contingency.append(0)
    if (predicted_test_labels_updated[i] == label_list_test[i]):
        updated_test_contingency.append(1)
    else:
        updated_test_contingency.append(0)
 
# Then we build the contingency table by comparing the above results
contingency_table = [[0,0],[0,0]]
for i in range(0,39):
    if (baseline_test_contingency[i] == 1 and updated_test_contingency[i] == 1):
        contingency_table[0][0] = contingency_table[0][0] + 1
    if (baseline_test_contingency[i] == 1 and updated_test_contingency[i] == 0):
        contingency_table[0][1] = st_test_table[0][1] + 1
    if (baseline_test_contingency[i] == 0 and updated_test_contingency[i] == 1):
        contingency_table[1][0] = st_test_table[1][0] + 1
    if (baseline_test_contingency[i] == 0 and updated_test_contingency[i] == 0):
        contingency_table[1][1] = st_test_table[1][1] + 1
        
# this runs McNemar's test and gives us a pvalue
mcnemar_result = mcnemar(contingency_table, exact=True)
print(mcnemar_result.pvalue) 

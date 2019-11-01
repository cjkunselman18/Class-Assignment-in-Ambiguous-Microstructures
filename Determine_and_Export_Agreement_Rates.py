# MY is 1
# LP is 2
# CKM is 3
# S4VM is 4
# Updated is 5

my_labels = st_svm.predict(processed_unknown)
lp_labels = lp_svm.predict(processed_unknown)
ckm_labels = ckm_svm.predict(processed_unknown)
tsvm_labels = tsvm_svm.predict(processed_unknown)
up_labels = updated_svm.predict(processed_unknown)

# The counter list is counting how many points the given set of classifiers agree on. The first entry is for subset {1,2}, the
# second is {1,3}, the third is {1,4}, and so on. 
counter = np.zeros(26)
for i in range(0,52):
    if my_labels[i] == lp_labels[i]:                    # {1,2}
        counter[0] = counter[0] + 1
    if my_labels[i] == ckm_labels[i]:                   # {1,3}
        counter[1] = counter[1] + 1
    if my_labels[i] == tsvm_labels[i]:                  # {1,4}
        counter[2] = counter[2] + 1
    if my_labels[i] == up_labels[i]:                    # {1,5}
        counter[3] = counter[3] + 1
    if lp_labels[i] == ckm_labels[i]:                   # {2,3}
        counter[4] = counter[4] + 1
    if lp_labels[i] == tsvm_labels[i]:                  # {2,4}
        counter[5] = counter[5] + 1
    if lp_labels[i] == up_labels[i]:                    # {2,5}
        counter[6] = counter[6] + 1
    if tsvm_labels[i] == ckm_labels[i]:                 # {3,4}
        counter[7] = counter[7] + 1
    if up_labels[i] == ckm_labels[i]:                   # {3,5}
        counter[8] = counter[8] + 1
    if tsvm_labels[i] == up_labels[i]:                  # {4,5}
        counter[9] = counter[9] + 1
    if (my_labels[i] == ckm_labels[i] and my_labels[i] == lp_labels[i]):      # {1,2,3}
        counter[10] = counter[10] + 1
    if (my_labels[i] == tsvm_labels[i] and my_labels[i] == lp_labels[i]):     # {1,2,4}
        counter[11] = counter[11] + 1
    if (my_labels[i] == up_labels[i] and my_labels[i] == lp_labels[i]):       # {1,2,5}
        counter[12] = counter[12] + 1
    if (my_labels[i] == tsvm_labels[i] and my_labels[i] == ckm_labels[i]):    # {1,3,4}
        counter[13] = counter[13] + 1
    if (my_labels[i] == up_labels[i] and my_labels[i] == ckm_labels[i]):      # {1,3,5}
        counter[14] = counter[14] + 1
    if (my_labels[i] == tsvm_labels[i] and my_labels[i] == up_labels[i]):     # {1,4,5}
        counter[15] = counter[15] + 1
    if (ckm_labels[i] == tsvm_labels[i] and ckm_labels[i] == lp_labels[i]):   # {2,3,4}
        counter[16] = counter[16] + 1
    if (ckm_labels[i] == up_labels[i] and ckm_labels[i] == lp_labels[i]):     # {2,3,5}
        counter[17] = counter[17] + 1
    if (up_labels[i] == tsvm_labels[i] and up_labels[i] == lp_labels[i]):     # {2,4,5}
        counter[18] = counter[18] + 1
    if (ckm_labels[i] == tsvm_labels[i] and ckm_labels[i] == up_labels[i]):   # {3,4,5}
        counter[19] = counter[19] + 1
    if (my_labels[i] == lp_labels[i] and my_labels[i] == ckm_labels[i] and my_labels[i] == tsvm_labels[i]):  # {1,2,3,4}
        counter[20] = counter[20] + 1
    if (my_labels[i] == lp_labels[i] and my_labels[i] == ckm_labels[i] and my_labels[i] == up_labels[i]):    # {1,2,3,5}
        counter[21] = counter[21] + 1
    if (my_labels[i] == lp_labels[i] and my_labels[i] == up_labels[i] and my_labels[i] == tsvm_labels[i]):   # {1,2,4,5}
        counter[22] = counter[22] + 1
    if (my_labels[i] == up_labels[i] and my_labels[i] == ckm_labels[i] and my_labels[i] == tsvm_labels[i]):  # {1,3,4,5}
        counter[23] = counter[23] + 1
    if (up_labels[i] == lp_labels[i] and up_labels[i] == ckm_labels[i] and up_labels[i] == tsvm_labels[i]):  # {2,3,4,5}
        counter[24] = counter[24] + 1
    if (my_labels[i] == lp_labels[i] and my_labels[i] == ckm_labels[i] and my_labels[i] == tsvm_labels[i] and my_labels[i] == up_labels[i]):  # {1,2,3,4,5}
        counter[25] = counter[25] + 1
        
        
        # Now we need to export these values for optimization in Matlab
        workbook = xlsxwriter.Workbook('Agreement Counts.xslx')
        worksheet = workbook.add_worksheet
        
        worksheet.write(0,0, 'Agreement Counts')
        worksheet.write_column(1,0, counter.T)
        
        workbook.close()
        

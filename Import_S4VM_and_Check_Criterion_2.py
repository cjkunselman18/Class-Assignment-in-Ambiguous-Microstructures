# -*- coding: utf-8 -*-

import xlrd

# read in new labels
book = xlrd.open_workbook("S4VM_Label_Prediction.xlsx")
sheet = book.sheet_by_index(0)
s4vm_labels = []
for i in range(0,52):
    s4vm_labels.append(sheet.cell_value(i+1,0))
    




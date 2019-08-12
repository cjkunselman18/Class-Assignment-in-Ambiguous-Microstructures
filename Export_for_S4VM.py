# -*- coding: utf-8 -*-

import xlsxwriter

workbook = xlsxwriter.Workbook('Processed Autocorrelation Data.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write(0,0, 'PC1')
worksheet.write(0,1, 'PC2')
worksheet.write(0,2, 'PC3')

row = 1

for col, data in enumerate(processed_no_test.T):
    worksheet.write_column(row, col, data)


workbook.close()

workbook = xlsxwriter.Workbook('Processed Auto Correlation Data Labels.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write(0,0, 'labels')
worksheet.write_column(1,0, np.array(label_list_train).T)


workbook.close()


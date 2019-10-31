# -*- coding: utf-8 -*-

import xlsxwriter

workbook = xlsxwriter.Workbook('Processed Autocorrelation Data.xlsx')
worksheet = workbook.add_worksheet()

for i in range(1,51):
    worksheet.write(0,i-1, 'PC%s' % (i))


row = 1

for col, data in enumerate(processed.T):
    worksheet.write_column(row, col, data)


workbook.close()

workbook = xlsxwriter.Workbook('Processed Autocorrelation Data Labels.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write(0,0, 'labels')
worksheet.write_column(1,0, np.array(label_list_train + label_list_test).T)


workbook.close()


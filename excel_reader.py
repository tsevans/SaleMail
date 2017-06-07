import os
from os.path import join, dirname, abspath
import xlrd

excel_filename = join(dirname(abspath(__file__)), 'sample_data.xlsx')
book = xlrd.open_workbook(excel_filename)
sheet = book.sheet_by_index(0)

col_headers = sheet.row(0)
from xlrd.sheet import ctype_text

for idx, cell_obj in enumerate(col_headers):
    print('%s' % cell_obj.value)
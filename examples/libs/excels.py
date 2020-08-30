
import re
import xlrd


def read_excel(path, sheet):
    workbook = xlrd.open_workbook(path)
    booksheet = workbook.sheet_by_name(sheet)
    p = list()
    for row in range(booksheet.nrows):
        row_data = []
        for col in range(booksheet.ncols):
            cel = booksheet.cell(row, col)
            val = cel.value
            try:
                val = cel.value.strip()
            except:
                pass

            if type(val) == float:
                val = int(val)
            else:
                val = str.strip(str(val))
            row_data.append(val)
        p.append(row_data)
    return p

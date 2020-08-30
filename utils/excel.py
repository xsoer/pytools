#!/usr/bin/env python
# coding=utf-8
# @Time    : 2018-06-23 13:09
# @Author  : zhangxicheng
# @Email   : zhangxicheng@jingdata.com
# @File    : excel_writer
# @Desc    :

import xlsxwriter
import xlrd
import re


class ExcelWriter:
    def __init__(self, excel_name, options=None):
        self.wb = xlsxwriter.Workbook(excel_name, options)

    def add_sheet(self, sheet_name="sheet-1"):
        ws = self.wb.add_worksheet(sheet_name)
        return ws

    def close(self):
        self.wb.close()

    def write_sheet(self, ws, data, title=[]):
        if data:
            ws.write_row('A1', title)

            for k, row in enumerate(data):
                ws.write_row(k+1, 0, row)
        else:
            print("no data")


def reade_excel(path, sheet):
    """读取excel内容"""
    workbook = xlrd.open_workbook(path)
    booksheet = workbook.sheet_by_name(sheet)
    data = list()
    for row in range(booksheet.nrows):
        row_data = []
        for col in range(booksheet.ncols):
            cel = booksheet.cell(row, col)
            val = cel.value
            try:
                val = cel.value
                val = re.sub(r'\s+', '', val)
            except:
                pass

            if type(val) == float:
                val = int(val)
            else:
                val = str(val)
            row_data.append(val)
        data.append(row_data)
    return data

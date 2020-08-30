#!/usr/bin/env python
# -*- coding: utf8 -*-

import traceback
import xlwt,xlrd
import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

class ExcelWriter():
    def __init__(self):
        self.wb = xlwt.Workbook(encoding='utf-8')
        self.wb.set_tab_width(10000)
        self.wb.set_width(10000)

    def add_new_sheet(self, sname="sheet-1"):
        bs = self.wb.add_sheet(sname, cell_overwrite_ok=True)
        return bs

    def save_excel(self, fname):
        self.wb.save(fname)

    def write_sheet(self, bs, datas, head=[], title="", clos_width=[], head_h=[]):
        style = xlwt.easyxf('align: wrap on, vert center, horiz left;')
        style2 = xlwt.easyxf('align: vert center, horiz center;')
        if datas:
            kk = 0
            len_col = len(datas[0])
            if title:
                bs.write_merge(0,0,0,len_col-1, title, style2)
                kk = 1
            if clos_width:
                for i,v in enumerate(clos_width):
                    bs.col(i).width = v
            else:
                for i in range(len_col):
                    bs.col(i).width = 5000

            h_fix = 0
            if head_h:
                jj = 0
                for j,v in enumerate(head_h):
                    [vv, col, raw] = v
                    bs.write_merge(kk,kk+raw-1,jj,jj+col-1, vv, style2)
                    jj += col
                    if raw>1:
                        h_fix += col
                kk += 1

            if head:
                for j,v in enumerate(head):
                    bs.write(kk, j+h_fix, v, style2)
                kk += 1
            for i,data in enumerate(datas):
                for j,v in enumerate(data):
                    bs.write(i+kk, j, v, style)


# -*- coding: utf-8 -*-
# Version   : python3
# Date       : 2018-3-14 11:49:29
# Author     : cc
# Description: import excel data to wiki/html/markdown table

import xlrd


class Xlsx(object):
    """ 解析Excel文件 """

    def __init__(self, filename=None, sheetname="Sheet1"):
        super(Xlsx, self).__init__()

        self.filename = ""
        if filename:
            self.filename = filename
            self.data = xlrd.open_workbook(filename)
            self.table = self.data.sheet_by_name(sheetname)
            self.rows = self.table.nrows
            self.cols = self.table.ncols
            self.merged_cells = self.table.merged_cells
            self.text = ""
            self.outfile = filename.split(".")[0] + ".log"

    def is_merged_cell(self, row, col):
        """ 判断某个行列坐标是否是合并的单元格，是则返回合并的单元格坐标 """
        for coords in self.merged_cells:
            if coords[0] <= row < coords[1] and coords[2] <= col < coords[3]:
                return coords

        return False

    def out_put(self):
        """ 将转换后的文本信息写到log文件 """
        with open(self.outfile, "w", encoding="utf-8") as wf:
            wf.write(self.text)
        print(self.text)
        print("text output to file:{}".format(self.outfile))


class XlsxToWiki(Xlsx):
    """ 将Xslx文件内容解析成wiki表格 """

    def __init__(self, filename=None, sheetname="Sheet1"):
        super(XlsxToWiki, self).__init__(filename, sheetname)
        self.to_wiki()

    def to_wiki(self):
        """ 将excel导出成wiki表格 """

        for row in range(self.rows):
            for col in range(self.cols):
                posts = self.is_merged_cell(row, col)

                if not posts:
                    if row == 0:
                        self.text = "{}|_.{}".format(self.text, self.table.cell_value(row, col))
                    else:
                        self.text = "{}|{}".format(self.text, self.table.cell_value(row, col))
                else:
                    nr = posts[1] - posts[0]
                    nc = posts[3] - posts[2]
                    if row == posts[0] and col == posts[2]:
                        self.text = "{}|_/{}\\{}.{}".format(self.text, nr, nc, self.table.cell_value(row, col))

            self.text = "{}|\n".format(self.text)

        return self.text


class XlsxToHtml(Xlsx):
    """ 将excel导出成html表格 """

    def to_html(self):
        pass


class XlsxToMarkdown(Xlsx):
    """ 将excel导出成markdown表格 """

    def to_markdown(self):
        pass


if __name__ == "__main__":
    x = XlsxToWiki("test.xlsx")
    x.out_put()


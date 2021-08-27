# -*-coding:utf-8 -*-
'''
封装读写文件类，后续用于处理接口请求数据
读取url、params、token等信息
写入接口返回状态码或者返回json数据、更新时间..
attention:2.0.1版本的xlrd只支持xls文件，不能打开xlsx文件
'''
import xlrd


class ReadWriteExcel:

    def read_excel(self, filepath):
        tables = []
        # 打开文件
        workbook = xlrd.open_workbook(filepath)
        # 获取所有sheet
        sheet_name = workbook.sheet_names()[0]
        # 根据sheet索引或者名称获取sheet内容
        sheet = workbook.sheet_by_index(0)  # sheet索引从0开始
        # sheet = workbook.sheet_by_name('Sheet1')
        # print (workboot.sheets()[0])
        # sheet的名称，行数，列数
        print(sheet.name, sheet.nrows, sheet.ncols)

        # 获取整行和整列的值（数组）
        rows = sheet.row_values(1)  # 获取第2行内容
        cols = sheet.col_values(2)  # 获取第3列内容
        print(rows)
        print(cols)

        for rown in range(sheet.nrows):
            array = {'L1': sheet.cell_value(rown, 0), 'L2': sheet.cell_value(rown, 1), 'L3': sheet.cell_value(rown, 2),
                     'L4': sheet.cell_value(rown, 3),  'L5': sheet.cell_value(rown, 4),
                     'L6': sheet.cell_value(rown, 5)}
            tables.append(array)

        print(len(tables))
        print(tables)
        # print (tables[5])

    def update_excel(self):
        pass


if __name__ == '__main__':
    A = ReadWriteExcel()
    A.read_excel(r'/home/zach/pystore/PycharmProjects/ApiAutoTest/templates/ZACH工作周报-2021（8.16-8.20).xls')

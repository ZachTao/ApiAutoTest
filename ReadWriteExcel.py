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
        urls = []
        params = []
        paramvals = []
        keys = []
        rtunfmats = []
        isruns = []
        # 打开文件
        workbook = xlrd.open_workbook(filepath)
        '''
        # 获取sheetname,也可以获取sheet后获取属性sheet.name
        sheet_name = workbook.sheet_names()[0]
        print('sheet_name'+sheet_name)
        '''
        sheet = workbook.sheet_by_index(0)  # sheet索引从0开始，获取第一个sheet页面内容
        # sheet的名称，行数，列数
        print(sheet.name, sheet.nrows, sheet.ncols)
        '''
        获取整行和整列的值（数组）
        rows = sheet.row_values(1)  # 获取第2行内容
        cols = sheet.col_values(2)  # 获取第3列内容
        print(rows)
        print(cols)
        '''
        for row in range(sheet.nrows):
            rowvalue = sheet.row_values(row)
            print(rowvalue)
        # sheet.cell_value(rown, 0) 获取具体单元格参数值
        for row in range(sheet.nrows-1):
            urlval = sheet.cell_value(row+1, 4)
            param = sheet.cell_value(row+1, 6)
            paramval = sheet.cell_value(row+1, 7)
            key = sheet.cell_value(row+1, 8)
            rtunfmat = sheet.cell_value(row+1, 10)
            isrun = sheet.cell_value(row+1, 13)
            urls.append(urlval)
            params.append(param)
            paramvals.append(paramval)
            keys.append(key)
            rtunfmats.append(rtunfmat)
            isruns.append(isrun)
        return urls, params, paramvals, keys, rtunfmats, isruns

    def update_excel(self):
        pass


if __name__ == '__main__':
    A = ReadWriteExcel()
    A.read_excel(r'/home/zach/pystore/PycharmProjects/ApiAutoTest/templates/ApiData.xls')

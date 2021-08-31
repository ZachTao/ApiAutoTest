# -*-coding:utf-8 -*-
from ReadWriteExcel import ReadWriteExcel


class DealParams:

    def dealparams(self, filpath):
        headers = {
            'user - agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                            '(KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.84'
        }
        get_pm = ReadWriteExcel()   # 一定要先实例化再引用类方法
        pms = get_pm.read_excel(filpath)
        for pm in pms:
            req_typ = pm['req_type']
            url_var = pm['url_val']
            # 组合params
            paras = {
                'key': pm['key'],
                'dtype': pm['rtunfmat'],
            }
            lins = pm['param'].split('&')
            linvs = str(pm['param_val']).split('&')
            for i in range(len(lins)):
                paras[lins[i]] = linvs[i]
            return req_typ, url_var, paras, headers



if __name__ == '__main__':
    requ = DealParams()
    requ.dealparams(r'/home/zach/pystore/PycharmProjects/ApiAutoTest/case_excel/ApiData.xls')


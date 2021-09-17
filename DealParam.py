# -*-coding:utf-8 -*-
from ReadWriteExcel import ReadWriteExcel
from splitlist import list_of_groups


class DealParams:

    def dealparams(self, filpath):
        Jihe = []
        get_pm = ReadWriteExcel()
        pms = get_pm.read_excel(filpath)
        # print(pms)
        for pm in pms:
            req_typ = pm['req_type']
            Jihe.append(req_typ)
            url_var = pm['url_val']
            Jihe.append(url_var)
            # 组合params
            paras = {
                'key': pm['key'],
                'dtype': pm['rtunfmat'],
            }
            lins = pm['param'].split('&')
            linvs = str(pm['param_val']).split('&')
            for i in range(len(lins)):
                paras[lins[i]] = linvs[i]
            Jihe.append(paras)
        ret = list_of_groups(Jihe, 3)
        return ret


if __name__ == '__main__':
    requ = DealParams()
    requ.dealparams(r'F:\PycharmProjects\ApiAutoTest\case_excel\ApiData.xls')

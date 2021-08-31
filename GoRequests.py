# -*-coding:utf-8 -*-
import requests
import logging
from parameterized import parameterized
from DealParams import DealParams


class GoRequests:

    @parameterized.expand(DealParams())
    # 上面返回的参数需要是List
    def reqgo(self, reqmethod, requrl, regparams, headers):
        try:
            if reqmethod == ("post" or "POST"):
                results = requests.post(requrl, regparams, headers=headers)
            elif reqmethod == ("get" or "GET"):
                results = requests.get(requrl, regparams, headers=headers)
            elif reqmethod == "put":
                results = requests.put(requrl, regparams, headers=headers)
            elif reqmethod == "patch":
                results = requests.patch(requrl, regparams, headers=headers)
            # elif reqmethod == "options":
            #     results = requests.options(requrl, headers=headers)
            # elif reqmethod == "delete":
            #     results = requests.delete(requrl, headers=headers)
            response = results.json()
            # print(response)
            code = response.get("reason")
            return code
        except Exception as e:
            logging.error("service is error", e)


if __name__ == '__main__':
    GoRequests()

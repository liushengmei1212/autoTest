import json

import requests

from src.utils.ExcelToJson import excelToJson


class requestUtil():
    def sendRequest(self, application, text):
        apiJson = excelToJson.readExcel(self)
        apis_dic_list = json.loads(apiJson)
        # print(apis_dic_list)

        for i in range(0, len(apis_dic_list)):
            apis_dic = apis_dic_list[i]
            if application in apis_dic.keys():
                apisList = apis_dic[application]
                for j in range(0, len(apisList)):
                    if apisList[j]["描述"] == text:
                        api_dic = apisList[j]
                        break
        header = api_dic["请求头"]
        param = api_dic["参数"]
        if header == '':
            header = ''
        else:
            header = eval(header)
        if api_dic["方式"] == 'post':
            param = json.loads(param)
            re = requests.request(method=api_dic["方式"], url=api_dic["URL"], data=json.dumps(param), headers=header)
        else:
            re = requests.request(method=api_dic["方式"], url=api_dic["URL"], headers=header)
        return re

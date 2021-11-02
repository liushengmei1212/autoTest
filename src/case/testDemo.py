from src.utils.RequestUtil import requestUtil


class testDemo:
    def test_programOpen(self):
        re=requestUtil.sendRequest(self,"playout","getVersion")
        print(re.json())

        re = requestUtil.sendRequest(self, "playout", "page")
        print(re.json())

        re = requestUtil.sendRequest(self, "playout", "listMember")
        print(re.json())

        re = requestUtil.sendRequest(self, "playout", "info")
        print(re.json())

        re = requestUtil.sendRequest(self, "playout", "add")
        print(re.json())

obj=testDemo()
obj.test_programOpen()
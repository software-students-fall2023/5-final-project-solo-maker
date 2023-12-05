import urllib.request
import json

# class Spider:
#     def __init__(self):
#         self.siteURL = 'http://space.bilibili.com/ajax/channel/getChannel?mid=546195&guest=1'
#
#     def getPage(self):
#         request = urllib.request.Request(self.siteURL)
#         with urllib.request.urlopen(request) as response:
#             return response.read().decode('utf-8')
#
#     def getContents(self):
#         page = self.getPage()
#         # 解析返回的 JSON 数据
#         json_data = json.loads(page)
#         # 根据实际情况进行解析和处理
#         return json_data
#
# spider = Spider()
# res = spider.getContents()
class Spider:
    def __init__(self, url):
        self.siteURL = url

    def getPage(self):
        request = urllib.request.Request(self.siteURL)
        with urllib.request.urlopen(request) as response:
            return response.read().decode('utf-8')

    def getContents(self):
        page = self.getPage()
        json_data = json.loads(page)
        return json_data

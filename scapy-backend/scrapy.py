import urllib.request
import json

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

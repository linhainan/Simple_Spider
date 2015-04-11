import urllib
import urllib.request
class HTMLClient:
    def GetPage(self, url):
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)' 
        headers = { 'User-Agent' : user_agent }
        req = urllib.request.Request(url, None, headers)
        res = urllib.request.urlopen(req)
        return res.read().decode("utf-8")

from tools.Simple_Parser import Simple_Parser
from tools.Simple_WebCatcher import HTMLClient
import json
class XQ_Spider:
    def Get_Json(self, page):
       myparser = Simple_Parser()
       return myparser.feed(str(page), 'SNB.data.req_isBrick = 0;', "SNB.data.statusType") 

if __name__ == '__main__':
    myclient = HTMLClient()
    mypage = myclient.GetPage("http://xueqiu.com/2821861040")
    xq_spider = XQ_Spider()
    xq_json = xq_spider.Get_Json(mypage)
    infile = input('>')
    with open("xq_article.txt", 'wb') as xqfile:
        for item in xq_json:
            s = item.find('{')
            e = item.rfind('}')
            content = item[s:e+1]
            xml_content = json.loads(content)
            for status in xml_content["statuses"]:
                xqfile.write(bytes(status["title"], 'utf-8'))
                xqfile.write(b'\n')
                xqfile.write(bytes(status["text"], 'utf-8'))
                print(status["title"])
            #xqfile.write(bytes(str(xml_content["statuses"][0]), 'utf-8'))
        xqfile.close()

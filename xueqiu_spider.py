from tools.Simple_Parser import Simple_Parser
from tools.Simple_WebCatcher import HTMLClient
from tools.HTML2Doc import HTML2Doc
import json
class XQ_Spider:
    def __init__(self):
        self.myclient = HTMLClient()
    def Get_Json(self, page):
       myparser = Simple_Parser()
       return myparser.feed(str(page), 'SNB.data.req_isBrick = 0;', "SNB.data.statusType") 
    def Get_Div(self, page):
       myparser = Simple_Parser()
       return myparser.feed(str(page), '<div class="status-content">', "</div>") 
    def Get_Url(self, userid):
        pg = 1
        maxpg = 1000
        urlList = []
        retweetList = []
        while True:
            mypage = self.myclient.GetPage("http://xueqiu.com/" + userid +'?page=' + str(pg))#"2821861040")
            xq_spider = XQ_Spider()
            xq_json = xq_spider.Get_Json(mypage)
            #infile = input('>')
            
            for item in xq_json:
                s = item.find('{')
                e = item.rfind('}')
                content = item[s:e+1]
                xml_content = json.loads(content)
                maxpg = xml_content["maxPage"]
                for status in xml_content["statuses"]:
                    retweeded_status = status['retweet_status_id']
                    flag = True
                    for retweed in retweetList:
                        if retweed == str(retweeded_status):
                            flag = False
                    if flag == True:
                        print(str(status['target']))
                        urlList.append(str(status['target']))
                        if retweeded_status != 0:
                            retweetList.append(str(retweeded_status))
            pg += 1
            if pg > maxpg:
                break
        return urlList
    def Get_HTML(self, userid):
        urlList = self.Get_Url(userid)
        with open("xq_article_"+ userid +".txt", 'wb') as xqfile:
            xqfile.write(b'<head>')
            xqfile.write(b'<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">')
            xqfile.write(b'</head>')
            for url in urlList:
                #print(url)
                if url == None:
                    continue
                mypage = self.myclient.GetPage("http://xueqiu.com" + url)
                div_ctx = self.Get_Div(mypage)
                for ctx in div_ctx:
                    xqfile.write(bytes(ctx, 'utf-8'))
            xqfile.close()
    def Get_Doc(self, userid):
        urlList = self.Get_Url(userid)
        h2d = HTML2Doc()
        h2d.open('xq_' + userid + '.doc')
        for url in urlList:
            print(url)
            if url == None:
                continue
            mypage = self.myclient.GetPage("http://xueqiu.com" + url)
            div_ctx = self.Get_Div(mypage)
            for ctx in div_ctx:
               h2d.write(ctx) 

if __name__ == '__main__':
    xq_spider = XQ_Spider()
    #xq_spider.Get_HTML("2821861040")
    xq_spider.Get_Doc("2821861040")


#if __name__ == '__main__':
#    #myclient = HTMLClient()
#    #mypage = myclient.GetPage("http://xueqiu.com/2821861040")
#    #xq_spider = XQ_Spider()
#    #xq_json = xq_spider.Get_Json(mypage)
#    #infile = input('>')
#    #with open("xq_article.txt", 'wb') as xqfile:
#    #    for item in xq_json:
#    #        s = item.find('{')
#    #        e = item.rfind('}')
#    #        content = item[s:e+1]
#    #        xml_content = json.loads(content)
#    #        urlList = []
#    #        for status in xml_content["statuses"]:
#    #            urlList.append(status['target'])
#                xqfile.write(bytes(status["target"], 'utf-8'))
#                #xqfile.write(b'\n')
#                #xqfile.write(bytes(status["text"], 'utf-8'))
#                #print(status["title"])
#            #xqfile.write(bytes(str(xml_content["statuses"][0]), 'utf-8'))
#        xqfile.close()

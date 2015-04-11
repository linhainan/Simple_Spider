from tools.Simple_Parser import Simple_Parser
from tools.Simple_WebCatcher import HTMLClient
class JX3_Spider:
    def Get_News(self, page):
        myparser = Simple_Parser()
        return myparser.feed(page, u'<div class="news_list news_list02">', u'</div>');
    def Get_CSS(self, page):
        myparser = Simple_Parser()
        return myparser.feed(page, u'<link ', u'/>')

if __name__ == '__main__':
    myclient = HTMLClient()
    mypage = myclient.GetPage("http://xw.jx3.xoyo.com/news/")
    jx3_spider = JX3_Spider()
    jx3_news = jx3_spider.Get_News(mypage)
    jx3_css = jx3_spider.Get_CSS(mypage)
    infile = input('>')
    with open("jx3_news.html", 'wb') as jx3file:
        jx3file.write(b'<head>')
        jx3file.write(b'<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">')
        for item in jx3_css:
            jx3file.write(bytes(item, 'utf-8'))
        for item in jx3_news:
            jx3file.write(bytes(item, 'utf-8'))
        jx3file.close()

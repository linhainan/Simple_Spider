import re
import urllib
import urllib.request
import time
import string

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.links = []
        self.attrs = []
 
    def handle_starttag(self, tag, attrs):
        #print "Encountered the beginning of a %s tag" % tag
        if tag == "div":
            if len(attrs) == 0: pass
            else:
                #print(attrs)
                self.attrs = attrs
                for (variable, value)  in attrs:
                    if variable == "class":
                        if value == "ImgSearch":
                            print('find')
                #return attrs
    def handle_data(self, data):
        print(data)
        attrs = self.attrs
        for (variable, value)  in attrs:
            if variable == "class":
                if value == "ImgSearch":
                    print("data"+data)

class MyParser:
    def __init__(self):
        self.enable = True
        self.begin = 0
        self.end = 0
        self.dep = 0
        self.MyTool = HTML_Tool()
    def Parser(self, data, stag, etag):
        epos = 0
        npos = epos
        totallen = 0
        elen = len(etag)
        dlen = len(data)
        while True:
            epos = data[totallen:].find(etag)
            print("len" +str(epos))
            #print(repr(data[npos:npos+epos]))
            print(self.dep)
            #print(repr(data[npos]))
            if epos < 0:
                return -1
            else:
                count = data[totallen:epos+totallen].count(stag)
                self.dep += count
                
                self.dep -=1
                epos += elen
                totallen += epos
                if self.dep == 0:
                    return totallen
                if totallen >= dlen:
                    return -1
        return -1
    def savefile(self, content):
        with open("00001.html",'wb') as file:
            file.write(content)
        file.close()
    def feed(self, data, stag, etag):
        #data = self.MyTool.Replace_Char(str(data))
        npos = data.find('<div class="news_list news_list02">')
        print(data[npos:1000])
        if npos < 0:
            return -1
        
        nlen = self.Parser(str(data[npos:]), stag, etag)
        #print(data)
        #print(data[npos:])
        if nlen >= 0:
            #print(len(data[npos:nlen+npos]))
            self.savefile(bytes(data[npos:npos+nlen], "UTF-8"))
        else:
            #print(data[npos:])
            self.savefile(bytes(data[npos:], "UTF-8"))
        
            

class Simple_Spider:
    def __init__(self, url, filename, sflag, eflag):
        self.done = False
        self.sflag = sflag
        self.eflag = eflag
        self.fname = filename
        self.url = url
    def GetDiv(self, page):
        #ps = self.sflag + "(.*?)" + self.eflag
        #print(self.sflag)
        #pat = re.compile(r'<div class="ImgSearch"(.*)>(.*?)</div>', re.DOTALL)
        #items = pat.findall(page)
        #self.savefile(bytes(self.sflag, 'UTF-8'))
        #(items)
        #for item in items:
        #    print(item[0])
        #    io = input()
        #    self.savefile(bytes(item, 'UTF-8'))
        #self.savefile(bytes(self.eflag, 'UTF-8'))
        mypaser = MyParser()
        mypaser.feed(str(page), "<div", "</div>")
    def GetPage(self, url):
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)' 
        headers = { 'User-Agent' : user_agent }
        req = urllib.request.Request(url, None, headers)
        res = urllib.request.urlopen(req)
        print(req)
        return res.read().decode("utf-8")

    def Start(self):
        page = self.GetPage(self.url)
        self.GetDiv(page)
        cmd = input()

mySpider = Simple_Spider("http://xw.jx3.xoyo.com/news/", "jx3.html", '<div class="news_list news_list02">', u'</div>')
mySpider.Start()

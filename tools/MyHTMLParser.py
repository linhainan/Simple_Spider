from html.parser import HTMLParser
from docx import Document
from docx.shared import Inches
from tools.Simple_WebCatcher import HTMLClient
import os
import re
class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.links = []
        self.attrs = []
 
    def handle_starttag(self, tag, attrs):
        print("Encountered the beginning of a %s tag" % tag)
#        if tag == "div":
#            if len(attrs) == 0: pass
#            else:
#                #print(attrs)
#                self.attrs = attrs
#                for (variable, value)  in attrs:
#                    if variable == "class":
#                        if value == "ImgSearch":
#                            print('find')
#                #return attrs
#    def handle_data(self, data):
#        print(data)
#        attrs = self.attrs
#        for (variable, value)  in attrs:
#            if variable == "class":
#                if value == "ImgSearch":
#                    print("data"+data)
    def handle_endtag(self, tag):
        print("Encountered the beginning of a %s tag" % tag)
#html = MyHTMLParser()
#html.feed('<p>abcd</br></p>')
#html = 'c:/html/kkk/start'
#print(html.split(r'/')[-1])

class XQHTMLParser(HTMLParser):
    def __init__(self, docfile):
        HTMLParser.__init__(self)
        self.docfile = docfile
        self.doc = Document(docfile)
        self.myclient = HTMLClient()
        self.text = ''
        self.title = False
        self.picList=[]
    def handle_starttag(self, tag, attrs):
        #print "Encountered the beginning of a %s tag" % tag
        if re.match(r'h(\d)', tag):
            self.title = True 
        if tag == "img":
            if len(attrs) == 0: pass
            else:
                for (variable, value)  in attrs:
                    if variable == "src":
                        picdata = self.myclient.GetPic(value)
                        pictmp = value.split('/')[-1]
                        with open(pictmp, 'wb') as pic:
                            pic.write(bytes(picdata))
                            pic.close()
                        self.doc.add_picture(pictmp, width=Inches(1.25))
                        self.picList.append(pictmp)
    def handle_data(self, data):
        if self.title == True:
            self.doc.add_paragraph(self.text)
            self.text = ''
            self.doc.add_heading(data)
        else:
            self.text += data
    def handle_endtag(self, tag):
        if tag == 'br':
            self.doc.add_paragraph(self.text)
            self.text = ''
    def complete(self, html):
        self.feed(html)
        self.doc.save(self.docfile)
        for item in self.picList:
            os.remove(item)

#xq_parser = XQHTMLParser()
#xq_parser.feed('<img src="http://xavatar.imedao.com/community/201411/1418865775807-1418865776034.jpeg!50x50.png">')
#json = '<img src="http://xavatar.imedao.com/community/201411/1418865775807-1418865776034.jpeg!50x50.png">'
#xq_parser.complete(json, 'tmp.doc')
#doc.save('tmp.doc')

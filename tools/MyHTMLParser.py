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


import urllib.request
from bs4 import BeautifulSoup as Soup
import textwrap

class Googler:
    link="https://www.google.com/search?q="

    hdr = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}

    def __init__(self,value,pageTitle):

        self.scrapeLink=Googler.link+value
        self.request=urllib.request.Request(self.scrapeLink,headers=Googler.hdr)
        self.uClient = urllib.request.urlopen(self.request)
        self.page_html = self.uClient.read()
        self.uClient.close()
        self.page_soup = Soup(self.page_html, "html.parser")
        self.containers = self.page_soup.find_all("div", {"class": "g"})
        self.pageTitle=pageTitle
        #print(self.containers)

    def getInfo(self):
        for a in self.page_soup.find_all('div', {"class": "g"}):
            for x in a.find_all("cite", {"class":"iUh30"}):
                if(self.pageTitle in x.text):
                    return(textwrap.fill(a.text, 200))
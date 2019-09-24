import requests
import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl
import json


class InstaScrape:
    def __init__(self, path=None):
        self.ctx = ssl.create_default_context()
        self.ctx.check_hostname = False
        self.ctx.verify_mode = ssl.CERT_NONE
        self.path = path
        
    def getinfo(self, url, to_txt=False):
        assert url, "url invalid!"
        html = urllib.request.urlopen(url, context=self.ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        
        data = soup.find_all('meta', attrs={'property': 'og:description'})
        text = data[0].get('content').split()
        user = '%s %s %s' % (text[-3], text[-2], text[-1])
        followers = text[0]
        following = text[2]
        posts = text[4]
        print ('User:', user)
        print ('Followers:', followers)
        print ('Following:', following)
        print ('Posts:', posts)
        print ('---------------------------')
        if to_txt:
            
            name = url.split("/")[-1] if url.split("/")[-1] else url.split("/")[-2]
            file1 = open(self.path + name + ".txt","w")   
            file1.writelines(str(soup.html.encode('utf8')) )
            file1.close() 
            print (self.path + name + ".txt is saved!")
        else:
            return soup        

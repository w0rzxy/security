#!/usr/bin/python
import re
import urllib

def getHtml(url): #get html file
    page = urllib.urlopen(url)
    html= page.read()
    return html

def getImg(html): #use html's pic url get pic
    print type(html)
    reg = r'src="(.*\.jpg)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    x = 0
    for imgurl in imglist:
        urllib.urlretrieve(imgurl, '%s.jpg' % x) #save pic
        x += 1

if __name__ == "__main__":
    html = getHtml("http://www.nvshen.so/17902.html")
    print getImg(html)
    

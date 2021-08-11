import re
from bs4 import BeautifulSoup
from urllib import request
from urllib.request import urlopen

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}

req = request.Request('https://en.wikipedia.org/wiki/Cat', headers=headers)
html = urlopen(req)
bsObj = BeautifulSoup(html.read(), "html.parser")
# print(bsObj.get_text())
bs=bsObj.find_all(['ul','p','a','b'])
for i in bs:
    print(i.text)
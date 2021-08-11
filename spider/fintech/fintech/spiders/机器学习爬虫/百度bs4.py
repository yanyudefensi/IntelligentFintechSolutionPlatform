import re
from bs4 import BeautifulSoup
from urllib import request
from urllib.request import urlopen
from urllib.parse import quote

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}

req = request.Request('https://baike.baidu.com/item/'+quote('区块链', 'utf-8'), headers=headers)
html = urlopen(req)
bsObj = BeautifulSoup(html.read(), "html.parser")
print(bsObj.get_text())
# bs=bsObj.find_all(re.compile('a|b|p|ul'))
# for i in bs:
#     print(i.text)
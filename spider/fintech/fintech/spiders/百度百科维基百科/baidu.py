from urllib.parse import quote
from bs4 import BeautifulSoup
from urllib import request
from urllib.request import urlopen

def search(s):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}

    req = request.Request('https://baike.baidu.com/item/'+quote(s, 'utf-8'), headers=headers)
    html = urlopen(req)
    bsObj = BeautifulSoup(html.read(), "html.parser")
    bs=bsObj.find_all(name='div',attrs={'class':'para'})
    content=""
    for i in bs:
        content=f'{content}{i.text}'
    return content

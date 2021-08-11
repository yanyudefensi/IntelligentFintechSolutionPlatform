#encoding = utf-8
from bs4 import BeautifulSoup
from urllib import request
import re
from urllib.request import urlopen
def search(s):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    req = request.Request('https://en.wikipedia.org/wiki/'+s, headers=headers)
    html = urlopen(req)
    bsObj = BeautifulSoup(html.read(), "html.parser")
    bs=bsObj.find_all(['h1','h2','h3','ul','li','table','p']) #只要是符合数组内的内容就加入，不打乱文章顺序
    content=""
    pattern = re.compile('See also*')
    for i in bs:
        if (re.match(pattern,i.text)):
            break
        content=f'{content}{i.text}'
        # print(i.text)
    return content
# h1,h2,h3大标题,li、ul大框.p,a,b,table部分内容
# print(search('cat'))
# print(search('Internet of things'))
#'Big data','Artificial intelligence','Cloud computing','Internet of things'
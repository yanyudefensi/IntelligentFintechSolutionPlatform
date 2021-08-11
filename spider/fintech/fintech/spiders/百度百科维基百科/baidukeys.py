import lxml
from lxml import html
from urllib.parse import quote
import requests

def get_relevant_keys(key):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    req = requests.get('https://baike.baidu.com/item/'+quote(key, 'utf-8'), headers=headers)
    req.encoding = req.apparent_encoding
    htm = lxml.html.fromstring(req.text)
    html_data = htm.xpath('//*[@class="para"]/a')
    keys=[]
    for i in html_data:
        if (i.text!='\xa0'and i.text!=None):
            keys.append(i.text)
    return keys

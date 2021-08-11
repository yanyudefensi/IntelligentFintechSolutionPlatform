import lxml
from lxml import html
import re
import requests

def get_relevant_keys(key):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    req = requests.get('https://en.wikipedia.org/wiki/'+key, headers=headers)
    req.encoding = req.apparent_encoding
    htm = lxml.html.fromstring(req.text)
    html_data = htm.xpath('//a')
    keys=[]
    pattern1 = re.compile('Articles*')
    pattern2 = re.compile('\d+')
    for i in html_data:
        if (i.text!=None):
            if (re.match(pattern2, i.text)):
                continue
            if (re.match(pattern1, i.text)):
                break
            if (len(i.text)>5):
                keys.append(i.text)
            # print(i.get('href'))
#Webarchive template wayback links
    keys.pop(0)
    keys.pop(0)
    return keys
# print(get_relevant_keys('Big data'))

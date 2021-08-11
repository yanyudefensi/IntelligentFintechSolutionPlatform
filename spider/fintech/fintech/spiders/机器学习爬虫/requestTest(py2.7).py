import requests

r = requests.get('https://baike.baidu.com/item/%E5%8C%BA%E5%9D%97%E9%93%BE/13465666',allow_redirects=False)
print type(r)
print r.status_code
print r.encoding
# print r.text
print r.cookies

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post("http://httpbin.org/post", data=payload)
print r.text

r = requests.get('http://github.com', timeout=0.001)
print (r.text)


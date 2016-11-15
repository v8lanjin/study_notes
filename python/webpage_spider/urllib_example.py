# -*- coding: utf-8 -*
import urllib.request

# response = urllib.request.urlopen("http://www.baidu.com")
# response = response
# print(response.read().decode("utf-8"))

response = urllib.request.urlopen("http://placekitten.com/g/500/600")
# req = urllib.request.Request("http://placekitten.com/g/500/600")
# response = urllib.request.urlopen(req)
cat_img = response.read()

with open("cat_img.jpg", "wb") as f:
    f.write(cat_img)


print("url:" + response.geturl())
print("info:" + str(response.info()))
print("code:" + str(response.getcode()))


#--------------------------------------
print('-------------------------------')
print("example for youdao dict")
url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=dict2.top"

inputData = "Good morning "
inputData = inputData.strip()
# inputData = inputData.replace(' ', '+')
data = {}
data['type'] = 'AUTO'
data['i'] = inputData
data['doctype'] = 'json'
data['xmlVersion'] = "1.8"
data['keyfrom'] = 'fanyi.web'
data['ue'] = 'UTF-8'
data['action'] = 'FY_BY_CLICKBUTTON'
data['typoResult'] = 'true'

data = urllib.parse.urlencode(data).encode("utf-8")

response = urllib.request.urlopen(url, data)
res = response.read().decode('utf-8')
print(str(res))

import json
res = json.loads(res)
print(type(res))
print('src: ' + inputData + '    dest: ' + res['translateResult'][0][0]['tgt'])



header = {}
header['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'
# response = urllib.request.urlopen(url, data, header)
req = urllib.request.Request(url, data, header)
response = urllib.request.urlopen(req)
res = response.read().decode('utf-8')

res = json.loads(res)
print('src: ' + inputData + '    dest: ' + res['translateResult'][0][0]['tgt'])



req = urllib.request.Request(url, data)
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0')
response = urllib.request.urlopen(req)
res = response.read().decode('utf-8')

res = json.loads(res)
print('src: ' + inputData + '    dest: ' + res['translateResult'][0][0]['tgt'])



import time
# while True:
prompt = 'Please type a sentence:[q quit] '
# content = input(prompt)
content = "I Love Python"
content = content.strip()
# if content == 'q' or content == 'quit':
#     break

# content = content.replace(' ', '+')
data = {}
data['type'] = 'AUTO'
data['i'] = content
data['doctype'] = 'json'
data['xmlVersion'] = "1.8"
data['keyfrom'] = 'fanyi.web'
data['ue'] = 'UTF-8'
data['action'] = 'FY_BY_CLICKBUTTON'
data['typoResult'] = 'true'

data = urllib.parse.urlencode(data).encode("utf-8")

req = urllib.request.Request(url, data)
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0')
response = urllib.request.urlopen(req)
res = response.read().decode('utf-8')

res = json.loads(res)
print('src: ' + inputData + '    dest: ' + res['translateResult'][0][0]['tgt'])





# req = urllib.request.Request('http://whatismyip.org/')
# req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0')
# response = urllib.request.urlopen(req)

# html = response.read().decode('utf-8')
# print(html)
req = urllib.request.Request('http://www.baidu.com')

response = urllib.request.urlopen(req)

html = response.read().decode('utf-8')
print(html)



proxy_open = urllib.request.ProxyHandler({"http":"36.42.32.107:8080"})
opener = urllib.request.build_opener(proxy_open)
opener.add_headers = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0')]
urllib.request.install_opener(opener)

# response = opener.open('http://whatismyip.org')
# html = response.read().decode('utf-8')
# print(html)

req = urllib.request.Request('http://www.baidu.com')

response = urllib.request.urlopen(req)

html = response.read().decode('utf-8')
print(html)
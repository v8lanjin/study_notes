import urllib.request
import os

cnt = 1


def url_open(url):
	print("url is:" + url)
	req = urllib.request.Request(url)
	req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0')
	response = urllib.request.urlopen(req)
	html = response.read()
	return html

def getPageNum(url):
	html = url_open(url).decode('utf-8')
	# print(html)

	n_start = html.find("current-comment-page") + 23
	n_end   = html.find(']', n_start)

	return html[n_start:n_end]

def findImages(url):
	html = url_open(url).decode('utf-8')
	img_list = []
	n_start = 0
	n_end = 0
	while True:
		n_start = html.find("img src=", n_start)
		# print(n_start)
		if n_start == -1:
			break
		n_start += 9
		n_end   = html.find(".jpg", n_start, n_start + 100)
		if n_end == -1:
			continue
		n_end += 4
		# print('----------------------')
		# print(html[n_start:n_end])
		img_list.append(html[n_start:n_end])
	return img_list

	# print(html)


def saveImages(list):
	for each in list:
		print(each)
		global cnt
		pic = url_open(each)
		with open(str(cnt) + '.jpg', 'wb') as f:
			f.write(pic)
		cnt += 1




def download_pic(dir = 'pic', pages = 10):
	try:
		os.makedirs(dir)
	except FileExistsError:
		pass
	os.chdir(dir)

	url = ''
	page_num = int(getPageNum(url))
	print('current page num is :' + str(page_num))

	for i in range(pages):
		page_url = url + 'page-' + str(page_num - i) + '#comments'
		img_addrs = findImages(page_url)
		saveImages(img_addrs)

if __name__ == '__main__':
	download_pic('pic', 10)


#coding:utf-8
import json
import re
import requests
from bs4 import BeautifulSoup 

url = "https://share.zaixs.com"
#网站做了防爬，直接发请求会403，这里要在headers里加上User-Agent
headers = {'User-Agent': "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Mobile Safari/537.36",'Content-Type': "application/x-www-form-urlencoded"}
querystring = {"fid":"67"}
#payload = "page=3"

def gettid():
#访问征婚版块，获取该板块下的帖子id
	url1 = url + "/wap/community/list"
	tidlist = []
	#page是页数从1开始，每页40条信息,6时为200条信息
	for page in	range(1,6):
		payload = "page=" + str(page)
		response_id = requests.request("GET", url1, data=payload, headers=headers, params=querystring)
		soup_id = BeautifulSoup(response_id.text,'html.parser')
		#每页返回的帖子地址，循环输出tid保存到tidlist中		
		for link in soup_id.find_all('a'):
			url_id = link.get('href')
			if str(url_id)[:5] == '/wap/':
				tidlist.append(url_id)
	return tidlist
#print(gettid())

def getmessage():
	messagelist = []
	for j in gettid():
		#链接拼接后访问 
		url2 = url+ str(j)
		response = requests.request("GET", url2, headers=headers)
		soup = BeautifulSoup(response.text,'html.parser')
		#print(soup)		
		try:#根据标签取出个人信息,取不到时忽略
			message = soup.select('.typeoption')[0].text
			#print(message)
			message1 = url2 + str(message)
			messagelist.append(message1)
		except IndexError:
			pass
	return messagelist
#print(getmessage())
f = open('E:/git/changtang/message.txt','w')
for x in getmessage():
    y = str(x) + '\n'
    f.write(y)
f.close()

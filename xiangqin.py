#coding:utf-8
'''
Author:zhjfeng
Date:20190314
'''
import json
import re
import requests
from bs4 import BeautifulSoup 
url3 = "http://www.zaixs.com/forum.php?mod=forumdisplay&fid=67&orderby=lastpost&dateline=2592000&typeid=32&orderby=lastpost&filter=dateline&dateline=2592000&typeid=32&page=2"
url = "https://share.zaixs.com/wap/community/list"
#网站做了防爬，直接发请求会403，这里要在headers里加上User-Agent
headers = {'User-Agent': "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Mobile Safari/537.36"}
#page是页数从1开始，每页40条信息,6时为200条信息
#querystring = {"fid":"67","ordertype":"1","page":"3"}
querystring = {"fid":"67","page":"1"}
url1 = "https://share.zaixs.com/wap/thread/view-thread/tid/"

def gettid():
#访问征婚版块，获取该板块下的帖子id
	tidlist = []	
	response = requests.request("POST", url, headers=headers, params=querystring).json()
	#每页返回上限为40条，循环输出tid保存到tidlist中
	
	for i in range(0,40):		
		tid = response["data"]["list"]["thread"][i]["tid"]
		tidlist.append(tid)
	return response	
#print(gettid())

def getmessage():
	messagelist = []
	for j in gettid():
		#链接拼接后访问 
		url2 = url1+ str(j)
		response = requests.request("GET", url2, headers=headers)
		#html格式化
		soup = BeautifulSoup(response.text,'html.parser')
		#print(soup)
		#根据标签取出个人信息
		try:
			message = soup.select('.typeoption')[0].text
			#print(message)
			message1 = url2 + str(message)
			messagelist.append(message1)
		except IndexError:
			pass
	return messagelist
#print(getmessage())
#返回写入txt
f = open('D:/git/changtang/message.txt','w')
for x in getmessage():
    y = str(x) + '\n'
    f.write(y)
f.close()

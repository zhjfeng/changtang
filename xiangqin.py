#coding:utf-8
'''
author:zhjfeng
date:20190319
'''
import json
import re
import requests
from bs4 import BeautifulSoup

url = "https://share.zaixs.com/wap/community/list"
#page是页数从1开始，每页40条信息
querystring = {"fid":"67","ordertype":"1","page":"1"}
#网站做了防爬，直接发请求会403，这里要在headers里加上User-Agent
headers = {'User-Agent': "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Mobile Safari/537.36"}
url1 = "https://share.zaixs.com/wap/thread/view-thread/tid/"

def gettid():
#访问征婚版块，获取该板块下的帖子id
	response = requests.request("POST", url, headers=headers, params=querystring).json()
	#print(response)
	tidlist = []
	#每页返回上限为40条，循环输出tid保存到tidlist中
	for i in range(0,40):		
		tid = response["data"]["list"]["thread"][i]["tid"]
		tidlist.append(tid)
	return tidlist	
#print(gettid())
#
messagelist = []
def getmessage():
	for j in gettid():
		#链接拼接后访问 
		url2 = url1+ str(j)
		response = requests.request("GET", url2, headers=headers)
		#html格式化
		soup = BeautifulSoup(response.text,'html.parser')
		#print(soup)
		#根据标签取出个人信息
		message = soup.select('.typeoption')[0].text
		#print(message)
		message1 = url2 + str(message)
		messagelist.append(message1)
	return messagelist
#print(getmessage())
#返回写入txt
f = open('E:/git/changtang/message.txt','w')
for x in getmessage():
    y = str(x) + '\n'
    f.write(y)
f.close()
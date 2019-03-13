#coding:utf-8
'''
nametest，是对随机生成的昵称进行合法性校验的脚本，可以单张表先校验，再组合校验
author:zhjfeng
date:20170601
'''
import os
import xlrd
import subprocess

#更新date目录
subprocess.Popen(r'TortoiseProc.exe /command:update /path:"E:\RPG001\doc\trunk\策划\data" /closeonend:0')

#输入需要测试的name表
excel = xlrd.open_workbook('E:/RPG001/doc/trunk/策划/data/name1.xlsx')
table = excel.sheets()[0]

#获取姓的列表
name1 = table.col_values(1)

#删除前3个无效数据，表头
name1 = name1[3:]

#删除可能出现的空字符串情况
while '' in name1:
    name1.remove('')
name2 = table.col_values(2)
name2 = name2[3:]
while '' in name2:
    name2.remove('')
   
name3 = name1 + name2

#获取名的列表
name4 = table.col_values(3)
name4 = name4[3:]
while '' in name4:
    name4.remove('')
    
name5 = table.col_values(4)
name5 = name5[3:]
while '' in name5:
    name5.remove('')

name6 = name4 + name5

wordexcel = xlrd.open_workbook('E:/RPG001/doc/trunk/策划/data/word.xlsx')
table = wordexcel.sheets()[0]
words = table.col_values(1)
words = words[3:]


for i in name1:
    for j in name6:
        playername = i + j

        for word in words:
            if word in playername:
                print('{0}&{1} 出现了屏蔽字：{2}'.format(i, j, word))
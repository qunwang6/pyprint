#!/usr/bin/env python
# -*- coding: utf-8 -*-
#正则替换，文本断点换行。
#准备好r.txt文件，将要索引的单词输入到r.txt文本文件中，每行一个单词,每行为一页.
#每页含有两个以上的词，每行的单词间用'|'分开：ab|ac|ad
#python pyprint.py,结果写入renew.txt文件
#for mac osx
import re

f = open('renew.txt','w')
rt = open('r.txt')
rp = open('re.txt')
rtw = rt.readline()
count = 1
line = len(open('re.txt').readlines())
while (count <= line):
	
	rd = rp.readline()
	rw = rd.strip('\n')
	#rpw = '|%s|' % rw
	
	text=re.sub(r'\|(%s)\|' % rw,'|%s\n' % rw,rtw)
	#判断re.txt里的单词是否匹配r.txt里的单词。
	#s='|abelmosk|Abenaki|Aberdeen Angus|'
	#用re.match出错
	if re.search(r'\|(%s)\|' % rw,rtw):
		print 'match'
	else:
		print rw+' not match'
	rtw = text
	count = count + 1
#print rtw
	



	

	




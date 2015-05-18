#!/usr/bin/env python
# -*- coding: utf-8 -*-
#准备好r.txt文件，将要索引的单词输入到r.txt文本文件中，每行一个单词,每行为一页.
#每页含有两个以上的词，每行的单词间用'|'分开：ab|ac|ad
#python pyprint.py,结果写入index.txt文件
#for Mdx
f = open('index.txt','w')
r = open('r.txt')

count = 1
line = len(open('r.txt').readlines())


hw = '%s\n<link href="DefaultStyle.css" rel="stylesheet" type="text/css"/>' 
word = '<span class="word"><a class="swd" href="x-dictionary:r:'
a = '">'
wd = '%s</a></span>'
left = '<span class="left"><a class="slf" href="x-dictionary:r:'
lb = 'previous</a></span>'
right = '<span class="right"><a class="srt" href="x-dictionary:r:'
rb = 'next</a></span>'
img1 = '<img class="img" src="images/'
img2 = '.jpg"/>'
while (count <= line):
	rd = r.readline()
	rw = rd.strip('\n')
	for i in rw.split('|'):
		print >> f,hw % (i.strip('\n')) + word + str(count) + a +wd % (i.strip('\n')),left + str(count-1) + a +lb,right + str(count+1) + a + rb + img1 + str(count) + img2  
		

	count = count + 1

f.close()

	
	







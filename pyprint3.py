#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pyprint.py
#准备好r.txt文件，将要索引的单词输入到r.txt文本文件中，每行一个单词.
#python pyprint.py,结果写入index.txt文件
f = open('index.txt','w')
r = open('r.txt')
#读取r.txt文件行数
line = len(open('r.txt').readlines())

print >> f,'<?xml version="1.0" encoding="UTF-8"?>\n<d:dictionary xmlns="http://www.w3.org/1999/xhtml" xmlns:d="http://www.apple.com/DTDs/DictionaryService-1.0.rng">'
count = 1
hw = '<d:entry id="%d" d:title="%d">\n    <d:index d:value="%s"/>\n<html><body><link href="DefaultStyle.css" rel="stylesheet" type="text/css"/>' 
word = '<span class="word"><a class="swd" href="x-dictionary:r:'
a = '">'
wd = 'word</a></span>'
left = '<span class="left"><a class="slf" href="x-dictionary:r:'
lb = 'previous</a></span>'
right = '<span class="right"><a class="srt" href="x-dictionary:r:'
rb = 'next</a></span>'
img1 = '<img class="img" src="images/'
img2 = '.jpg/>'
ew = '</body></html>\n</d:entry>'
while (count <= line):
#逐行读取r.txt并去掉每行的换行符'\n'
	rw = r.readline()
	rw = rw.strip('\n')
	print >> f,hw % (count+1,count+1,rw) + word + str(count+1) + a +wd,left + str(count) + a +lb,right + str(count+2) + a + rb + img1 + str(count+1) + img2 + ew 
	count = count + 1
print >> f,'</d:dictionary>'
f.close()
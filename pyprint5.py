#!/usr/bin/env python
# -*- coding: utf-8 -*-
f = open('index.txt','w')
r = open('r.txt')

column = str.split('|')
count = 1
line = len(open('r.txt').readlines())

print >> f,'<?xml version="1.0" encoding="UTF-8"?>\n<d:dictionary xmlns="http://www.w3.org/1999/xhtml" xmlns:d="http://www.apple.com/DTDs/DictionaryService-1.0.rng">'

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
	rw = r.readline()
	rw = rw.strip('\n')
	
	if rw.split('|'):
		for i in rw.split('|'):
			print >> f,hw % (count,count,i.strip('\n')) + word + str(count) + a +wd,left + str(count-1) + a +lb,right + str(count+1) + a + rb + img1 + str(count) + img2 + ew 
	elif not len(rw.strip()):
		continue
	else:
		print 'error'

	count = count + 1
print >> f,'</d:dictionary>'
f.close()

	
	







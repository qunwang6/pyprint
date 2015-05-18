#!/usr/bin/env python
# -*- coding: utf-8 -*-
## pyprint.py
f = open('index.txt','w')
print >> f,'<?xml version="1.0" encoding="UTF-8"?>\n<d:dictionary xmlns="http://www.w3.org/1999/xhtml" xmlns:d="http://www.apple.com/DTDs/DictionaryService-1.0.rng">'
count = 1
hw = '<d:entry id="%d" d:title="%d">\n    <d:index d:value="word"/>\n<html><body><link href="DefaultStyle.css" rel="stylesheet" type="text/css"/>' 
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

while (count < 90):
	print >> f,hw % (count+1,count+1) + word + str(count+1) + a +wd,left + str(count) + a +lb,right + str(count+2) + a + rb + img1 + str(count+1) + img2 + ew
	count = count + 1	
print >> f,'</d:dictionary>'
f.close()
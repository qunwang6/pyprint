#!/usr/bin/python
count = 1
word = '<span class="word"><a class="swd" href="x-dictionary:r:'
a = '">'
wd = 'word</a></span>'
left = '<span class="left"><a class="slf" href="x-dictionary:r:'
lb = 'leftpage</a></span>'
right = '<span class="right"><a class="srt" href="x-dictionary:r:'
rb = 'right</a></span>'
while (count < 90):
	print word + str(count+1) + a +wd,left + str(count) + a +lb,right + str(count+2) + a + rb
	count = count + 1
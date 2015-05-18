#!/usr/bin/env python
# -*- coding: utf-8 -*-
#准备好r.txt文件，将要索引的单词输入到r.txt文本文件中，每行一个单词,每行为一页.
#每页含有两个以上的词，每行的单词间用'|'分开,左右两列单词用'/'分开：ab|ac|ad/ba|bc|bd
#python pyprint.py,结果写入index.txt文件
#for mdx

f = open('index.txt','w')
r = open('r.txt')
count = 1

text = '<link href="DefaultStyle.css" rel="stylesheet" type="text/css"/>\n<span class="left">☜</span><span class="word1">%s</span><span class="right">☞</span><span class="word2">%s</span><a class="pre" href="entry://%s">上一页</a><a class="nex" href="entry://%s">下一页</a><img class="img" src="images/%s.jpg"/>\n'

#第一行空
f.write('\n</>\n')

#汉字/拼音/字母索引
line = len(open('r.txt').readlines())
while (count <= line):
	n = str(count)
	s = n.zfill(6) #自动补0
	n1 = str(count-1)
	s1 = n1.zfill(6)
	n2 = str(count+1)
	s2 = n2.zfill(6)
	
	rd = r.readline()
	rw = rd.strip('\n')
	for i in rw.split('/'):
		rw2 = i.strip('\n')
		
		for i in rw2.split('|'):
			f.write('%s\n' % i.strip('\n'))
			f.write('@@@LINK=%s\n' % count)
			f.write('</>\n')

		rw3 = rw.split('/')
		#left
		rw4 = rw3[0].split('|')
		#right
		rw5 = rw3[1].split('|')
	#词头前序号
		for j,k in enumerate(rw4):
			rw6 = str(j+1)+str(k)
	 		print rw6
	 		#f.write(text % (rw6,rw3[1],count-1,count+1,count))
	
						
	f.write('%s\n' % count)	
	#f.write(text % (rw3[0],rw3[1],count-1,count+1,count))
	#f.write(text % (rw6,rw3[1],count-1,count+1,count))
	f.write('</>\n')
	count = count + 1
f.close()
	

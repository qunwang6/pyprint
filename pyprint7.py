#!/usr/bin/env python
# -*- coding: utf-8 -*-
#准备好r.txt文件，将要索引的单词输入到r.txt文本文件中，每行一个单词,每行为一页.
#每页含有两个以上的词，每行的单词间用'|'分开：ab|ac|ad
#python pyprint.py,结果写入index.txt文件
#for mac osx

f = open('index.xml','w')
r = open('r.txt')
count = 1
text = '<html><body><link href="DefaultStyle.css" rel="stylesheet" type="text/css"/><div><a class="play" href="" onclick="document.getElementById(\'index\').style.display = \'block\'; return false;"></a><div class="index" id="index"><a class="hide" href="" onclick="document.getElementById(\'index\').style.display = \'none\'; return false;"></a><a class="left" href="x-dictionary:r:%s">☜</a><a class="A" href="A">A</a><a class="B" href="B">B</a><a class="C" href="C">C</a><a class="D" href="D">D</a><a class="E" href="E">E</a><a class="F" href="F">F</a><a class="G" href="G">G</a><a class="H" href="H">H</a><a class="I" href="I">I</a><a class="J" href="J">J</a><a class="K" href="K">K</a><a class="L" href="L">L</a><a class="M" href="M">M</a><a class="N" href="N">N</a><a class="O" href="O">O</a><a class="P" href="P">P</a><a class="Q" href="Q">Q</a><a class="R" href="R">R</a><a class="S" href="S">S</a><a class="T" href="T">T</a><a class="U" href="U">U</a><a class="V" href="V">V</a><a class="W" href="W">W</a><a class="X" href="X">X</a><a class="Y" href="Y">Y</a><a class="Z" href="Z">Z</a><a class="right" href="x-dictionary:r:%s">☞</a></div></div><img class="img" src="images/%s.jpg"/>\n</body></html>\n</d:entry>\n'
line = len(open('r.txt').readlines())
f.write('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<d:dictionary xmlns="http://www.w3.org/1999/xhtml" xmlns:d="http://www.apple.com/DTDs/DictionaryService-1.0.rng">\n')

while (count <= line):
	n = str(count)
	s = n.zfill(6) #自动补0
	n1 = str(count-1)
	s1 = n1.zfill(6)
	n2 = str(count+1)
	s2 = n2.zfill(6)
	f.write('<d:entry id="%s" d:title="%s">\n' % (s,s))
	rd = r.readline()
	rw = rd.strip('\n')
	for i in rw.split('|'):
		f.write('    <d:index d:value="%s"/>\n' % i.strip('\n'))
	f.write('    <d:index d:value="%s"/>\n' % count)
	f.write(text % (s1,s2,s))
	count = count + 1
#目录索引
ml = 1
while (ml <= 75):
	n = str(ml)
	s = n.zfill(5) #自动补0
	n1 = str(ml-1)
	s1 = n1.zfill(5)
	n2 = str(ml+1)
	s2 = n2.zfill(5)
	p = '!' + s
	p1 = '!' + s1
	p2 = '!' + s2	
	f.write('<d:entry id="%s" d:title="%s">\n' % (p,p))
	f.write('    <d:index d:value="%s"/>\n' % p)
	f.write(text % (p1,p2,p))
	ml = ml + 1
f.write('</d:dictionary>\n')
f.close()

#css
c = open('dic.css','w')
c.write('.hide,.A,.B,.C,.D,.E,.F,.G,.H,.I,.J,.K,.L,.M,.N,.O,.P,.Q,.R,.S,.T,.U,.V,.W,.X,.Y,.Z,.left,.right{display: block;text-align: center;text-decoration:none;color:#5484C8;background: #DCDCDC; color: #fff;border-radius:8px;margin:1px;}\na:hover {color: #FF9900;}\n .play,.index{float:right;position:fixed;right:15px;height:100%;line-height:20px;overflow:scroll;margin-top:20%;}\n.left,.right{display: block;font-size:24px;text-decoration:none;line-height:20px;}\n.img{width:100%;}\n .play{text-decoration:none;}')
c.close()
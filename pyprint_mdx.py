#!/usr/bin/env python
# -*- coding: utf-8 -*-
#准备好r.txt文件，将要索引的单词输入到r.txt文本文件中，每行一个单词,每行为一页.
#每页含有两个以上的词，每行的单词间用'|'分开：ab|ac|ad
#python pyprint.py,结果写入index.txt文件
#for mdx

f = open('index.txt','w')
r = open('r.txt')
count = 1
#entry里参数自行修改
text = '<link href="DefaultStyle.css" rel="stylesheet" type="text/css"/><div><a class="play" href="" onclick="document.getElementById(\'index\').style.display = \'block\'; return false;"></a><div class="index" id="index"><a class="hide" href="" onclick="document.getElementById(\'index\').style.display = \'none\'; return false;"></a><a class="left" href="entry://%s">☜</a><a class="A" href="entry://!00001">A</a><a class="B" href="entry://!00001">B</a><a class="C" href="entry://!00003">C</a><a class="D" href="entry://!00005">D</a><a class="E" href="entry://!00007">E</a><a class="F" href="entry://!00008">F</a><a class="G" href="entry://!00009">G</a><a class="H" href="entry://!00011">H</a><a class="I" href="I">I</a><a class="J" href="entry://!00012">J</a><a class="K" href="entry://!00016">K</a><a class="L" href="entry://!00017">L</a><a class="M" href="entry://!00018">M</a><a class="N" href="entry://!00020">N</a><a class="O" href="entry://!00020">O</a><a class="P" href="entry://!00020">P</a><a class="Q" href="entry://!00021">Q</a><a class="R" href="entry://!00023">R</a><a class="S" href="entry://!00024">S</a><a class="T" href="entry://!00027">T</a><a class="U" href="U">U</a><a class="V" href="V">V</a><a class="W" href="entry://!00029">W</a><a class="X" href="entry://!00030">X</a><a class="Y" href="entry://!00032">Y</a><a class="Z" href="entry://!00035">Z</a><a class="right" href="entry://%s">☞</a></div></div><img class="img" src="images/%s.jpg"/>\n'
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
	for i in rw.split('|'):
		f.write('%s\n' % i.strip('\n'))
		f.write('@@@LINK=%s\n' % count)
		f.write('</>\n')
	f.write('%s\n' % count)
	f.write(text % (s1,s2,s))
	f.write('</>\n')
	count = count + 1
	
#图书目录索引
ml = 1
#ml参数要改，等于读秀图书目录最后一页
while (ml <= 35):
	n = str(ml)
	s = n.zfill(5) #自动补0
	n1 = str(ml-1)
	s1 = n1.zfill(5)
	n2 = str(ml+1)
	s2 = n2.zfill(5)
	p = '!' + s
	p1 = '!' + s1
	p2 = '!' + s2	
	f.write('%s\n' % p)
	f.write(text % (p1,p2,p))
	f.write('</>\n')
	ml = ml + 1
f.close()

#css
c = open('dic.css','w')
c.write('.hide,.A,.B,.C,.D,.E,.F,.G,.H,.I,.J,.K,.L,.M,.N,.O,.P,.Q,.R,.S,.T,.U,.V,.W,.X,.Y,.Z,.left,.right{display: block;text-align: center;text-decoration:none;color:#5484C8;background: #DCDCDC; color: #fff;font-weight:bold;border-radius:5px;}\na:hover {color: #FF9900;}\n.index{float:right;position:fixed;right:15px;height:100%;line-height:20px;overflow:scroll;margin-top:20%;}\n.left,.right{display: block;font-size:24px;text-decoration:none;line-height:20px;}\n.img{width:100%;}\n.play{text-decoration:none;}')
c.close()
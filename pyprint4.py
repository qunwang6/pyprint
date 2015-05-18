#!/usr/bin/env python
# -*- coding: utf-8 -*-
#遇到分隔符'|'
f = open('index.txt','w')
r = open('r.txt')
for line in r.readlines():
	if not line.strip():
		continue
import linecache
print linecache.getline('r.txt',3)




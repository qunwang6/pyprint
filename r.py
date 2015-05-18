#!/usr/bin/env python
# -*- coding: utf-8 -*-
f = open('r.txt','w')
line = 1162
while line<=1189:
	print >>f,'00'+str(line)
	line = line +1
f.close()
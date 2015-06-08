#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
f = open('write.txt','w')
r = open('test.txt')
strs = r.readlines()
for line in strs:
	#lines = line.strip('\n')
	word = re.sub(r"[</>]","",line)
	print word
	f.write(word)



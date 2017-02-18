#!/usr/bin/env python

from operator import itemgetter
import sys

current_k = None
current_v = 0
k = None

for line in sys.stdin:
	line = line.strip() # in case there is any space
	k, v = line.split(',', 1)

	try:
		v = float(v)
	except ValueError:
		continue

	if current_k == k:
		current_v += v
	else:
		if current_k:
			print '%s, %f' %(current_k, current_v)
		current_v = v
		current_k = k

if current_k == k:
    print '%s, %f' %(current_k, current_v)

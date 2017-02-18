#!/usr/bin/env python

import sys
import numpy as np

def isInt(value):
	try:
		int(value)
		return True
	except ValueError:
		return False

# input comes from STDIN (standard input)
for line in sys.stdin:
	line = line.strip()
	kv = line.split()
	k = kv[0].split("-")[0]
	count = 0
	sum = []
	kv.pop(0)
	for v in kv:
		if isInt(v.strip()):
			if (int(v.strip()) != -9999):
				a = int(v.strip())
				sum.append(a)
	print "%s, %f" %(str(k), np.mean(sum))

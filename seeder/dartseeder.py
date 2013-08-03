#!/usr/bin/env python

# 16 ^ 8 = 4294967296 permutations
#
# 0x00000001      
# 0x00000002
# etc......

import hashlib

ceil = 4294967296
cnt = 0

while( cnt < ceil ):
	md5 = hashlib.md5()
	value = "%0.8X" % cnt
	md5.update( value.encode('utf-8') )
	hd = md5.hexdigest()
	
	record = value + "," + hd
	
	print( record )
	cnt += 1
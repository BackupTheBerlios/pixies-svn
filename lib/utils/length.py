
"""
$Id$
$URL$

Copyright (C) 2004 Matteo Merli <matteo.merli@gmail.com>

This code is licenced under the GPL. See LICENSE file.
"""

from reportlab.lib.units import *
## 1em is fixed to 11pt
em = 11
	
def toLength(s, default=em):
	'''convert a string to  a length'''
	try:
		if s[-2:]=='cm': return float(s[:-2])*cm
		if s[-2:]=='in': return float(s[:-2])*inch
		if s[-2:]=='pt': return float(s[:-2])
		if s[-1:]=='i': return float(s[:-1])*inch
		if s[-2:]=='mm': return float(s[:-2])*mm
		if s[-4:]=='pica': return float(s[:-4])*pica
		if s[-2:]=='pc': return float(s[:-2])*pica
		if s[-2:]=='em': return float(s[:-2]) * default
		if s[-1:]=='%': return float(s[:-1]) * default / 100
		return float(s)
	except:
		## check for the form: margin-left="1.2in - -1.5pc"
		try:
			print "WARNING: TESTING NEGATIVE VALUES: ",  s 
			l1, l2 = s.split(' - ')
			l1 = toLength( l1 )
			l2 = toLength( l2 )
			print "L1 = %f - L2  = %f ----- L = %f" % ( l1, l2, float(l1-l2) )
			return float( l1 - l2 )
		except:
			raise
		raise ValueError, "Can't convert '%s' to length" % s
		

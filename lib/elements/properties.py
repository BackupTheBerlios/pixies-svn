
"""
$Id$
$URL$

Copyright (C) 2004 Matteo Merli <matteo.merli@gmail.com>
"""

import sys

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
		

def Warning( feat ):
	sys.stderr.write( "WARNING: '%s' not supported" % feat )

class Properties:
	properties = {}
		
	def common_borders( self, attrs ):
		if 'background-color' in attrs :
			self.style.backColor = toColor( attrs['background-color'].encode('utf-8') )
		if 'background-image' in attrs :
			Warning('background-image')
		if 'background-repeat' in attrs :
			Warning('background-repeat')
		if 'background-position-horizontal' in attrs:
			Warning('background-position-horizontal')
		if 'background-position-vertical' in attrs:
			Warning('background-position-vertical')
			
		if 'padding-left' in attrs:
			d['padding-left'] = toLength( attrs['padding-left'] )
		if 'padding-right' in attrs:
			d['padding-right'] = toLength( attrs['padding-right'] )
		if 'padding-top' in attrs:
			d['padding-top'] = toLength( attrs['padding-top'] )
		if 'padding-bottom' in attrs:
			d['padding-bottom'] = toLength( attrs['padding-bottom'] )
	
	def common_margins(self, attrs ):
		p = self.properties
		if 'margin-left' in attrs:
			p['margin-left'] = toLength( attrs['margin-left'] )
		if 'margin-right' in attrs:
			p['margin-right'] = toLength( attrs['margin-right'] )
		if 'margin-top' in attrs:
			p['margin-top'] = toLength( attrs['margin-top'] )
		if 'margin-bottom' in attrs:
			p['margin-bottom'] = toLength( attrs['margin-bottom'] )
		if 'space-before.optimum' in attrs:
			p['space-before'] = toLength( attrs['space-before.optimum'] )
		if 'space-after.optimum' in attrs:
			p['space-after'] = toLength( attrs['space-after.optimum'] )	
			
	def common_fonts(self, attrs ):
		p = self.properties
		
		if 'font-family' in attrs:
			p['font-family'] = 
		
		
		
		
		
		
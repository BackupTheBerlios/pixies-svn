
"""
$Id$
$URL$

Copyright (C) 2004 Matteo Merli <matteo.merli@gmail.com>
"""

import sys
from lib.utils import *


class Properties:
	properties = {}
		
	def common_borders( self, attrs ):
		if 'background-color' in attrs :
			self.style.backColor = toColor( attrs['background-color'].encode('utf-8') )
		if 'background-image' in attrs :
			NotImplemented('background-image')
		if 'background-repeat' in attrs :
			NotImplemented('background-repeat')
		if 'background-position-horizontal' in attrs:
			NotImplemented('background-position-horizontal')
		if 'background-position-vertical' in attrs:
			NotImplemented('background-position-vertical')
			
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
			
	def common_fonts( self, attrs ):
		p = self.properties
		
		p['font'] = PsFont( attrs )
		if 'font-size' in attrs:
			p['font-size'] = toLength( attrs['font-size'] )
		if 'font-stretch' in attrs:
			NotImplemented('font-stretch')
		if 'font-size-adjust' in attrs:
			NotImplemented('font-size-adjust')
		if 'font-size-adjust' in attrs:
			NotImplemented('font-size-adjust')
		if 'font-variant' in attrs:
			NotImplemented('font-variant')
			
	def common_align( self, attrs ):
		p = self.properties
		
		if 'alignment-adjust' in attrs:
			NotImplemented('alignment-adjust')
			
	def common_text( self, attrs ):
		p = self.properties
		
		if 'line-height' in attrs:
			p['line-height'] = toLength( attrs['line-height'] )
		if 'text-align' in attrs:
			p['text-align'] = Alignement( attrs['text-align'] )
		if 'color' in attrs:
			p['color'] = toColor( attrs['color'] )
			
		
		
		
		
		
		

"""
$Id$
$URL$

Copyright (C) 2004 Matteo Merli <matteo.merli@gmail.com>

This code is licenced under the GPL. See LICENSE file.
"""

from reportlab.lib.enums import *
from reportlab.lib.colors import Color

class Style:
	
	fontName = 'Helvetica'
	fontSize = 10
	leading = 12
	leftIndent = 0
	rightIndent = 0
	firstLineIndent = 0
	alignment = TA_LEFT
	spaceBefore = 0
	spaceAfter = 0
	bulletFontName = 'Times-Roman'
	bulletFontSize = 10
	bulletIndent = 0
	textColor = Color(0,0,0)
	backColor = None
	
	def __init__( self, p ):
		
		if 'font' in p: self.fontName = p['font']
		if 'font-size' in p: self.fontSize = p['font-size']
		if 'line-height' in p: self.leading = p['line-height']
		# indents
		if 'text-align' in p: self.alignment = p['text-align']
		if 'space-before' in p: self.spaceBefore = p['space-before']
		if 'space-after' in p: self.spaceAfter = p['space-after']
		if 'color' in p: self.textColor = p['color']
		if 'background-color' in p: self.backColor = p['background-color']
			
		# Check for line-height consintency..
		if self.leading <= self.fontSize:
			self.leading = self.fontSize + 2
		


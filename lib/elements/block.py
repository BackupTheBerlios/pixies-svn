
"""
$Id$
$URL$

Copyright (C) 2004 Matteo Merli <matteo.merli@gmail.com>

This code is licenced under the GPL. See LICENSE file.
"""

from reportlab.platypus.paragraph import *
from properties import *
from lib.utils import *

class Block( Paragraph, Properties ):
	
	def __init__(self, text, attrs, bulletText=None, frags=None ):
		
		# The class is instancied from a split()
		if frags: 
			Paragraph.__init__ (self, text, attrs, bulletText=bulletText, frags=frags )
			return 
			
		Properties.__init__(self)
		text = text.encode('latin1', 'ignore')
		
		###REMOVE ME
		if len(text) < 5: 
			return
		
		self.common_fonts( attrs )
		self.common_margins( attrs )
		self.common_borders( attrs )
		self.common_text( attrs )
		
		self.style = Style( self.properties )
		## print self.properties
		
		self.caseSensitive = 1
		self._setup( text, self.style, None, None, cleanBlockQuotedText)

			
			
			

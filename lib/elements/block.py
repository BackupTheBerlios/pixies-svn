
"""
$Id$
$URL$

Copyright (C) 2004 Matteo Merli <matteo.merli@gmail.com>
"""

from reportlab.platypus.paragraph import *
from properties import *
from lib.utils import *

class Block( Paragraph, Properties ):
	
	"""
	<fo:block font-size="18pt"
            font-family="sans-serif"
            line-height="24pt"
            space-after.optimum="15pt"
            background-color="blue"
            color="white"
            text-align="center"
            padding-top="3pt"
            font-variant="small-caps">
	"""
	def __init__(self, text, attrs ):
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

			
			
			

"""
$Id$
$URL$

Copyright (C) 2004 Matteo Merli <matteo.merli@gmail.com>

This code is licenced under the GPL. See LICENSE file.
"""


from reportlab.platypus.flowables import Image
from properties import *
# from pixies.utils import *

class ExternalGraphic( Image, Properties ):
	""" 
	Map to the fo:external-graphic XSL-FO element.
	Properties to be supported are:
		- "scaling" -- § 7.14.10 on page 250
		- "scaling-method" -- § 7.14.11 on page 251
		- "src" -- § 7.28.7 on page 335
		- "text-align" -- § 7.15.9 on page 258
		- "width" -- § 7.14.12 on page 251
	"""

	def __init__( self, attrs ):
		
		# PIL is required to draw images
		try:
			import PIL
		except ImportError:
			Error("""
PIL (Python Imaging Library) is required to use images in 
your documents. 
You should download and install it. 
http://www.pythonware.com/products/pil/
				""")
		
		Properties.__init__(self)
		self.graphic( attrs )
		
		if self.properties['src']:
			self.filename = self.properties['src']
		else:
			Error('No source defined for external-graphic element.')
		
		Image.__init__( self, self.filename )

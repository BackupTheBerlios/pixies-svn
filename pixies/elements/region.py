
"""
$Id$
$URL$

Copyright (C) 2004 Matteo Merli <matteo.merli@gmail.com>

This code is licenced under the GPL. See LICENSE file.
"""

from pixies.utils import *
from properties import *

class Region( Properties ):
	
	def __init__( self, attrs ):
		Properties.__init__(self)
		self.common_borders( attrs )
		self.common_margins( attrs )
		
		p = self.properties
		
		self.marginTop = get( p, 'margin-top')
		self.marginBottom = get( p, 'margin-bottom')
		self.marginLeft = get( p, 'margin-left')
		self.marginRight = get( p, 'margin-right')
		self.paddingTop = get( p, 'padding-top')
		self.paddingBottom = get( p, 'padding-bottom')
		self.paddingLeft = get( p, 'padding-left')
		self.paddingRight = get( p, 'padding-right')
		self.extent = get( p, 'extent' )
		
	def __str__(self):
		""" Testing method """
		return """
		REGION
		self.marginTop: %f
		self.marginBottom: %f
		self.marginLeft: %f
		self.marginRight: %f
		self.paddingTop: %f
		self.paddingBottom: %f
		self.paddingLeft: %f
		self.paddingRight: %f
		self.extent: %f 
		""" % ( self.marginTop, self.marginBottom, self.marginLeft,
						    self.marginRight, self.paddingTop, self.paddingBottom,
							self.paddingLeft, self.paddingRight, self.extent )


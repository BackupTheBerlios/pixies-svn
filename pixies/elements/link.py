
"""
$Id$
$URL$

Copyright (C) 2004 Matteo Merli <matteo.merli@gmail.com>

This code is licenced under the GPL. See LICENSE file.
"""

from properties import *

class Link(Properties):
	
	def __init__( self, node ):
		Properties.__init__(self)
		self.node = node
		
	def getText( self ):
		s = ''
		for n in self.node.childNodes:
			if n.nodeType == n.TEXT_NODE:
				s  += n.data
			
		return s

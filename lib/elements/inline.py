
"""
$Id$
$URL$

Copyright (C) 2004 Matteo Merli <matteo.merli@gmail.com>
"""

from lib.utils import *
from properties import *

class Inline( Properties ):
	
	
	def __init__(self, node):
		Properties.__init__(self)
		self.node = node
		self.attrs = Attrs( node )
		
		self.common_fonts( self.attrs )
		self.common_borders( self.attrs )
		self.common_align( self.attrs )
		self.common_text( self.attrs )
		
		self.prefix = ''
		self.suffix = ''
		
		p = self.properties
		
		font = {}
		if 'font-family' in self.attrs:
			font['font-family'] = self.attrs['font-family']
		if 'font-size' in p:
			font['font-size'] = p['font-size']
		if 'color' in p:
			font['color'] = p['color']
		if 'background-color' in p:
			font['bgcolor'] = p['background-color']
			
		
		if self.attrs.get('font-weight') == 'bold':
			self.add('b')
		if self.attrs.get('font-style') in ('italic', 'oblique'):
			self.add('i')
			
		print "\nAdded Inline Formatting:"
		print self.prefix + self.getText() + self.suffix + "\n\n"
		

	def getText(self):
		s = ''
		for n in self.node.childNodes:
			if n.nodeType == n.TEXT_NODE:
				s += n.data
			elif n.nodeName == 'fo:inline':
				i = Inline( n )
				s += i.getText()
			elif n.nodeName == 'fo:page-number':
				s += "#1#"

		return unicode( s )
			
			
	def add( self, key, attrs={} ):
		self.prefix += '<%s' % key
		for k,v in attrs:
			self.prefix += ' %s="%s"' % (k,v)
		self.prefix += '>'
		
		self.suffix = '</%s>%s' % ( key, self.suffix )
			
			
			
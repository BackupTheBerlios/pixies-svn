
"""
$Id$
$URL$

Copyright (C) 2004 Matteo Merli <matteo.merli@gmail.com>

This code is licenced under the GPL. See LICENSE file.
"""

from pixies.utils import *
from properties import *
from link import *

class Inline( Properties ):
	""" This represent the &lt;fo:inline&gt; element. """
	
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
			font['face'] = self.attrs['font-family']
		if 'font-size' in p:
			font['font-size'] = p['font-size']
		if 'color' in p:
			font['color'] = p['color']
		if 'background-color' in p:
			font['bgcolor'] = p['background-color']
			
		if font: 
			self._add( 'font', font )	
			print font, self.getText()
			
		if self.attrs.get('font-weight') == 'bold':
			self._add('b')
		if self.attrs.get('font-style') in ('italic', 'oblique'):
			self._add('i')
		
		
		

	def getText(self):
		""" Return the processed text of the Inline object, 
			resolving all the nested tags. """
		self.text = ''
		for n in self.node.childNodes:
			if n.nodeType == n.TEXT_NODE:
				self.text += n.data
			elif n.nodeName == 'fo:inline':
				i = Inline( n )
				self.text += i.getText()
			elif n.nodeName == 'fo:basic-link':
				l = Link( n )
				self.text += l.getText()
			elif n.nodeName == 'fo:page-number':
				self.text += "#1#"

		## print "\nAdded Inline Formatting:"
		self.text = self.prefix + escape_tags(self.text) + self.suffix 
		print "###", self.text
		return unicode( trim_spaces( self.text ) )			
			
	def _add( self, key, attrs={} ):
		""" Add a xml-like tag to pass inline formatting 
			specification to paragraph builder. """
		self.prefix += '<%s' % key
		for k,v in attrs.items():
			self.prefix += ' %s="%s"' % (k,v)
		self.prefix += '>'
		
		self.suffix = '</%s>%s' % ( key, self.suffix )
			
			
			

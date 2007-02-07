
"""
$Id$
$URL$

Copyright (C) 2004 Matteo Merli <matteo.merli@gmail.com>

This code is licenced under the GPL. See LICENSE file.
"""

import xml.dom.minidom

from fo import FoBuilder
from pixies.utils import *
from pixies.elements import *

class Handler( FoBuilder ):
	def __init__(self, root):
		self.tag = None
		self.text = ''
		self.seq_master = {}
		self.attrs = None
		FoBuilder()
		self.handle_root( root )
		
	def getText(self, node):
		rc = ""
		for node in node.childNodes:
			if node.nodeType == node.TEXT_NODE:
				rc += node.data
			elif node.nodeName == 'fo:inline':
				inline = self.handle_inline( node )
				rc += inline.getText()
			elif node.nodeName == 'fo:page-number':
				rc += "#1"
			elif node.nodeName == 'fo:marker':
				pass 
				# text = self.getText( node )
				# print "fo:marker:", text
			elif node.nodeName == 'fo:block':
				return rc
				"""<fo:marker marker-class-name="section.head.marker">Competencies</fo:marker>"""
				  
			else:
				print "Unhandled Inline tag:", node.nodeName
		return rc
			
	def handle_root(self, root ):
		for i in root.getElementsByTagName("fo:layout-master-set"):
			self.handle_layout_master_set( i )
		for sequence in root.getElementsByTagName('fo:page-sequence'):
			self.handle_page_sequence( sequence )
			
	def handle_layout_master_set(self, set):
		for i in set.getElementsByTagName("fo:simple-page-master"):
			attrs = Attrs( i )
			self.fo_simple_page_master( attrs )
			## print "###", attrs['master-name']
			
			# Get values for various page regions
			for region in i.childNodes:
				if region.nodeType == region.TEXT_NODE:
					continue
				a = dict( region.attributes.items() )
				
				name = a.get('region-name', "xsl-%s" % region.nodeName.split(':')[-1])
				self.fo_region( name, attrs['master-name'], a )
				
		for seq in set.getElementsByTagName('fo:page-sequence-master'):
			seq_master = SequenceMaster( seq )
			self.seq_master[ seq_master.name ] = seq_master
			
	def handle_page_sequence(self, seq ):
		attrs = Attrs( seq )
		self.page_sequence = attrs['master-reference']
		
		self.fo_page_sequence( self.page_sequence )
		
		for c in seq.childNodes:
			if c.nodeName[:3] != 'fo:': continue
			
			## print c.nodeName
			if c.nodeName == 'fo:static-content':
				self.handle_static_content( c )
			elif c.nodeName == 'fo:flow':
				self.handle_flow( c )
				
	def handle_static_content( self, static ):
		attrs = Attrs( static )
		self.region = attrs['flow-name']
		print "Static Content: ==> ", self.region, " page_sequence:", self.page_sequence
		######## self.handle_blocks( blocks, page_sequence, region )
	
	def handle_flow( self, flow ):
		attrs = Attrs( flow )
		self.region = attrs['flow-name']
		print "Flow Content: ==> ", self.region, " page_sequence:", self.page_sequence
		## blocks = flow.getElementsByTagName("fo:block")
		### self.handle_blocks( blocks )
		self.handle_contents( flow )
		
	def handle_blocks( self, blocks ):
		for block in blocks:
			self.handle_block( block )
			
	def handle_block(self, block ):
		attrs = Attrs( block )
		self.fo_block( self.getText(block), attrs, self.page_sequence, self.region )
		# for b in block.getElementsByTagName('fo:block'):
		#	self.handle_block( b )
		
	def handle_inline(self, inline ):
		return Inline( inline )
		
	def handle_contents( self, node ):
		""" Handle all types of block-level elements that are 
			children of this node. """
		for n in node.childNodes:
			if n.nodeName == 'fo:block':
				self.handle_block( n )
			if n.nodeName == 'fo:external-graphic':
				self.fo_graphic( Attrs( n ), self.page_sequence, self.region )
			if n.nodeName == 'fo:list-block':
				self.fo_list( n, self.page_sequence, self.region )
	

def go( filename=None, buffer=None ):
	
	if not (filename or buffer):
		Error("We don't have and XSL-FO input")
	if (filename and buffer):
		Error("We have two XSL-FO input!")

	if filename:
		root = xml.dom.minidom.parse( filename )
	elif string:
		root = xml.dom.minidom.parseString( buffer )
		
	dh = Handler( root )
	
	# returns the instance of the handler
	return dh
	
	
	
	

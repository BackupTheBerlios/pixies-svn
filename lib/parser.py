
"""
$Id$
$URL$

Copyright (C) 2004 Matteo Merli <matteo.merli@gmail.com>

This code is licenced under the GPL. See LICENSE file.
"""

import xml.dom.minidom

from fo import FoBuilder
from lib.utils import *
from lib.elements import *

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
		page_sequence = attrs['master-reference']
		
		self.fo_page_sequence( page_sequence )
		
		for c in seq.childNodes:
			if c.nodeName[:3] != 'fo:': continue
			
			## print c.nodeName
			if c.nodeName == 'fo:static-content':
				self.handle_static_content( c, page_sequence )
			elif c.nodeName == 'fo:flow':
				self.handle_flow( c, page_sequence )
				
	def handle_static_content(self, static, page_sequence):
		attrs = Attrs( static )
		region = attrs['flow-name']
		print "Static Content: ==> ", region, " page_sequence:", page_sequence
		blocks = static.getElementsByTagName("fo:block")
		##for i in blocks:
		## print i.nodeName, ' - ' ,self.getText( i )
		self.handle_blocks( blocks, page_sequence, region )
	
	def handle_flow(self, flow, page_sequence):
		attrs = Attrs( flow )
		region = attrs['flow-name']
		print "Flow: ==> ", region
		blocks = flow.getElementsByTagName("fo:block")
		self.handle_blocks( blocks, page_sequence, region )
		
	def handle_blocks(self, blocks, page_sequence, region ):
		for block in blocks:
			self.handle_block( block, page_sequence, region )
			
	def handle_block(self, block, page_sequence, region ):
		attrs = Attrs( block )
		self.fo_block( self.getText(block), attrs, page_sequence, region )
		# for b in block.getElementsByTagName('fo:block'):
		#	self.handle_block( b )
		
	def handle_inline(self, inline ):
		return Inline( inline )
	
	

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
	
	
	
	

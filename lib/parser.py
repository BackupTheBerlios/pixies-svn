
"""
$Id$
$URL$

Copyright (C) 2004 Matteo Merli <matteo.merli@gmail.com>
"""

import xml.dom.minidom

from fo import FoBuilder

def normalize_whitespace(text):
    """Remove redundant whitespace from a string"""
    return ' '.join(text.split())

class Handler( FoBuilder ):
	def __init__(self, root):
		self.tag = None
		self.text = ''
		self.attrs = None
		FoBuilder()
		self.handle_root( root )
		
	def getText(self, node):
		rc = ""
		for node in node.childNodes:
			if node.nodeType == node.TEXT_NODE:
				rc += node.data
			elif node.nodeName == 'fo:inline':
				rc += self.handle_inline( node )
			elif node.nodeName == 'fo:page-number':
				rc += "#1"
			elif node.nodeName == 'fo:marker':
				pass 
				# text = self.getText( node )
				# print "fo:marker:", text
			elif node.nodeName == 'fo:block':
				return rc
				"""<fo:marker marker-class-name="section.head.marker">
                 			 Competencies</fo:marker>
                 		"""
				  
			else:
				print "Unhandled Inline tag:", node.nodeName
		return rc
			
	def handle_root(self, root ):
		print "fo:root", root.nodeType, root.nodeValue
		for i in root.getElementsByTagName("fo:layout-master-set"):
			self.handle_layout_master_set( i )
		for sequence in root.getElementsByTagName('fo:page-sequence'):
			self.handle_page_sequence( sequence )
			
	def handle_layout_master_set(self, set):
		for i in set.getElementsByTagName("fo:simple-page-master"):
			attrs = dict( i.attributes.items() )
			self.fo_simple_page_master( attrs )
			## print "###", attrs['master-name']
			
			# Get values for various page regions
			for region in i.childNodes:
				if region.nodeType == region.TEXT_NODE:
					continue
				a = dict( region.attributes.items() )
				
				name = a.get('region-name', "xsl-%s" % region.nodeName.split(':')[-1])
				self.fo_region( name, attrs['master-name'], a )
				
		for i in set.getElementsByTagName('fo:page-sequence-master'):
			attrs = dict( i.attributes.items() )
			sequence_name = attrs['master-name']
			# print "Sequence Name:", sequence_name
			for j in i.getElementsByTagName('fo:repeatable-page-master-alternatives'):
				for h in j.childNodes:
					if h.nodeName == 'fo:conditional-page-master-reference':
						attrs = dict( h.attributes.items() )
						master = attrs['master-reference']
						# print "Conditional - Master:", master
						
						self.fo_page_master_reference( master, sequence_name )
						
						#### Ok.. actually we only use the first page template
						break
					
				
	def handle_page_sequence(self, seq ):
		attrs = dict( seq.attributes.items() )
		## print "Page Sequence - Ref:", attrs['master-reference']
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
		attrs = dict( static.attributes.items() )
		region = attrs['flow-name']
		# print "Static Content: ==> ", region
		blocks = static.getElementsByTagName("fo:block")
		##for i in blocks:
		## print i.nodeName, ' - ' ,self.getText( i )
		self.handle_blocks( blocks, page_sequence, region )
	
	def handle_flow(self, flow, page_sequence):
		attrs = dict( flow.attributes.items() )
		region = attrs['flow-name']
		print "Flow: ==> ", region
		blocks = flow.getElementsByTagName("fo:block")
		self.handle_blocks( blocks, page_sequence, region )
		
	def handle_blocks(self, blocks, page_sequence, region ):
		for block in blocks:
			self.handle_block( block, page_sequence, region )
			
	def handle_block(self, block, page_sequence, region ):
		# print "fo:block"
		attrs = dict( block.attributes.items() )
		# print "TEXT:", getText( block )
		self.fo_block( self.getText(block), attrs, page_sequence, region )
		# for b in block.getElementsByTagName('fo:block'):
		#	self.handle_block( b )
		
	def handle_inline(self, inline ):
		print "fo:inline"
		attrs = dict( inline.attributes.items() )
		print attrs
		return "<i>%s</i>" %  unicode( self.getText( inline ) )
	 
	

def go( filename ):

	root = xml.dom.minidom.parse( filename )
	dh = Handler( root )
	
	# returns the instance of the handler
	return dh
	
	
	
	
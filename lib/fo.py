
"""
$Id$
$URL$

Copyright (C) 2004 Matteo Merli <matteo.merli@gmail.com>
"""

from reportlab.platypus import *

from lib.elements import *


##################from reportlab.platypus.para import Paragraph




############################################################################

class Sequence:
	name = None
	regions = {}
	"""
		'xsl-region-before' : [],  ### Elements list
		'xsl-region-body' : [],
		'xsl-region-after' : []
	"""
		

		
class FoBuilder:
	
		
	sequences = []
	page_masters = {}
	master = None
	
	def __init__(self):
		pass
	
	def fo_page_master(self, attrs ):
		pass
	
	def fo_simple_page_master(self, attrs ):
		self.page_masters[ attrs['master-name'] ] = PageMaster( attrs )

	def fo_region(self, name, master, attrs ):
		r = Region( attrs )
		self.page_masters[ master ][ name ] = r
		
	def fo_page_master_reference(self, master, sequence_name ):
		self.master = master
		
	def fo_page_sequence(self, name):
		sequence = Sequence()
		sequence.name = name
		self.sequences.append( sequence )

	def fo_block(self, text, attrs, sequence, region):
		
		###REMOVE ME
		if len(text) < 5: 
			# print "'Empty' box: "
			# print attrs
			return
		
		seq = None
		for s in self.sequences:
			if s.name == sequence:
				print "We are in sequence:", sequence
				seq = s 
				break
			
		if not seq:
			print "\n\nSequences:"
			for i in self.sequences:
				print " *", i.name
			print "Sequence not found: '%s'\n" % sequence
			raise ValueError
		
		# print seq.regions
		
		if not seq.regions.get( region ):
			seq.regions[ region ] = []
			
		seq.regions[ region ].append( 
						Block( text, attrs ) 
				)
		
		
		
		
		

"""
$Id$
$URL$

Copyright (C) 2004 Matteo Merli <matteo.merli@gmail.com>

This code is licenced under the GPL. See LICENSE file.
"""

from pixies.reportlab.platypus import *
from pixies.elements import *
from pixies.utils import *

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

	def fo_block(self, text, attrs, seq_name, region):
		
		seq = self.get_sequence( seq_name, region )
		
		###REMOVE ME
		if len(text) < 5: 
			# print "'Empty' box: "
			# print attrs
			return
		
		seq.regions[ region ].append( 
						Block( text, attrs ) 
				)
				
	def fo_graphic( self, attrs, seq_name, region ):
		seq = self.get_sequence( seq_name, region )
		seq.regions[ region ].append( ExternalGraphic( attrs ) )
		
	## def fo_list( self, node ):
	### 	
		
		
	def get_sequence( self, seq_name, region ):
		seq = None
		for s in self.sequences:
			if s.name == seq_name:
				seq = s 
				break
			
		if not seq:
			Log("\n\nSequences:")
			for i in self.sequences:
				Log(" * %s" % i.name )
			Error( "Sequence not found: '%s'" % seq_name )
		
		# initialize the region list
		if not seq.regions.get( region ):
			seq.regions[ region ] = []
			
		return seq
		
		
		

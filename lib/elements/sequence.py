
"""
$Id$
$URL$

Copyright (C) 2004 Matteo Merli <matteo.merli@gmail.com>
"""

from lib.utils import *

class SinglePageMaster:
	
	def __init__( self, node ):
		attrs = Attrs( node )
		self.master_reference = attrs['master-reference']
		print "NEW single-page-master-reference"
		
class RepeteablePageMaster:
	
	def __init__( self, node ):
		pass
		
class AlternativePageMaster:
	
	def __init__( self, node ):
		attrs = Attrs( node )
		self.maximum_repeat = attrs.get( 'maximum-repeat', 0 )
		self.conditions = []
		print "New repeatable-page-master-alternatives"
		print "Conditions:"
		for n in node.childNodes:
			if n.nodeName != 'fo:conditional-page-master-reference':
				continue
			self.conditions.append( Conditional( n ) )
			
class Conditional:
	
	def __init__( self, node ):
		attrs = Attrs( node )
		self.master_reference = attrs['master-reference']
		
		self.page_position = attrs.get( 'page-position', None )
		self.odd_or_even = attrs.get( 'odd-or-even', None )
		self.blank_or_not_blank = attrs.get( 'blank-or-not-blank', None )
		
		s = ''
		if self.odd_or_even: s += " [odd-or-even='%s']" % self.odd_or_even
		if self.page_position: s += " [page-position='%s']" % self.page_position
		if self.blank_or_not_blank: s += " [blank-or-not-blank='%s']" % self.blank_or_not_blank
		print " * '%s' --%s" % ( self.master_reference, s )
		
	def test( self, page_number, rel_page_number, blank=None ):
		result = True 
		if self._test_position( rel_page_number ) is False: 
			return False
		if self._test_odd( page_number ) is False:
			return False
	
	def _test_position( self, rel_page_number ):
		if not self.page_position:
			return None
			
		if self.page_position == 'any':
			return True
		if self.page_position == 'first' and rel_page_number == 1:
			return True
		if self.page_position == 'rest' and rel_page_number > 1:
			return True
		## Actually I don't have clue how to treat the case of page-position="last"
		## The problem is that at this point we don't down the total number of
		## pages
		## if self.page_position == 'last' and rel_page_number > 1:
		##	return True	
		return False
		
	def _test_odd( self, page_number ):
		if not self.odd_or_even:
			return None
		if self.odd_or_even == 'any': 
			return True
			
		i = ['even','odd'].index( self.odd_or_even )
		if ( (page_number + i) % 2 ) == 0:
			return True
			
		return False

class SequenceMaster:
	
	def __init__(self, node):
		self.subsequences = []
		self.attrs = Attrs( node )
		self.name = self.attrs['master-name']
		print "***\nNew sequence: ",  self.name
		
		print "Elements:"
		for j in node.childNodes:
			if j.nodeName == 'fo:single-page-master-reference':
				self.subsequences.append( SinglePageMaster( j ) )
			if j.nodeName == 'fo:repeatable-page-master-reference':
				self.subsequences.append( RepeteablePageMaster( j ) )
			if j.nodeName == 'fo:repeatable-page-master-alternatives':
				self.subsequences.append( AlternativePageMaster( j ) )
				
		"""
		# ('fo:repeatable-page-master-alternatives'):
			
			for h in j.childNodes:
				print 
				
				if h.nodeName == 'fo:conditional-page-master-reference':
					attrs = Attrs( h )
					master = attrs['master-reference']
					print "Conditional - Master:", master
					
					self.fo_page_master_reference( master, sequence_name )
					
					#### Ok.. actually we only use the first page template
					break
				"""
				
		print "-----"


"""
$Id$
$URL$

Copyright (C) 2004 Matteo Merli <matteo.merli@gmail.com>

This code is licenced under the GPL. See LICENSE file.
"""

from pixies.utils import *

class SinglePageMaster:
	
	def __init__( self, node ):
		attrs = Attrs( node )
		self.master_reference = attrs['master-reference']
		Log( " - fp:single-page-master-reference [%s]" % self.master_reference )
		
class RepeteablePageMaster:
	
	def __init__( self, node ):
		attrs = Attrs( node )
		self.maximum_repeat = attrs.get( 'maximum-repeat', 0 )
		self.master_reference = attrs['master-reference']
		Log(' - fo:repeteable-page-master [max:%u] [%s]' % (self.maximum_repeat, self.master_reference))
		
	def get( self, page_number, rel_page_number ):
		return self.master_reference
		
class AlternativePageMaster:
	
	def __init__( self, node ):
		attrs = Attrs( node )
		self.maximum_repeat = attrs.get( 'maximum-repeat', 0 )
		self.conditions = []
		Log( " - fo:repeatable-page-master-alternatives" )
		Log( "     Conditions:" )
		for n in node.childNodes:
			if n.nodeName != 'fo:conditional-page-master-reference':
				continue
			self.conditions.append( Conditional( n ) )
			
	def get( self, page_number, rel_page_number ):
		for c in self.conditions:
			if c.test( page_number, rel_page_number ):
				return c.master_reference
				
		return None
			
class Conditional:
	""" Represent a condition in a 
		&lt;fo:repeteable-page-master-alternatives&gt; """
	
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
		Log( "      * '%s' --%s" % ( self.master_reference, s ) )
		
	def test( self, page_number, rel_page_number, blank=None ):
		""" Test if the page-master specified should be used for the current page. """
		result = True 
		if self._test_position( rel_page_number ) is False: 
			return False
		if self._test_odd( page_number ) is False:
			return False
		if self._test_blank() is False:
			return False
			
		return True
	
	def _test_position( self, rel_page_number ):
		""" Test the page-position condition """
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
		## if self.page_position == 'last' and ???? :
		##	return True	
		return False
		
	def _test_odd( self, page_number ):
		""" Test the odd-or-even condition. """
		if not self.odd_or_even:
			return None
		if self.odd_or_even == 'any': 
			return True
			
		i = ['even','odd'].index( self.odd_or_even )
		if ( (page_number + i) % 2 ) == 0:
			return True
			
		return False
		
	def _test_blank( self, blank=None ):
		""" Test the blank-or-not-blank. """
		if not self.blank_or_not_blank:
			return None
		
		if self.blank_or_not_blank == 'any':
			return True
		if self.blank_or_not_blank == 'blank':
			# Actually we don't effectevely test it.. 
			# we just say that all the pages are not blank
			# XXX This should be fixed in a remote future..
			return False
		return True
			

class SequenceMaster:
	
	def __init__( self, node ):
		self.subsequences = []
		self.attrs = Attrs( node )
		self.name = self.attrs['master-name']
		Log( "***\nNew sequence: " + self.name )
		
		Log( "Elements:" )
		for j in node.childNodes:
			if j.nodeName == 'fo:single-page-master-reference':
				self.subsequences.append( SinglePageMaster( j ) )
			if j.nodeName == 'fo:repeatable-page-master-reference':
				self.subsequences.append( RepeteablePageMaster( j ) )
			if j.nodeName == 'fo:repeatable-page-master-alternatives':
				self.subsequences.append( AlternativePageMaster( j ) )
				
		Log( "-----" )


	def getMaster( self, page_number, rel_page_number ):
		""" Returns the reference to the page-master to be used 
			in the current page. """
		
		for s in self.subsequences:
			r = s.get( page_number, page_number )
			if r: return r
		


"""
$Id$
$URL$

Copyright (C) 2004 Matteo Merli <matteo.merli@gmail.com>
"""

from properties import *

class PageMaster( Properties ):
	
	regions = {}
	
	def __init__(self, attrs):
		Properties.__init__(self)
		##  It is not an error to consider always present the 
		##  'master-name' key..  It should be so, and if not
		##  we don't know how to refer to it. ( so better to 
		## trigger an exception.
		self.name = attrs['master-name']
		
		self.common_margins( attrs )
		p = self.properties
		
		# These properties only apply to page_master
		if 'page-width' in attrs:
			p['page-width'] = toLength( attrs['page-width'] )
		if 'page-height' in attrs:
			p['page-height'] = toLength( attrs['page-height'] )
		
		if 'reference-orientation' in attrs:
			NotImplemented('reference-orientation')
		if 'writing-mode' in attrs:
			NotImplemented('writing-mode')
			
		self.width = get( p, 'page-width' )
		self.height = get( p, 'page-height' )
		self.pagesize = (self.width, self.height)
		
		self.leftMargin   = get( p, 'margin-left'  )
		self.rightMargin  = get( p, 'margin-right' )
		self.topMargin    = get( p, 'margin-top'   )
		self.bottomMargin = get( p, 'margin-bottom')
		
	def __setitem__(self, key, obj):
		self.regions[ key ] = obj
		
		

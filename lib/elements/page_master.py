
"""
$Id$
$URL$

Copyright (C) 2004 Matteo Merli <matteo.merli@gmail.com>
"""

from properties import *

class PageMaster( Properties ):
	
	def __init__(self, attrs):
		
		##  It is not an error to consider always present the 
		##  'master-name' key..  It should be so, and if not
		##  we don't know how to refer to it. ( so better to 
		## trigger an exception.
		name = attrs['master-name']
		
		self.common_margins( attrs )
		
		if 'reference-orientation' in attrs:
			NotImplemented('reference-orientation')
		if 'writing-mode' in attrs:
			NotImplemented('writing-mode')
		

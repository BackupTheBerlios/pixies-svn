
"""
$Id$
$URL$

Copyright (C) 2004 Matteo Merli <matteo.merli@gmail.com>
"""

import copy

def My(obj):
	""" Returns a 'deep' copy of the object """
	return copy.deepcopy( obj )


def Attrs( node ):
	""" Returns a dict containing all the xml properties """
	return dict( node.attributes.items() )

def get( obj, attr ):
	""" Returns a dict element with a default of float(0.0) """
	try:
		f = obj.get( attr, 0.0 )
	except:
		f = 0.0
	return f


"""
$Id$
$URL$

Copyright (C) 2004 Matteo Merli <matteo.merli@gmail.com>

This code is licenced under the GPL. See LICENSE file.
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

def trim_spaces(text):
    """Remove redundant whitespace from a string"""
    return ' '.join( text.split() )

def escape_tags(text):
	"""Replace < and > with &lt; and &gt; """
	if not text: return ''
	text.replace('<', '&lt;')
	text.replace('>', '&gt;')
	return text

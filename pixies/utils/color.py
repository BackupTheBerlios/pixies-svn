
"""
$Id$
$URL$

Copyright (C) 2004 Matteo Merli <matteo.merli@gmail.com>

This code is licenced under the GPL. See LICENSE file.
"""

from reportlab.lib import colors
# import Color, toColor
from pixies.utils import *

def toColor( color ):
	""" Convert a color string to an internal representation """
	if type(color) is unicode:
		color = color.encode('utf-8')
		
	try:
		c = colors.toColor( color )
	except:
		Warning( "Color not found '%s'" % c )
		# Set to black
		c = colors.Color( 0, 0, 0 )
		
	return c

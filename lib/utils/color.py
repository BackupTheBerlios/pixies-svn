
"""
$Id$
$URL$

Copyright (C) 2004 Matteo Merli <matteo.merli@gmail.com>
"""

from reportlab.lib import colors
# import Color, toColor
from lib.utils import *

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

"""
$Id$
$URL$

Copyright (C) 2004 Matteo Merli <matteo.merli@gmail.com>
"""

from reportlab.lib.enums import *

def Align( a ):
	if a == 'left': return TA_LEFT
	if a == 'right': return TA_RIGHT
	if a == 'center': return TA_CENTER
	if a == 'justify': return TA_JUSTIFY
	if a == 'start': return TA_LEFT
	if a == 'end': return TA_RIGHT
	# default
	return TA_LEFT 

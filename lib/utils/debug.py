
"""
$Id$
$URL$

Copyright (C) 2004 Matteo Merli <matteo.merli@gmail.com>
"""

import sys

DEBUG = 1 

def Warning( msg ):
	if DEBUG:
		sys.stderr.write( 'WARNING: %s' % msg )
		
def NotImplemented( feature ):
	Warning("Not Implemented: '%s'" % feature)

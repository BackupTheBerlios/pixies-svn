
"""
$Id$
$URL$

Copyright (C) 2004 Matteo Merli <matteo.merli@gmail.com>

This code is licenced under the GPL. See LICENSE file.
"""

import sys

DEBUG = 1 

def Error( msg ):
	sys.stderr.write( '\nERROR:\n%s\n\n' % msg )
	sys.exit( -1 )

def Warning( msg ):
	if DEBUG:
		sys.stderr.write( 'WARNING: %s\n' % msg )
		
def NotImplemented( feature ):
	Warning("Not Implemented: '%s'" % feature)
	
def Log( msg ):
	if type( msg ) == list:
		msg = ' '.join( msg )
	sys.stderr.write( msg + '\n' )

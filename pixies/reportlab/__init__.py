
"""
$Id$
$URL$

Copyright (C) 2004 Matteo Merli <matteo.merli@gmail.com>

This code is licenced under the GPL. See LICENSE file.
"""

__all__ = ['lib', 'pdfbase', 'pdfgen', 'platypus'] 

# We change the sys.path because we need to import
# reportlab.* which is actually in a subfolfer of 
# pixies.
# The matter is that I want to keep ReportLab sources
# untouched, without adding the "pixies" prefix in 
# its include statements.

import sys, os, copy

if not 'dummy' in sys.path:

	path = copy.deepcopy( sys.path )
	for i in path:
		sys.path.insert( 0, i + os.path.sep + 'pixies' )

	# This value is inserted to mark the sys.path list
	sys.path.append('dummy')

	### print "PATH:", sys.path, "\n\n"
	del path
	


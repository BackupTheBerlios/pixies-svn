
"""
$Id$
$URL$

Copyright (C) 2004 Matteo Merli <matteo.merli@gmail.com>

This code is licenced under the GPL. See LICENSE file.

This module contains the functions to convert the XML documents 
to XSL-FO using a XSL stylesheet.
We should take care that someone may not have the xml and xslt 
extensions installed. The only thing we do is to inform of the
problem.
"""

from pixies.utils import *

_have_xslt = True

try:
	import libxml2
	import libxslt
except ImportError:
	_have_xsl = False

_err_msg = """
The XSLT transformation you required requires some Python modules that
are not insalled in your system. 
You can do the transformation with another program and then convert the
obtained XSL-FO to PDF with Pixies, or install the extension.

Download and install the following Python modules (Chances are that they
are packaged and present on the CDs of your distribution):

 * libxml2  - http://xmlsoft.org/
 * libxslt  - http://xmlsoft.org/XSLT/ 
"""

def xslt_convert( xml, xsl ):
	if not _have_xslt:
		Error( _err_msg )

	libxml2.lineNumbersDefault( 1 )
	libxml2.substituteEntitiesDefault( 1 )
	
	styledoc = libxml2.parseFile( xsl )
	if not styledoc:
		Error("Cannot parse stylesheet: '%s'" % xsl )

	style = libxslt.parseStylesheetDoc( styledoc )

	doc = libxml2.parseFile( xml )
	if not doc:
		Error("Unable to parse XML document: '%s'" % xml )

	result = style.applyStylesheet( doc, None )
	s = style.saveResultToString( result )
	style.freeStylesheet()
	doc.freeDoc()
	result.freeDoc()
	return s

if __name__ == '__main__':
	import sys 
	xml = sys.argv[1]
	xsl = sys.argv[2]
	xsl_fo = xslt_convert( xml, xsl )
	print xsl_fo


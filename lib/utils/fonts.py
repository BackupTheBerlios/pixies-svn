
"""
$Id$
$URL$

Copyright (C) 2004 Matteo Merli <matteo.merli@gmail.com>
"""

from reportlab.lib.fonts import *
from reportlab.lib.fonts import _tt2ps_map

# Added some very basic fonts.. 
# They should be already there from ReportLab, but the alias
# machinery is not working..
addMapping('serif', 0, 0, 'Times-Roman')
addMapping('serif', 1, 0, 'Times-Bold')
addMapping('serif', 0, 1, 'Times-Italic')
addMapping('serif', 1, 1, 'Times-BoldItalic')
addMapping('sans-serif', 0, 0, 'Helvetica')
addMapping('sans-serif', 1, 0, 'Helvetica-Bold')
addMapping('sans-serif', 0, 1, 'Helvetica-Oblique')
addMapping('sans-serif', 1, 1, 'Helvetica-BoldOblique')
addMapping('monospace', 0, 0, 'Courier')
addMapping('monospace', 1, 0, 'Courier New-Bold')
addMapping('monospace', 0, 1, 'Courier New-Italic')
addMapping('monospace', 1, 1, 'Courier New-BoldItalic')


_families = {}

# We keep a list of all valid family names
for k in _tt2ps_map.keys():
	_families[ k[0] ] = None
	
print "Valid font families:\n", _families


# Default Font
bold = 0
italic = 0
font = 'serif'
default_font = tt2ps( font, bold, italic )

	
def PsFont( attrs, default=default_font ):
	""" Return the Postscript description of the selected font """
	font, bold, italic = ps2tt( default )
	
	if 'font-family' in attrs:
		font_list = attrs['font-family'].split(',')
		for f in font_list:
			if f.lower() in _families:
				font = f.lower()
				break
			
		
	if 'font-style' in attrs:
		if attrs['font-style'] == 'italic':
			italic = 1
	if 'font-weight' in attrs:
		if attrs['font-weight'] != 'normal':
			bold = 1
	return tt2ps( font, bold, italic ) 

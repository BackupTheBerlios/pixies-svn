
"""
$Id$
$URL$

Copyright (C) 2004 Matteo Merli <matteo.merli@gmail.com>
"""

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import *
from reportlab.lib.units import *
from reportlab.lib.enums import *
from reportlab.lib.colors import Color, toColor
from reportlab.lib.fonts import *

##################from reportlab.platypus.para import Paragraph

import copy
def My(obj):
	return copy.deepcopy( obj )

styles = getSampleStyleSheet()

NormalStyle = My( styles["Normal"] )
NormalStyle.spaceBefore = 0.1*inch
NormalStyle.alignment = TA_JUSTIFY

def convertAlign( a ):
	if a == 'left': return TA_LEFT
	if a == 'right': return TA_RIGHT
	if a == 'center': return TA_CENTER
	if a == 'justify': return TA_JUSTIFY
	if a == 'start': return TA_LEFT
	if a == 'end': return TA_RIGHT
	# default
	return TA_LEFT

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
	
def convertFont( attrs, style ):
	font, bold, italic = ps2tt( style.fontName )
	if 'font-family' in attrs:
		font = attrs['font-family'].split(',')[0]
	if 'font-style' in attrs:
		if attrs['font-style'] == 'italic':
			italic = 1
	if 'font-weight' in attrs:
		if attrs['font-weight'] != 'normal':
			bold = 1
	return tt2ps( font, bold, italic )
	
## 1em is fixed to 11pt
em = 11
	
def toLength(s):
	'''convert a string to  a length'''
	try:
		if s[-2:]=='cm': return float(s[:-2])*cm
		if s[-2:]=='in': return float(s[:-2])*inch
		if s[-2:]=='pt': return float(s[:-2])
		if s[-1:]=='i': return float(s[:-1])*inch
		if s[-2:]=='mm': return float(s[:-2])*mm
		if s[-4:]=='pica': return float(s[:-4])*pica
		if s[-2:]=='pc': return float(s[:-2])*pica
		if s[-2:]=='em': return float(s[:-2]) * em
		if s[-1:]=='%': return float(s[:-1]) * em / 100
		return float(s)
	except:
		## check for the form: margin-left="1.2in - -1.5pc"
		try:
			l1, l2 = s.split(' - ')
			l1 = toLength( l1 )
			l2 = toLength( l2 )
			return float( l1 - l2 )
		except:
			raise
		raise ValueError, "Can't convert '%s' to length" % s

		
############################################################################
############################################################################
############################################################################

def checkSizeMarginAttrs( attrs ):
	d = {}
	if 'page-height' in attrs:
		d['page-height'] = toLength( attrs['page-height'] )
	if 'page-width' in attrs:
		d['page-width'] = toLength( attrs['page-width'] )
	if 'margin-left' in attrs:
		d['margin-left'] = toLength( attrs['margin-left'] )
	if 'margin-right' in attrs:
		d['margin-right'] = toLength( attrs['margin-right'] )
	if 'margin-top' in attrs:
		d['margin-top'] = toLength( attrs['margin-top'] )
	if 'margin-bottom' in attrs:
		d['margin-bottom'] = toLength( attrs['margin-bottom'] )
	if 'padding-left' in attrs:
		d['padding-left'] = toLength( attrs['padding-left'] )
	if 'padding-right' in attrs:
		d['padding-right'] = toLength( attrs['padding-right'] )
	if 'padding-top' in attrs:
		d['padding-top'] = toLength( attrs['padding-top'] )
	if 'padding-bottom' in attrs:
		d['padding-bottom'] = toLength( attrs['padding-bottom'] )
	if 'extent' in attrs:
		d['extent'] = toLength( attrs['extent'] )
	return d


############################################################################

class Sequence:
	name = None
	regions = {}
	"""
		'xsl-region-before' : [],  ### Elements list
		'xsl-region-body' : [],
		'xsl-region-after' : []
	"""
		

		
class FoBuilder:
	
		
	sequences = []
	page_masters = {}
	master = None
	
	def __init__(self):
		pass
	
	def fo_page_master(self, attrs ):
		pass
	
	def fo_simple_page_master(self, attrs ):
		name = attrs['master-name']

		pm = checkSizeMarginAttrs( attrs )
		self.page_masters[ name ] = pm

	def fo_region(self, name, master, attrs ):
		rm = checkSizeMarginAttrs( attrs )
		self.page_masters[ master ][ name ] = rm
		
	def fo_page_master_reference(self, master, sequence_name ):
		self.master = master
		
	def fo_page_sequence(self, name):
		sequence = Sequence()
		sequence.name = name
		self.sequences.append( sequence )

	"""
	<fo:block font-size="18pt"
            font-family="sans-serif"
            line-height="24pt"
            space-after.optimum="15pt"
            background-color="blue"
            color="white"
            text-align="center"
            padding-top="3pt"
            font-variant="small-caps">
	"""
	def fo_block(self, text, attrs, sequence, region):
		# print "__BLOCK__"
		#for k,v in attrs:
		#	print k,':', v
		#print text, '\n----------------------'
		
		###REMOVE ME
		if len(text) < 5: 
			# print "'Empty' box: "
			# print attrs
			return
		
		style = My( NormalStyle )
		
		## print attrs
		
		style.fontName = convertFont( attrs, style )
		# print style.fontName
		if 'font-size' in attrs:
			style.fontSize = toLength( attrs['font-size'] )
		if 'color' in attrs:
			style.textColor = toColor( attrs['color'].encode('utf-8') )
		if 'background-color' in attrs :
			style.backColor = toColor( attrs['background-color'].encode('utf-8') )
		if 'text-align' in attrs:
			style.alignment = convertAlign( attrs['text-align'] )
		if 'line-height' in attrs:
			style.leading = toLength( attrs['line-height'] )
		if 'text-indent' in attrs:
			style.firstLineIndent = toLength( attrs['text-indent'] )
		if 'space-before.optimum' in attrs:
			style.spaceBefore = toLength( attrs['space-before.optimum'] )
		if 'space-after.optimum' in attrs:
			style.spaceAfter = toLength( attrs['space-after.optimum'] )	
		
		seq = None
		for s in self.sequences:
			if s.name == sequence:
				print "We are in sequence:", sequence
				seq = s 
				break
			
		if not seq:
			print "\n\nSequences:"
			for i in self.sequences:
				print " *", i.name
			print "Sequence not found: '%s'\n" % sequence
			raise ValueError
		
		# print seq.regions
		
		if not seq.regions.get( region ):
			seq.regions[ region ] = []
			
		seq.regions[ region ].append( 
						Paragraph( text.encode('latin1', 'ignore'), style ) 
				)
		
		
		
		
		
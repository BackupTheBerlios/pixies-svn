
"""
$Id$
$URL$

Copyright (C) 2004 Matteo Merli <matteo.merli@gmail.com>
"""

from reportlab.platypus.paragraph import *


class Block( Paragraph ):
	
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
	def __init__(self, text, attrs, sequence, region):
		
		###REMOVE ME
		if len(text) < 5: 
			# print "'Empty' box: "
			# print attrs
			return
		
		style = My( NormalStyle )
		
		## print attrs
		
		style.fontName = convertFont( attrs, style )
		# print style.fontName
		
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
			
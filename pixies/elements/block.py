
"""
$Id$
$URL$

Copyright (C) 2004 Matteo Merli <matteo.merli@gmail.com>

This code is licenced under the GPL. See LICENSE file.
"""

from reportlab.platypus.paragraph import *
from properties import *
from pixies.utils import *

class Block( Paragraph, Properties ):
	
	def __init__(self, text, attrs, bulletText=None, frags=None ):
		# The class is instancied from a split()
		if frags: 
			# print "I am a splitted paragraph..\n\n\n"
			# print "frags: ", frags
			# print "attrs: ", attrs
			# print "text: ", text
			# Paragraph.__init__ (self, text, attrs, bulletText=bulletText, frags=frags )
			# return 
			self.style = attrs
		
		else: 
			## We parse the fo attributes	
			Properties.__init__(self)
			text = text.encode('latin1', 'ignore')
		
			###REMOVE ME
			if len(text) < 5: 
				return
		
			self.common_fonts( attrs )
			self.common_margins( attrs )
			self.common_borders( attrs )
			self.common_text( attrs )
		
			self.style = Style( self.properties )
			## print self.properties
		
		self.caseSensitive = 1
		self._setup( text, self.style, bulletText, frags, cleanBlockQuotedText)

	def split(self,availWidth, availHeight):
		if len(self.frags)<=0: return []

		#the split information is all inside self.blPara
		if not hasattr(self,'blPara'):
			self.wrap(availWidth,availHeight)
		blPara = self.blPara
		style = self.style
		leading = style.leading
		lines = blPara.lines
		n = len(lines)
		s = int(availHeight/leading)
		if s<=1:
			del self.blPara
			return []
		if n<=s: return [self]
		func = self._get_split_blParaFunc()

		P1 = Block(None,style,bulletText=self.bulletText,frags=func(blPara,0,s))
		#this is a major hack
		P1.blPara = ParaLines(kind=1,lines=blPara.lines[0:s],aH=availHeight,aW=availWidth)
		P1._JustifyLast = 1
		if style.firstLineIndent != 0:
			style = deepcopy(style)
			style.firstLineIndent = 0
		P2 = Block(None,style,bulletText=None,frags=func(blPara,s,n))
		# print "P1\n", P1
		# print "P2\n", P2
		return [P1,P2]			
	

	def getPlainText(self,identify=None):
		"""Convenience function for templates which want access
		   to the raw text, without XML tags. """

		frags = getattr(self,'frags',None)
		if frags:
			plains = []
			for frag in frags:
				# plains.append( frag.text )
				plains.append( getattr( frag, 'text', '' ) )
			return join(plains, '')
		elif identify:
			text = getattr(self,'text',None)
			if text is None: text = repr(self)
			return text
		else:
			return ''

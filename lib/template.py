
"""
$Id$
$URL$

Copyright (C) 2004 Matteo Merli <matteo.merli@gmail.com>
"""

from reportlab.platypus import *
from reportlab.pdfgen import canvas

import copy
def My(obj):
	return copy.deepcopy( obj )

def get( obj, attr ):
	try:
		f = obj.get( attr, 0.0 )
	except:
		f = 0.0
	return f

def myPage(canvas, doc):
	print "CANVAS::: DOC:::"
	seq = doc.sequence.name
	header = My( doc.sequence.regions.get('xsl-region-before') )
	footer = My( doc.sequence.regions.get('xsl-region-after')  )
	canvas.saveState()
	
	for f in doc.pageTemplate.frames:
		elements = None
		if f.id == 'body': continue
		if f.id == 'before': elements = header
		if f.id == 'after': elements = footer
		
		if elements: 
			f.addFromList( elements, canvas )
		
	canvas.restoreState()
	
class DocumentTemplate(BaseDocTemplate):
	
	def __init__(self, filename, dh):
		self.dh = dh
		BaseDocTemplate.__init__(self, filename)
		for name,attrs in self.dh.page_masters.items():
			self.buildPageTemplate(name, attrs)
			
	def buildPageTemplate(self, name, attrs):
		print "New Page Template:", name
		width = attrs['page-width']
		height = attrs['page-height']
		pagesize = (width, height)
		
		leftMargin   = get(attrs,'margin-left')
		rightMargin  = get(attrs,'margin-right')
		topMargin    = get(attrs, 'margin-top')
		bottomMargin = get(attrs,'margin-bottom')
		
		be = self.dh.page_masters[name].get('xsl-region-before')
		bo = self.dh.page_masters[name].get('xsl-region-body')
		af = self.dh.page_masters[name].get('xsl-region-after')
		
		fwidth = width - leftMargin - rightMargin
		
		frameBefore = Frame( 
				leftMargin + get(be,'margin-left'),
				height - topMargin - get(be,'extent'), ## region-before bottomMargin
				fwidth, 
				get(be,'extent'), 
				id='before', showBoundary=0,
				leftPadding=get(be,'padding-left'),rightPadding=get(be,'padding-right'),
				topPadding=get(be,'padding-top'),bottomPadding=get(be,'padding-bottom') )
				
		frameBody =   Frame( 
				leftMargin + get(bo, 'margin-left'), 
				bottomMargin + 0, 
				fwidth, 
				height - topMargin - bottomMargin - get(bo, 'margin-bottom') - get(bo, 'margin-top'), 
				id='body', showBoundary=0,
				leftPadding=get(be,'padding-left'),rightPadding=get(be,'padding-right'),
				topPadding=get(be,'padding-top'),bottomPadding=get(be,'padding-bottom'))
		
		frameAfter =  Frame( 
				leftMargin, 
				bottomMargin + get(af,'margin-bottom'), 
				fwidth, 
				get(af,'extent'), 
				id='after', showBoundary=0,
				leftPadding=get(be,'padding-left'),rightPadding=get(be,'padding-right'),
				topPadding=get(be,'padding-top'),bottomPadding=get(be,'padding-bottom'))
	
		frame_list = [frameBody, frameBefore, frameAfter]
		tmpl = PageTemplate( id=name, frames=frame_list, pagesize=pagesize, onPage=myPage)
		self.addPageTemplates( tmpl )
		
	def handle_pageBegin( self ):
		for pt in self.pageTemplates:
			if pt.id == self.dh.master:
				self.pageTemplate = pt
				break
		print "Using Page Template:", self.pageTemplate.id
		self._handle_pageBegin()

	def build( self ):
		self._calc()
		# flowableCount = len(flowables)
		self._startBuild( None, canvas.Canvas )
		
		for seq in self.dh.sequences:
			self.sequence = seq
			flowables = seq.regions['xsl-region-body']

			while len(flowables):
				self.clean_hanging()
				try:
					first = flowables[0]
					self.handle_flowable(flowables)
				except:
					#if it has trace info, add it to the traceback message.
					if hasattr(first, '_traceInfo') and first._traceInfo:
						exc = sys.exc_info()[1]
						args = list(exc.args)
						tr = first._traceInfo
						args[0] = args[0] + '\n(srcFile %s, line %d char %d to line %d char %d)' % (
							tr.srcFile,
							tr.startLineNo,
							tr.startLinePos,
							tr.endLineNo,
							tr.endLinePos
							)
						exc.args = tuple(args)
					raise
		
		self._endBuild()
	
		
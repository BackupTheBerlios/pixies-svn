
"""
$Id$
$URL$

Copyright (C) 2004 Matteo Merli <matteo.merli@gmail.com>

This code is licenced under the GPL. See LICENSE file.
"""

from reportlab.platypus import *
from reportlab.pdfgen import canvas
from pixies.elements import Region
from pixies.utils import *

def myPage(canvas, doc):
	seq = doc.sequence.name
	before = My( doc.sequence.regions.get( 'xsl-region-before' ) )
	after = My( doc.sequence.regions.get( 'xsl-region-after' )  )
	start = My( doc.sequence.regions.get( 'xsl-region-start' )  )
	end = My( doc.sequence.regions.get( 'xsl-region-end' )  )
	
	canvas.saveState()
	
	for f in doc.pageTemplate.frames:
		elements = None
		if f.id == 'body': continue
		if f.id == 'before': elements = before
		if f.id == 'after':  elements = after
		if f.id == 'start':  elements = start
		if f.id == 'end':   elements = end
		
		if elements: 
			f.addFromList( elements, canvas )
		
	canvas.restoreState()
	

class DocumentTemplate(BaseDocTemplate):
	
	def __init__(self, filename, dh):
		self.dh = dh
		BaseDocTemplate.__init__(self, filename)
		
		self.pageTemplates = {}
		
		for pm in self.dh.page_masters.values():
			self.buildPageTemplate( pm )
			
		print "PAGE MASTERS:"
		for i in self.pageTemplates:
			print " * %s" % i
			
		print "\nSEQUENCES:"
		for i in self.dh.sequences:
			print " * %s" % i.name
			
			
	def buildPageTemplate(self, pm):
		# print "New Page Template:", pm.name
		
		empty = Region( {} )
		
		be = pm.regions.get( 'xsl-region-before', empty )
		bo = pm.regions.get( 'xsl-region-body',   empty )
		af = pm.regions.get( 'xsl-region-after', empty )
		st = pm.regions.get( 'xsl-region-start',  empty )
		en = pm.regions.get( 'xsl-region-end',    empty )
		
		fwidth = pm.width - pm.leftMargin - pm.rightMargin
		fheight = pm.height - pm.topMargin - pm.bottomMargin - be.extent - af.extent
		
		frameBefore = Frame( 
				pm.leftMargin,
				pm.height - pm.topMargin - be.extent,
				fwidth,
				be.extent, 
				id='before', showBoundary=0,
				leftPadding=be.paddingLeft, rightPadding=be.paddingRight,
				topPadding=be.paddingTop, bottomPadding=be.paddingBottom )
				
		frameStart = Frame( 
				pm.leftMargin,  # X0
				pm.bottomMargin + af.extent,  # Y0
				st.extent,   # width 
				fheight,  # height
				id='start', showBoundary=1,
				leftPadding=st.paddingLeft, rightPadding=st.paddingRight,
				topPadding=st.paddingTop, bottomPadding=st.paddingBottom )
				
		frameBody =  Frame( 
				pm.leftMargin + bo.marginLeft, 
				pm.bottomMargin + bo.marginBottom,  
				fwidth - bo.marginLeft - bo.marginRight,
				pm.height - pm.topMargin - pm.bottomMargin - bo.marginBottom - bo.marginTop, 
				id='body', showBoundary=0,
				leftPadding=bo.paddingLeft, rightPadding=bo.paddingRight,
				topPadding=bo.paddingTop, bottomPadding=bo.paddingBottom)
				
		frameEnd = Frame( 
				pm.width - pm.rightMargin - en.extent,  # X0
				pm.bottomMargin + af.extent, # Y0
				en.extent,   # width 
				fheight,  # height
				id='end', showBoundary=1,
				leftPadding=en.paddingLeft, rightPadding=en.paddingRight,
				topPadding=en.paddingTop, bottomPadding=en.paddingBottom )
				
		frameAfter =  Frame( 
				pm.leftMargin, 
				pm.bottomMargin, 
				fwidth, 
				af.extent, 
				id='after', showBoundary=1,
				leftPadding=af.paddingLeft, rightPadding=af.paddingRight,
				topPadding=af.paddingTop, bottomPadding=af.paddingBottom)
				
				
				
		frame_list = [frameBody, frameBefore, frameAfter, frameStart, frameEnd]
		tmpl = PageTemplate( id=pm.name, frames=frame_list, pagesize=pm.pagesize, onPage=myPage)
		self.pageTemplates[pm.name] = tmpl
		
	def handle_documentBegin(self):
		'''implement actions at beginning of document'''
		self._hanging = [PageBegin]
		self.pageTemplate = None
		self.page = 0
		Log( "\n[Document Begin]" )
		self.beforeDocument()
		
	def handle_pageBegin( self ):
		page = self.page + 1 
		if self.seq_master:
			pt = self.seq_master.getMaster( page, self.rel_page )
		else:
			print self.sequence.name
			print self.pageTemplates
			pt = self.pageTemplates[ self.sequence.name ]
		Log( "\t\t[%u] PageMaster='%s' [rel:%u]" % ( page, pt, self.rel_page ) )
		self.pageTemplate = self.pageTemplates[ pt ]
		self._handle_pageBegin()
		
	def handle_pageEnd( self ):
		self.rel_page += 1
		self._handle_pageEnd
		
	def build( self ):
		self._calc()
		self.sequence = None
		# flowableCount = len(flowables)
		self._startBuild( None, canvas.Canvas )
			
		for seq in self.dh.sequences:
			self.sequence = seq
			self.seq_master = self.dh.seq_master.get( seq.name , None )
			self.rel_page = 1
			Log( "\t[Seq: %s]" % seq.name )
			flowables = seq.regions['xsl-region-body']
			
			# After a page sequence, there's always a page break.
			flowables.append( PageBreak() )
				
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
		Log( "[Document Complete]\n" )
		
		

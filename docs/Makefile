
# $Id$
# $URL$

XHTML = /usr/share/sgml/docbook/xsl-stylesheets/xhtml/docbook.xsl 
FO = /usr/share/sgml/docbook/xsl-stylesheets/fo/docbook.xsl 
OPTIONS = -stringparam chunker.output.encoding UTF-8

all:
	xsltproc $(OPTIONS) -o design.html $(XHTML) design.xml
	
pdf:
	xsltproc $(OPTIONS) -o design.fo $(FO) design.xml
	xep design.fo
	rm -f design.fo
	
clean:
	rm -rf *~ *.fo *.pdf *.html
#!/usr/bin/env python

# $Id$
# $URL$

from distutils.core import setup

setup(
	name="pixies",
	version="0.2",
	description="Convert XML and XSL-FO to PDF.",
	long_description="""
Pixies is a formatter that convert XSL-FO 
documents to PDF. It is written in python and it is particulary 
focused on the production of PDF files from DocBook documents.
""",
	author="Matteo Merli",
	author_email="matteo.merli@gmail.com",
	licence="GPL",
	platforms='ALL',
	
	url="http://merlimat.net/software/pixies",
	packages=['pixies', 'pixies.utils', 'pixies.elements'],
	scripts=['pixies/pixies']
)


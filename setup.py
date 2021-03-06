#!/usr/bin/env python

# $Id$
# $URL$

from distutils.core import setup
from pixies import version

setup(
	name="pixies",
	version=version.string,
	description="Convert XML and XSL-FO to PDF.",
	long_description="""
Pixies is a formatter that convert XSL-FO 
documents to PDF. It is written in python and it is particulary 
focused on the production of PDF files from DocBook documents.
""",
	author="Matteo Merli",
	author_email="matteo.merli@gmail.com",
	license="GPL",
	platforms='ALL',
	
	url="http://merlimat.net/software/pixies",
	download_url='http://developer.berlios.de/project/showfiles.php?group_id=2516',
	packages=['pixies', 
		'pixies.utils', 
		'pixies.elements',
		'pixies.reportlab',
		'pixies.reportlab.lib',
		'pixies.reportlab.pdfbase',
		'pixies.reportlab.pdfgen',
		'pixies.reportlab.platypus'
	],
	scripts=['pixies/pixies']
)


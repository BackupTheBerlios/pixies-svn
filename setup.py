#!/usr/bin/env python

# $Id$
# $URL$

from distutils.core import setup

setup(
	name="Pixies Formatting Objects",
	version="0.2-cvs",
	description="""Pixies is a formatter that convert XSL-FO 
documents to PDF. It is written in python and it is particulary 
focused on the production of PDF files from DocBook documents.""",
	author="Matteo Merli",
	author_email="matteo.merli@gmail.com",
	url="http://merlimat.net/software/pixies",
	packages=['lib'],
	scripts=['pixies']
)


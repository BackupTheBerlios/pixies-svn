<?xml version="1.0" encoding="utf-8"?>

<!-- $Id$ -->
<!-- $URL$ -->

<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
				xmlns:fo="http://www.w3.org/1999/XSL/Format"
                version='1.0'>
  
  <xsl:output method="xml" indent="yes"/>

	<xsl:template match="collection">
	  <fo:root>
		<fo:layout-master-set>
		  
		  
		<!-- We define a simple-page-master, a description of the page that
			 we want for our report.. (note: the name 'A4' it's just a reference name, 
			 what count are the sizes)
		-->
		<fo:simple-page-master master-name="A4" page-height="29.7cm" page-width="21cm" 
								 margin-top="2cm" margin-bottom="2cm" margin-left="2cm" margin-right="2cm">
			<fo:region-body/>
		</fo:simple-page-master>
		
		<!-- Here we define a page sequence -->
		<fo:page-sequence-master master-name="my_sequence">
			<fo:repeatable-page-master-alternatives>
			  <fo:conditional-page-master-reference master-reference="A4" odd-or-even="any" />
			</fo:repeatable-page-master-alternatives>
		</fo:page-sequence-master>
		  
		</fo:layout-master-set>
		
		<!-- here starts the "real" content -->
		<fo:page-sequence master-reference="my_sequence">
		  <fo:flow flow-name="xsl-region-body">
			
			<fo:block font-family="Times" font-size="18pt" font-weight="bold">
				<xsl:value-of select="title"/>
			</fo:block>
			
			<xsl:for-each select="book">
			  
			<xsl:sort select="author" /> <!-- This tell that we want items sorted by author -->
			  
			  <fo:block font-size="12pt" font-family="sans-serif">
				<xsl:value-of select="author"/> - 
				<fo:inline font-style="italic">
					<xsl:value-of select="title"/>
				</fo:inline>
			  </fo:block>
			  
			</xsl:for-each>
			
		  </fo:flow>
		</fo:page-sequence>		
		
	  </fo:root>
	</xsl:template>
  
</xsl:stylesheet>


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
		
	</fo:layout-master-set>
		
		<!-- here starts the "real" content -->
	<fo:page-sequence master-reference="A4">
	  <fo:flow flow-name="xsl-region-body">
		
		<fo:block font-family="Times" font-size="18pt" font-weight="bold">
			<xsl:value-of select="title"/>
		</fo:block>
			
		<fo:list-block provisional-distance-between-starts="15mm" provisional-label-separation="5mm">
			<!-- font-size="12pt" font-family="sans-serif" -->

 		<xsl:for-each select="book">
				<!-- for each book in our collection print author and title -->
	<fo:list-item>
		<fo:list-item-label start-indent="5mm" end-indent="label-end()">
			<fo:block><xsl:number format="1." /></fo:block>
		</fo:list-item-label>
		
		<fo:list-item-body start-indent="body-start()">
			<fo:block>
				<xsl:value-of select="author"/> - 
				<fo:inline font-style="italic">
					<xsl:value-of select="title"/>
				</fo:inline>
			</fo:block>
		</fo:list-item-body>
	</fo:list-item>
		</xsl:for-each>

		</fo:list-block>
		
	  </fo:flow>
	</fo:page-sequence>		
		
  </fo:root>
</xsl:template>

<xsl:template match="book">
		  

	
</xsl:template>
  
</xsl:stylesheet>


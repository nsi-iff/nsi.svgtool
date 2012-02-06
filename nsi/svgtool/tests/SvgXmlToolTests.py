import unittest
from xml.dom import minidom

from nsi.svgtool.SvgXmlTool import SvgXmlTool
from nsi.svgtool.SvgTool import SvgTool

class SvgXmlToolTest(unittest.TestCase):

    def setUp(self):
        self.xmlTool = SvgXmlTool()
        self.tool = SvgTool()

    def test_copyAttrSvgTag(self):
        svg1 = minidom.parseString( '<svg a="0" b="1" c="2"/>' )
        svg2 = minidom.parseString( '<svg new="0"/>' )
        self.xmlTool.copyAttrSvgTag(svg1, svg2)
        self.assertTrue(svg2.documentElement.attributes.get('a'))
        self.assertTrue(svg2.documentElement.attributes.get('b'))
        self.assertTrue(svg2.documentElement.attributes.get('c'))
        self.assertTrue(svg1.documentElement.attributes.get('a'))
        self.assertTrue(svg1.documentElement.attributes.get('b'))
        self.assertTrue(svg1.documentElement.attributes.get('c'))

    def test_copyMetadataTag(self):
        svg1 = minidom.parseString( '<svg><metadata a="0" b="1" c="2"/></svg>' )
        svg2 = minidom.parseString( '<svg/>' )
        self.xmlTool.copyTag(svg1, svg2, 'metadata')
        self.assertTrue( svg2.documentElement.getElementsByTagName('metadata') )
        self.assertTrue( svg1.documentElement.getElementsByTagName('metadata') )

    def test_copyDefs(self):
        svg1 = minidom.parseString( '<svg><defs a="0"/></svg>')
        svg2 = minidom.parseString( '<svg/>' )
        self.xmlTool.copyTag(svg1, svg2, 'defs')
        self.assertTrue( svg2.documentElement.getElementsByTagName('defs') )
        self.assertTrue( svg1.documentElement.getElementsByTagName('defs') )          
if __name__ == '__main__':
    unittest.main()    

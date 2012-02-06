import unittest
import os
import StringIO

from nsi.svgtool.SvgFile import SvgFile
from nsi.svgtool.SvgFile import SvgStringIO
from nsi.svgtool.SvgImage import SvgImage
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')


SVG_CODE = '<?xml version="1.0" ?>\
<!-- Created with Inkscape (http://www.inkscape.org/) -->\
<svg \
height="100%" \
id="svg2" \
version="1.0" \
width="100%" \
xmlns="http://www.w3.org/2000/svg" \
xmlns:svg="http://www.w3.org/2000/svg">\n  \
<defs id="defs4">\n    \
<rect height="50" id="rectangle" \
style="fill:#0000ff" width="50" x="0" y="0"/>\n  \
</defs>\n  \
<g id="g7" transform="translate(25,25)">\n    \
<rect height="50" id="rect9" style="fill:#0000ff" width="50" x="0" y="0"/>\n  \
</g>\n  <g id="g11" transform="translate(50,50)">\n    \
<rect height="50" id="rect13" style="fill:#0000ff" width="50" x="0" y="0"/>\n  \
</g>\n  \
<g id="g15" transform="translate(75,75)">\n    \
<rect height="50" id="rect17" style="fill:#0000ff" width="50" x="0" y="0"/>\n  \
</g>\n\
</svg>'


class SvgImageTest(unittest.TestCase):

    def test_create_new_svg_image_object_with_file(self):
        content_file = SvgFile("teste.svg")
        image = SvgImage(content_file)
        assert(image._content.exists("teste.svg"))
        os.remove("/tmp/teste.svg")
        
    def test_create_new_svg_image_object_with_stringio(self):
        string_io = StringIO.StringIO("<svg><g></g></svg>")
        content_file = SvgStringIO("test",string_io)
        image = SvgImage(content_file)
        self.assertEquals("<svg><g></g></svg>",image._content.content)
     
    def test_create_generate_png(self):
        string_io = StringIO.StringIO(SVG_CODE)
        content_file = SvgStringIO("test.svg",string_io)
        image = SvgImage(content_file)
        image.toPng()
    
    def test_get_code(self):
        content_file = SvgFile("test.svg", DATA_DIR)
        image = SvgImage(content_file)
        self.assertEquals(SVG_CODE, str(image.getCode().toxml()))
        
if __name__ == '__main__':
    unittest.main()

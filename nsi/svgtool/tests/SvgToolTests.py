# -*- coding: utf-8 -*-

import unittest
import os
import StringIO

from nsi.svgtool.SvgTool import *
from nsi.svgtool.SvgXmlTool import SvgXmlTool
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')

# TODO: coments
SVG_HEAD_EXPECTED ='<?xml version="1.0" ?>\
<svg height="100%" id="svg2" version="1.0" width="100%" \
xmlns="http://www.w3.org/2000/svg" \
xmlns:svg="http://www.w3.org/2000/svg">\
<defs id="defs4">\n    \
<rect height="50" id="rectangle" style="fill:#0000ff" width="50" x="0" y="0"/>\n  \
</defs>\
</svg>'


# TODO: coments
SVG_ADD_TAG_SEQUENCE_EXPECTED = u'<?xml version="1.0" ?><svg><g id="g7" transform="translate(25,25)"><rect height="50" id="rect9" style="fill:#0000ff" width="50" x="0" y="0"/></g><g id="g15" transform="translate(75,75)"><rect height="50" id="rect17" style="fill:#0000ff" width="50" x="0" y="0"/></g></svg>'


# TODO: coments
SVG_FILE_TEST_CONTENT = '<?xml version="1.0" ?>\
<svg height="100%" \
id="svg2" \
version="1.0" \
width="100%" \
xmlns="http://www.w3.org/2000/svg" \
xmlns:svg="http://www.w3.org/2000/svg">\
<defs id="defs4">\n    \
<rect height="50" id="rectangle" style="fill:#0000ff" width="50" x="0" y="0"/>\n  \
</defs>\
<g id="g7" transform="translate(25,25)">\
<rect height="50" id="rect9" style="fill:#0000ff" width="50" x="0" y="0"/>\
</g>\
</svg>'



# TODO: coments
SVG_FILE_HORSE_CONTENT = '<?xml version=\'1.0\' encoding=\'utf-8\'?>\
<svg height="166" id="svg2" version="1.0" width="119" \
xmlns="http://www.w3.org/2000/svg" \
xmlns:svg="http://www.w3.org/2000/svg">\n\
<g id="layer1" transform="translate(-177.98486,-519.29053)">\
<path d="M 268.86607,643.55173 L 181.30715,557.23266 C 180.17536,545.99613 \
183.65804,536.81475 193.05018,530.40049 L 280.51786,616.5428 C \
277.86985,626.2324 273.64529,635.04614 268.86607,643.55173 z " \
id="path3154" style="fill:#000000;fill-opacity:1;fill-rule:evenodd;\
stroke:none;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;\
stroke-opacity:1" /><path d="M 266.05357,584.48923 L 271.23214,577.07851 L \
275.875,569.13209 C 279.2255,564.92306 283.69232,561.83035 288.375,558.95351 \
C 285.93149,553.90332 282.12801,549.70312 278.375,545.47137 C \
274.68804,542.31651 270.35292,540.4832 266.14286,538.68566 C \
262.26944,537.34992 257.30472,536.41266 255.36396,532.42079 C \
255.03044,531.58971 254.40999,530.93078 253.7856,530.27422 C \
253.07413,529.37203 252.07284,528.87558 251.07081,528.38018 C \
250.29638,528.34655 249.50339,528.27579 249.36618,529.5166 C \
250.84145,530.54967 250.74733,531.93148 251.26022,533.17841 C \
248.78177,532.99918 246.06537,528.30784 245.13617,531.47377 C \
246.37953,532.39472 247.29495,533.12939 247.39462,534.51955 C \
247.69295,536.31375 247.06338,537.61765 246.20945,538.67111 L \
241.54464,545.51601 C 241.07868,546.67997 240.43185,547.39177 \
239.80357,548.14994 C 238.61821,549.15553 238.22619,550.3478 \
237.63008,551.60593 C 236.98323,553.32518 235.95774,555.05021 \
235.07143,556.72137 C 233.74016,557.89837 232.4801,559.02131 \
231.23214,560.11423 C 230.77582,561.45352 230.66866,562.7928 \
231.05357,564.13209 C 231.71757,565.10704 232.49955,565.89322 \
233.58255,566.19777 L 236.10793,566.76598 L 237.11808,567.46046 C \
237.49627,568.30434 238.59729,568.41045 239.39093,567.93397 L \
242.68924,564.66853 C 244.14703,564.26472 245.04021,563.15828 \
246.33573,562.26765 C 246.78531,561.51385 248.02356,560.82293 \
248.70327,560.16842 C 250.3132,559.75202 251.54433,560.20226 \
253.34366,559.69491 C 255.22778,558.7062 255.7401,557.13106 \
257.88934,557.99028 C 260.79589,562.76667 263.37673,567.65163 \
265.27608,572.76376 C 266.02501,576.67225 266.14119,580.58074 \
266.05357,584.48923 z " id="path3156" style="fill:#000000;\
fill-opacity:1;\fill-rule:evenodd;stroke:none;stroke-width:1px;\
stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />\
</g>\
</svg>'



 
# TODO: coments
SVG_TAG_ADD_INTERNAL_EXPECTED = u'<?xml version="1.0" ?>\
<svg>\
<g id="g7" transform="translate(25,25)">\
<rect height="50" id="rect9" style="fill:#0000ff" width="50" x="0" y="0"/>\
</g>\
</svg>'


SVG_CODE_TEST = u'<?xml version="1.0" encoding="UTF-8" standalone="no"?>\
<!-- Created with Inkscape (http://www.inkscape.org/) -->\
<svg xmlns:svg="http://www.w3.org/2000/svg" xmlns="http://www.w3.org/2000/svg"\
   version="1.0" width="100%" height="100%" id="svg2">\
  <defs id="defs4">\n\
    <rect width="50" height="50" x="0" y="0" id="rectangle" style="fill:#0000ff"/>\n\
  </defs>\
  <g transform="translate(25,25)" id="g7">\
    <rect width="50" height="50" x="0" y="0" id="rect9" style="fill:#0000ff"/>\
  </g>\
  <g transform="translate(50,50)" id="g11">\
    <rect width="50" height="50" x="0" y="0" id="rect13" style="fill:#0000ff"/>\
  </g>\
  <g transform="translate(75,75)" id="g15">\
    <rect width="50" height="50" x="0" y="0" id="rect17" style="fill:#0000ff"/>\
  </g>\
</svg>'

class SvgBoxTest(unittest.TestCase):

    def test_point_inside_box(self):
        box = Box(Point(0,0),10,10)
        assert(box.isInside(Point(1,1)))
        assert(box.isInside(Point(1.5,5 - 1.2)))
        assert(not box.isInside(Point(15,1)))
        assert(not box.isInside(Point(1.5,18)))


class SvgToolTest(unittest.TestCase):

    def setUp(self):
        self.tool = SvgTool()
        self.xml_tool = SvgXmlTool()
                
        self.region0 = Box(Point(0,0),10,10)
        self.region1 = Box(Point(1,1),8,8)
        self.bbox0 = Box(Point(1,1),8,8)
        self.bbox1 = Box(Point(0,0),18,18)

    def test_make_new_svg_image_with_file(self):
        content_file = self.tool.makeNewSvgFile()
        assert(51, len(self.tool.makeNewSvgImage(content_file)._content.content))
        assert("noname" in os.listdir("/tmp"))
        os.remove("/tmp/noname")
        content_file = self.tool.makeNewSvgFile("testsvgtool1.svg")
        assert(51, len(self.tool.makeNewSvgImage(content_file)._content.content))
        assert("testsvgtool1.svg" in os.listdir("/tmp"))
        os.remove("/tmp/testsvgtool1.svg")
        content_file = self.tool.makeNewSvgFile("test2.svg",DATA_DIR)
        assert(51, len(content_file.content))
        assert((content_file.name) in os.listdir(content_file.directory))
        os.remove(content_file.getAbsolutePath())  

    def test_make_new_svg_image_with_string_io(self):
        content_string_io = self.tool.makeNewSvgStringIO("test.svg", StringIO.StringIO(SVG_HEAD_EXPECTED))
        assert(268, len(self.tool.makeNewSvgImage(content_string_io)._content.content))
        content_string_io = self.tool.makeNewSvgStringIO("test.svg", StringIO.StringIO(''))
        image = self.tool.makeNewSvgImage(content_string_io)
        assert(28, len(image._content.content))
        #image.toPng()

    def test_make_new_svg_file(self):
        assert(51, len(self.tool.makeNewSvgFile().content))
        assert("noname" in os.listdir("/tmp"))
        os.remove("/tmp/noname")
        assert(51, len(self.tool.makeNewSvgFile("testsvgtool1.svg").content))
        assert("testsvgtool1.svg" in os.listdir("/tmp"))
        os.remove("/tmp/testsvgtool1.svg")
        imgFile = self.tool.makeNewSvgFile("test2.svg",DATA_DIR)      
        assert(51, len(imgFile.content))
        assert((imgFile.name) in os.listdir(imgFile.directory))
        os.remove(imgFile.getAbsolutePath())
        
    def test_alter_svg_data(self):
        content_file = self.tool.makeNewSvgFile("testsvgtool.svg")
        im = self.tool.makeNewSvgImage(content_file)
        assert("testsvgtool.svg" in os.listdir("/tmp"))
        im = self.tool.alterSvgData(im, "newname.svg")
        assert("newname.svg" in os.listdir("/tmp"))
        if(not "testsvgtool" in os.listdir("/tmp")):
            os.mkdir('/tmp/testsvgtool')
            
        im = self.tool.alterSvgData(im, directory='/tmp/testsvgtool')
        assert("newname.svg" in os.listdir(im._content.directory))
        os.remove("/tmp/testsvgtool/newname.svg")
        os.rmdir("/tmp/testsvgtool")
        os.remove("/tmp/newname.svg")       
        os.remove("/tmp/testsvgtool.svg")  
        
    def test_verify_point_into_region(self):
        assert(self.tool.isBBoxInRegion(self.bbox0, self.region0))
        assert(self.tool.isBBoxInRegion(self.region0, self.region0))
        assert(not self.tool.isBBoxInRegion(self.bbox1, self.region1))


    def test_handle_tag_in_svg_file(self):
        """
        content_file = self.tool.makeNewSvgFile("test.svg",DATA_DIR)
        img = self.tool.makeNewSvgImage(content_file)
        tag_list = ["g7","rect9", "g15", "rect17"]
        self.assertEquals(["rect9", "rect17"], self.tool._SvgTool__handleTagIdList(img.getCode(), tag_list))
        """

    def test_handle_tag_in_svg_string_io(self):
        """
        content_file = self.tool.makeNewSvgStringIO("test.svg",StringIO.StringIO(SVG_CODE_TEST))
        img = self.tool.makeNewSvgImage(content_file)
        tag_list = ["g7","rect9", "g15", "rect17"]
        self.assertEquals(["rect9", "rect17"], self.tool._SvgTool__handleTagIdList(img.getCode(), tag_list))
        """

    def test_generate_bounding_box(self):
        grains = [['svg2', '25', '25', '100', '100'], \
        ['rectangle', '0', '0', '50', '50'], \
        ['g7', '25', '25', '50', '50'], \
        ['rect9', '25', '25', '50', '50'], \
        ['g11', '50', '50', '50', '50'], \
        ['rect13', '50', '50', '50', '50'], \
        ['g15', '75', '75', '50', '50'], \
        ['rect17', '75', '75', '50', '50']]
        self.assertEquals(grains, self.tool.generateBoundingBox(os.path.join(DATA_DIR, 'test.svg')))
        
        bbox = [['svg2', '39.5', '19.5', '481', '160.5'], \
        ['uprightPost', '-0.5', '-0.5', '11', '151'], \
        ['column', '11.5', '-0.5', '149', '151'], \
        ['beam', '-0.5', '-0.5', '137', '17'], \
        ['rect11', '-0.5', '-0.5', '4', '17'], \
        ['rect13', '4.5', '-0.5', '127', '9'], \
        ['rect15', '132.5', '-0.5', '4', '17'], \
        ['use17', '11.5', '-0.5', '137', '17'], \
        ['use19', '11.5', '49.5', '137', '17'], \
        ['use21', '11.5', '99.5', '137', '17'], \
        ['use23', '149.5', '-0.5', '11', '151'], \
        ['rack', '-10.5', '-0.5', '481', '160.5'], \
        ['floor', '-10.5', '149.5', '481', '10.5'], \
        ['rect27', '-10', '150', '480', '10'], \
        ['line29', '-10.5', '149.5', '481', '1'], \
        ['use31', '-0.5', '-0.5', '11', '151'], \
        ['use33', '11.5', '-0.5', '149', '151'], \
        ['use35', '161.5', '-0.5', '149', '151'], \
        ['use37', '311.5', '-0.5', '149', '151'], \
        ['use39', '39.5', '19.5', '481', '160.5']]
        self.assertEquals(bbox, self.tool.generateBoundingBox(os.path.join(DATA_DIR, 'shelves.svg')))

    def test_copy_svg_head_file(self):
        content_file = self.tool.makeNewSvgFile("test.svg",DATA_DIR)
        new_content_file = self.tool.makeNewSvgFile("new_file.svg")
        img = self.tool.makeNewSvgImage(content_file)
        new_svg = self.tool.copySvgHead(img.getCode(), self.tool.makeNewSvgImage(new_content_file).getCode())
        self.assertEquals(SVG_HEAD_EXPECTED, new_svg.toxml())
        os.remove("/tmp/new_file.svg")
        

    def test_copy_svg_head_string_io(self):
        """
        content_file = self.tool.makeNewSvgStringIO("test.svg",StringIO.StringIO(SVG_CODE_TEST))
        new_content_file = self.tool.makeNewSvgStringIO("new_file.svg", StringIO.StringIO(''))
        img = self.tool.makeNewSvgImage(content_file)
        new_svg = self.tool.copySvgHead(img.getCode(), self.tool.makeNewSvgImage(new_content_file).getCode())
        self.assertEquals(SVG_HEAD_EXPECTED, new_svg.toxml())
        """

    def test_select_grain_in_region_test(self):
        content_file = self.tool.makeNewSvgFile("test.svg",DATA_DIR)
        img = self.tool.makeNewSvgImage(content_file)
        region = Box(Point(20,20),70,70)
        new_content_file = self.tool.makeNewSvgFile("selec_test.svg")
        newSvg = SvgImage(new_content_file)        
        newSvg = self.tool.selectGrainsInRegion(region, img, newSvg)
        #self.assertEquals(['g7', 'rect9'], tagList)
        self.assertEquals(newSvg._content.content, SVG_FILE_TEST_CONTENT)
        os.remove("/tmp/selec_test.svg")

    def test_select_grain_in_region_test(self):
        """
        content_file = self.tool.makeNewSvgFile("test.svg",DATA_DIR)
        content_string_io = self.tool.makeNewSvgStringIO("test.svg", StringIO.StringIO(content_file.content))
        img = self.tool.makeNewSvgImage(content_string_io)
        region = Box(Point(20,20),70,70)
        new_content_string_io = self.tool.makeNewSvgStringIO("selec_test.svg", StringIO.StringIO(''))
        newSvg = SvgImage(new_content_string_io)        
        newSvg = self.tool.selectGrainsInRegion(region, img, newSvg)
        #self.assertEquals(['g7', 'rect9'], tagList)
        self.assertEquals(newSvg._content.content, SVG_FILE_TEST_CONTENT)
        os.remove("/tmp/selec_test.svg")
        """

    def test_select_grain_in_region_horse(self):
        content_file = self.tool.makeNewSvgFile("1_Cav_Shoulder_Insignia.svg",DATA_DIR)
        img = self.tool.makeNewSvgImage(content_file)
        region = Box(Point(0,0),130,130)
        new_content_file = self.tool.makeNewSvgFile('selec_horse.svg')
        newSvg = SvgImage(new_content_file)        
        newSvg = self.tool.selectGrainsInRegion(region, img, newSvg)
        #self.assertEquals(['path3154', 'path3156'], tag_list)
        #self.assertEquals(newSvg._file.content, SVG_FILE_HORSE_CONTENT)
        #os.remove("/tmp/selec_horse.svg")
        
        img.toPng('horse.png', '/tmp')
        newSvg.toPng()

    def test_select_grain_in_region_blason(self):
        content_file = self.tool.makeNewSvgFile("Blason_54.svg",DATA_DIR)    
        img = self.tool.makeNewSvgImage(content_file)
        region = Box(Point(120,0),460,450)
        new_content_file = self.tool.makeNewSvgFile('selec_blason.svg')        
        newSvg = SvgImage(new_content_file)
        newSvg = self.tool.selectGrainsInRegion(region, img, newSvg)
        """
        TAGS_IN_REGION = ['path3954', 'path3952', 'path3950', 'path3946', \
        'path3942', 'path3938', 'path3934', 'path3930', 'path3926', \
        'path3924', 'path3922', 'path3920', 'path3918', 'path3916', \
        'path1932', 'g5398', 'rect5400', 'path5402', 'path5404', 'path5406', \
        'path5408', 'path5410', 'path5412', 'path5414', 'path5416', \
        'path5418', 'path5420', 'path5422', 'path5424', 'path5426', \
        'path5428', 'path5430', 'path5432', 'path5434', 'path5436', \
        'path5438', 'path5440', 'path5442', 'path5444', 'path5446', \
        'path5462', 'path5464', 'path5466', 'path5468', 'path5472', \
        'path5476', 'path5480', 'path5484', 'path5488', 'path5492', \
        'path5496', 'path8232']
        """
        
        img.toPng('blason.png', '/tmp')
        newSvg.toPng()
        #self.assertEquals(TAGS_IN_REGION, tagList)
        #os.remove("/tmp/selec_blason.svg")

    def test_select_grain_in_region_heart(self):
        content_file = self.tool.makeNewSvgFile("15_Eunomia_symbol.svg",DATA_DIR)
        img = self.tool.makeNewSvgImage(content_file)
        region = Box(Point(4,150),250,260)
        new_content_file = self.tool.makeNewSvgFile('selec_heart.svg')
        newSvg = SvgImage(new_content_file)
        newSvg = self.tool.selectGrainsInRegion(region, img, newSvg)
        #self.assertEquals(['path1872'], tag_list)
        #os.remove("/tmp/selec_heart.svg")

    def test_select_grain_in_region_cat(self):
        content_file = self.tool.makeNewSvgFile("3Stormo-Patch.svg",DATA_DIR)
        img = self.tool.makeNewSvgImage(content_file)
        region = Box(Point(80,170),90,90)
        new_content_file = self.tool.makeNewSvgFile('selec_cat.svg')
        newSvg = SvgImage(new_content_file)
        newSvg = self.tool.selectGrainsInRegion(region, img, newSvg)
        #self.assertEquals(['g4297', 'path2306', 'path3291', 'path4290'], tag_list)
        #os.remove("/tmp/selec_cat.svg")

    def test_select_grain_in_region_brazil(self):
        content_file = self.tool.makeNewSvgFile("2006_Brazilian_Election_2nd_round_States.svg",DATA_DIR)
        img = self.tool.makeNewSvgImage(content_file)
        region = Box(Point(360,310),150,190)
        new_content_file = self.tool.makeNewSvgFile('selec_brazil.svg')
        newSvg = SvgImage(new_content_file)
        newSvg = self.tool.selectGrainsInRegion(region, img, newSvg)
        #self.assertEquals(['path58', 'path80'], tag_list)
        #os.remove("/tmp/selec_brasil.svg")
        
    

if __name__ == '__main__':
    unittest.main()        

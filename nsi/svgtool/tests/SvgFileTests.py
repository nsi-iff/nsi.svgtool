import unittest
import os
import StringIO

from nsi.svgtool.SvgFile import SvgFile
from nsi.svgtool.SvgFile import SvgStringIO

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')

class SvgFileTests(unittest.TestCase):

    def setUp(self):
        self._file = open("/tmp/svgfile","w")
        self._file.write("test")
        self._file.close()
        self.svgfile = SvgFile("svgfile")

    def tearDown(self):
        os.remove("/tmp/svgfile")

    def test_verify_if_file_exists_on_current_directory(self):
        svg_file = SvgFile("testsvgtool.svg")
        assert(svg_file.exists())
        assert(svg_file.exists("testsvgtool.svg"))
        os.remove("/tmp/testsvgtool.svg")

    def test_verify_if_file_exists_in_other_directory(self):
        svg_file = SvgFile("tiger.svg",DATA_DIR)
        assert(svg_file.exists("tiger.svg",DATA_DIR))

    def test_verify_nonexistent_file(self):
        assert(not self.svgfile.exists("nonexistent.svg"))
        assert(not self.svgfile.exists("nonexistent.svg",DATA_DIR))
        
    def test_get_absolute_path_of_svg_file(self):
        svg_file = SvgFile("tiger.svg",DATA_DIR)
        self.assertEquals(svg_file.getAbsolutePath(),\
                   os.path.join(svg_file.getDirectory(), svg_file.getName()))
 
    def test_alter_name_of_svg_file(self):
        svg_file = SvgFile("tiger.svg",DATA_DIR)
        self.assertEquals(svg_file.getName(),"tiger.svg")
        svg_file.name = 'tigre.svg'
        self.assertEquals(svg_file.getName(),"tigre.svg")
        
    def test_get_directory_of_svg_file(self):
        svg_file = SvgFile("tiger.svg",DATA_DIR)
        self.assertEquals(svg_file.getDirectory(),\
                          os.path.join(os.path.abspath('.'),DATA_DIR))     
    
    def test_deep_copy(self):
        f = self.svgfile.deepCopy()
        self.assertEquals("test",f.content)
        self.assertEquals(f.name, "CP_"+self.svgfile.name)
        self.assertEquals(f.directory, self.svgfile.directory)
        self.svgfile.setContent("deepcopy")
        self.assertEquals("deepcopy",self.svgfile.content)
        self.svgfile.close()
        self.assertEquals("test",f.content)
        f.close()
        os.remove("/tmp/CP_"+self.svgfile.name)

        
    def test_deep_copy_with_parameter(self):
        f = self.svgfile.deepCopy("deep")
        self.assertEquals("test",f.content)
        self.assertEquals(f.name, "deep")
        self.assertEquals(f.directory, self.svgfile.directory)
        self.svgfile.setContent("deepcopy")
        self.assertEquals("deepcopy",self.svgfile.content)
        self.svgfile.close()
        self.assertEquals("test",f.content)
        f.close()
        os.remove("/tmp/deep")

        
    def test_modify_file_name(self):
        svgfile = self.svgfile.deepCopy("name")
        self.assertEquals(4,len(self.svgfile.content))
        assert("name" in os.listdir("/tmp"))
        svgfile.name = "newname"
        self.assertEquals('newname',svgfile.name)
        assert("newname" in os.listdir("/tmp"))
        self.assertEquals(4, len(svgfile.content))
        svgfile.setContent("write")
        svgfile.save()
        self.assertEquals(5, len(svgfile.content))
        self.assertEquals(4, len(SvgFile("name").content))
        os.remove("/tmp/newname")
        os.remove("/tmp/name")

    def test_modify_file_directory(self):
        svgfile = self.svgfile.deepCopy("name.svg")
        self.assertEquals(4,len(self.svgfile.content))
        assert("name.svg" in os.listdir("/tmp"))
        if(not "testsvgtool" in os.listdir("/tmp")):
            os.mkdir('/tmp/testsvgtool')
        
        svgfile.directory = "/tmp/testsvgtool"
        self.assertEquals('/tmp/testsvgtool',svgfile.directory)
        assert("name.svg" in os.listdir(svgfile.directory))
        self.assertEquals(4, len(svgfile.content))
        svgfile.setContent("write")
        svgfile.save()
        self.assertEquals(5, len(svgfile.content))
        os.remove("/tmp/testsvgtool/name.svg")
        os.rmdir("/tmp/testsvgtool")
        os.remove("/tmp/name.svg")

class SvgStringIoTests(unittest.TestCase):

    def setUp(self):
        _file = StringIO.StringIO("test")
        self.svgstringio = SvgStringIO("io1",_file)
        
    def test_init_svg_string_io(self):
        self.assertEquals("test",self.svgstringio.content)
        
    def test_set_content(self):
        self.svgstringio.setContent("modify_content")
        self.assertEquals("modify_content",self.svgstringio.content)

if __name__ == '__main__':
    unittest.main()    

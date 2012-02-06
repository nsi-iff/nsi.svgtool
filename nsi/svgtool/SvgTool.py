# -*- coding: utf-8 -*-

#############################################################################
#                                                                           #
# Copyright (c) 2008 ISrg (NSI, CEFETCAMPOS, BRAZIL) and Contributors.      #
#                                                    All Rights Reserved.   #
#                                                                           #
# AUTHOR                                                                    # 
#       Leandro Moraes V. Cruz <lmvcruz@gmail.com>                          #
#                                                                           #
# REPORTING BUGS                                                            #
#       Report bugs to <nsi@cefetcampos.br>.                                #
#                                                                           #
# CONTRIBUTORS                                                              #
#       Hugo Lopes Tavares                                                  #
#       Gustavo Rezende                                                     #
#       Fábio Duncan                                                        #
#                                                                           #
#     WARNING: This program as such is intended to be used by professional  #
# programmers who take the whole responsability of assessing all potential  #
# consequences resulting from its eventual inadequacies and bugs            #
# End users who are looking for a ready-to-use solution with commercial     #
# garantees and support are strongly adviced to contract a Free Software    #
# Service Company                                                           #
#                                                                           #
#     This program is Free Software; you can redistribute it and/or         #
# modify it under the terms of the GNU General Public License               #
# as published by the Free Software Foundation; either version 2            #
# of the License, or (at your option) any later version.                    #
#                                                                           #
#     This program is distributed in the hope that it will be useful,       #
# but WITHOUT ANY WARRANTY; without even the implied warranty of            #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             #
# GNU General Public License for more details.                              #
#                                                                           #
#     You should have received a copy of the GNU General Public License     #
# along with this program; if not, write to the Free Software               #
# Foundation, Inc., 59 Temple Place - Suite 330, Boston,                    #
# MA  02111-1307, USA.                                                      #
#                                                                           #
#############################################################################

import os
import string

from nsi.svgtool.SvgImage import SvgImage
from nsi.svgtool.SvgXmlTool import SvgXmlTool
from nsi.svgtool.SvgFile import SvgFile
from nsi.svgtool.SvgFile import SvgStringIO

DIRECTORY_DEFAULT = "/tmp"
ACCEPT_TAG = ['svg','g','rect','circle','path','tspan','text']

class Point:

    def __init__(self, x, y):
        self._x = x
        self._y = y
        
    @property
    def x(self):
        return self._x
 
    @property
    def y(self):
        return self._y 
             
class Box:

    def __init__(self, pointOrigin, width, height):
        """
            TODO
        """
        self._pointOrigin = pointOrigin
        self._width = width
        self._height = height
        self._oppositePoint = Point(float(self._pointOrigin.x) + float(width),
                              float(self._pointOrigin.y) + float(height))

    @property
    def originX(self):
        return self._pointOrigin.x

    @property
    def originY(self):
        return self._pointOrigin.y         

    @property
    def oppositeX(self):
        return self._oppositePoint.x

    @property
    def oppositeY(self):
        return self._oppositePoint.y
    
    def isInside(self, point):
        """
            Return True if the point was inside Bounding Box
        """
        x = (float(self.originX) <= float(point.x) <= float(self.oppositeX))
        y = (float(self.originY) <= float(point.y) <= float(self.oppositeY))
        return x and y
               
               
               
class SvgTool:

    """
        TODO
    """

    def makeNewSvgImage(self, content):
        """
            Return a new svg image
        """
        image = SvgImage(content)        
        return image
    
    def makeNewSvgFile(self, filename="noname", directory="/tmp"):
        """
            Create a new svg image, so return its atribute file
        """    
        return SvgFile(filename, directory)
    
    def makeNewSvgStringIO(self, filename, content=''):
        return SvgStringIO(filename, content)
    
    def copySvgHead(self, svg_code, new_code = None):
        """
            TODO
        """
        xml_tool = SvgXmlTool()
        
        new_code = xml_tool.copyAttrSvgTag(svg_code, \
                                          new_code or self.makeNewSvgImage().getCode())
        new_code = xml_tool.copyTag( svg_code, new_code, 'defs' )
        new_code = xml_tool.copyTag( svg_code, new_code, 'metadata' )
        new_code = xml_tool.copyTag( svg_code, new_code, 'sodipodi:namedview' )
        return new_code
    
    def alterSvgData(self, image, filename = None, directory = None):
        """
            Alter SvgImage's data such filename and directory
        """
        if filename:
            image.alterDataFile(name = filename)
        if directory:
            image.alterDataFile(directory = directory)
        return image

    def __handleTagIdList(self, svg_code, tag_id_list):
        """
            This method should remove all the parent tags whose the 
            children are in tag_id_list.
            So when you have to insert a new child and the parent is not into
            the new SVG Code, the parent should be added as well.
            
            tag_id_list before handled
            ['g1','rect2']
            
            tag_id_list after handled
            ['rect2']
            
            
            Per example:
                <svg>
                  <g id='g1'> <-- Parent
                    <rect id='rect2' /> <-- Child that should be copied to the new SVG Code.
                  </g>
                </svg>
                
                New SVG Code before insertion:
                <svg>
                </svg>
                
                After insertion:
                <svg>
                  <g id='g1'>
                    <rect id='rect2' />
                  </g>
                </svg>
        """
        xml_tool = SvgXmlTool()        
        all_children = xml_tool.getAllChildren(svg_code)
        for tag in all_children:
            if (tag.tagName in ACCEPT_TAG):
                if tag.attributes.get('id').value in tag_id_list:
                    if tag.parentNode.attributes.get('id').value in tag_id_list:
                        tag_id_list.remove( tag.parentNode.attributes['id'].value )
        return tag_id_list

    def isBBoxInRegion(self, box, region):
        """
            This method verify if a box is inside region 
        """
        return region.isInside(box._pointOrigin) and \
               region.isInside(box._oppositePoint)
        
    def generateBoundingBox(self, filename):
        """
            This method return the set of Bounding Box of file, 
            whose name is passed by parameter filename

            The function "inkscape FILE --query-all" is a 
            tuple (id, x, y, w, h)
            
            For Example:
            The inkscape return 
            svg2,25,35,100,150
            
            A Tag, whose id is svg2, has origin in point (25, 35) - 
            x = 25, y = 35 - its width is 100, and height is 150.
        
            This element is splited in a list.
            
            In previous example a list retuned is:
            ['svg2', '25', '35', '100', '150']

            
            TODO: create a method to calculate bounding box of 
            SVG grains whitout inkscape
        """
        bbox_list =  os.popen("inkscape %s --query-all" %(filename))
        bbox_list = map(string.strip, bbox_list.readlines())
        return [item.split(',') for item in bbox_list]

          
    def defineTagsInRegion(self, image, region):
        """
            Return the Ids of the grains within region. If only piece of some
            tag was inside of region concerned, this tag will not considered.
        """
        grainInBB = []
        filename = image._content.getAbsolutePath()
        for line in self.generateBoundingBox(filename):
            pathBBox = line
            box = Box(Point(pathBBox[1],pathBBox[2]),pathBBox[3],pathBBox[4])
            if self.isBBoxInRegion(box, region): 
                    grainInBB.append(pathBBox[0])
        return grainInBB    
    
    def selectGrainsInRegion(self, region, image, new_image):
        """
            Return a new Image with the set of tags which were inside of
            region passed by parameter.
            
            region = {'x', 'y', 'X', 'Y'}, where x,y are the coordinate of the
            top-left vertice and X, Y are the coordinate of the bottom-right 
            vertice of the Rectangle Region define by parameter region.
        """
        tag_id_list = self.defineTagsInRegion(image, region)
        tag_id_list = self.__handleTagIdList(image.getCode(), tag_id_list)
        
        self.copySvgHead(image.getCode(), new_image.getCode())

        xml_tool = SvgXmlTool()
        xml_tool.copyListTagById(image, new_image, tag_id_list)

        new_image.saveSvgImage()        
        
        return new_image

        

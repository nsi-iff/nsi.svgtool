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

from nsi.svgtool.SvgFile import SvgFile
from nsi.svgtool.SvgXmlTool import SvgXmlTool
import os

class SvgImage(object):

    """
        A classe SvgImage implementa um tipo de media abordado por nsi.media:
        imagens SVG (Scalable Vector Graphics).
        
        Atributos:
        __file: uma instancia de um SvgFile. Essa instancia armazena estados
        e comportamentos referentes a um arquivo.
        xml_tool: instancia de um SvgXmlTool (ferramenta para manipular 
        xml - especificamente svg)
        __stringCode: codigo da imagem svg referenciada pela instancia
        __xmlCode: instancia do xml parseado e possivel de ser manipulado 
        pela classe SvgXmlTool
    """
    

    def __init__(self, content):
        """
            This method is the initiator's SvgImage. Its main responsible
            is open the svg content referenced by paramenters.
            If there is the content then open it, else create 
            a new content with basic svg content
        """
        self._content = content
        self.xml_tool = SvgXmlTool()
       
        if (len(self._content.content)==0):
            self._content.setContent(self.xml_tool.getCode(self.xml_tool.parseXml("<svg/>")))
        
        self.updateAttributes()       
         
    def getCode(self):
        """
            Return the xml code of instance (content of content)
        """
        return self.__xmlCode
    
        
    def updateAttributes(self):
        """
            Update the atributtes stringCode and xmlCode with content 
            in content, when this is modify in instance
        """
        self._stringCode = self._content.content
        self.__xmlCode = self.xml_tool.parseXml(self._stringCode)
        
        
    
    def saveSvgImage(self):
        """
            This method write the content of attribute __xmlCode in content 
            referenced by instance of SvgContent (attribute _content)
        """
        self._content.setContent(self.__xmlCode.toxml())

    def alterDataFile(self, name=None, directory=None):
        """
            TODO
        """    
        if name:
            self._content.name = name
        if directory:
            self._content.directory = directory
            
    def getFile(self):
        """
            TODO
        """    
        return self._content
        
    def getContentFile(self):
        """
            TODO
        """    
        return self._content.content
        
    def toPng(self, new_name=None, directory=None):
        """
            This method exports the content of SVG Image for PNG format.
        """
        if not directory:
            directory = self._content.directory
            
        if not new_name:
            new_name = self._content.name[:-3]+'png'
            
        path = os.path.join(directory, new_name)
        
        #print self._content.getAbsolutePath() 
        
        os.popen("inkscape %s --export-png %s" \
                  % (self._content.getAbsolutePath(), path))

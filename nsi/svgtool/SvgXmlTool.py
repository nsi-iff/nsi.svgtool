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

from xml.dom import minidom

class SvgXmlTool(object):

    """
        A Classe SvgXmlTool apresenta um conjunto de funcionalidades 
        para manipular um código de uma imagem SVG.
        
        Ela utiliza como base, para parsear e manipular codigo svg, 
        a API minidom.
        
        Os métodos apresentados podem ser utilizados em manipulação 
        de outros tipos de codigos xml, porém, pode haver necessidades 
        de extensão, pois sua implementação foi pensada para um codigo 
        SVG.
        
        A descrição das funcionalidades desenvolvidas será apresentada 
        junto ao codigo destas
    """

    def parseXml(self, svg):
        """
            TODO
        """ 
        return minidom.parseString(svg)

    def getCode(self, code):
        """
            TODO
        """        
        return code.toxml()
        
    def copyAttrSvgTag(self, svg_code, new_svg):
        """
            TODO
        """
        attrs = svg_code.documentElement.attributes
        new_attrs = new_svg.documentElement.attributes
        for attr,value in attrs.items():
            new_attrs[attr] = value
        return new_svg

    def copyTag(self, svg_code, new_code, tag_name):
        """
            This method copy all tags, whose name is passed by parameter 
            tag_name, of svg_code to a new_code.
            
            ps: this method verify if new_code has the tag that will be 
            inserted not to repeat.
        """
        doc       = svg_code.documentElement
        newdoc    = new_code.documentElement
        
        tag_list  = doc.getElementsByTagName(tag_name)
        newdoc_tag_id_list = \
              [ elem.getAttribute('id') \
                for elem in newdoc.getElementsByTagName(tag_name)]
                               
        if tag_list:
            for tag in tag_list:
                if not(tag.getAttribute('id') in newdoc_tag_id_list):
                    newchild = svg_code.importNode(tag, True)
                    newdoc.appendChild( newchild )


        return new_code
        


    def getElementNodes(self, node):
        """
            TODO
        """
        return filter( lambda child: \
                       child.nodeType == child.ELEMENT_NODE, node.childNodes )
        
    def getAllChildren(self, node):
        """
            TODO
        """
        xml_tool = SvgXmlTool()
        children = []
        for child in node.childNodes:
            if child.nodeType == child.ELEMENT_NODE:
                children.extend( self.getAllChildren(child) )
        return children + xml_tool.getElementNodes( node )
        
    
    def getElementById(self, node, tag_id):
        """
            This method return a list of elements which each one is
            the parent of the next, the last one is your desired element.
            so, from last to first are your desired element, its parent,
            the parent of its parent, and etc.
            
            Example (I want to find the "x"):
            <svg>
                <g id="v">
                    <path id="no matters"/>
                    <g id="w">
                        <path id="x"/> <!-- WANTED -->
                    </g>
                </g>
            </svg>
            so it returns a list containing [g_v, g_w, path_x].
        """
        if node.nodeType == node.ELEMENT_NODE:
            for child in node.childNodes:
                child_id = child.attributes and child.attributes.get('id')
                if child_id and child_id.value == tag_id:
                    return [child]
                else:
                    elem = self.getElementById(child, tag_id)
                    if elem:
                        return [child] + elem
                        
                        
    def copyListTagById(self, svg, new_svg, tag_id_list):
        """
            This method copy tags listed in parameter tagId
            
            Monta árvores com as listas retornadas por xml_tool.getElementById e
            adiciona cada árvore dentro do nó principal de new_svg (documentElement)
            Exemplo (tag_id_list = ['2', '4']):
            <svg>
                <g id="0">
                    <path id="nao importa"/>
                    <g id="1">
                        <path id="2"/>
                        <path id="nao importa 2"/>
                    </g>
                </g>
                <g id="3.0">
                    <g id="3">
                        <path id="4"/>
                    </g>
                </g>
            </svg>
            xml_tool.getElementById retorna uma lista de listas (uma lista de árvores)
            sendo ELEM_ID o nó xml com a tag igual a ELEM e com id igual a ID:
            [ [(g_0, g_1), (g_1, path_2)], [(g_3.0, g_3), (g_3, path_4)] ]
            uma lista de árvores, pois
            g_0 é pai de g_1 que é pai de path_2 e,
            g_3.0 é pai de g_3 que é pai de path_4.
            
            assim sendo, transforma as sublistas em árovores XML reais
            e coloca-as dentro da raiz de new_svg.
       
        """
        svg_code = svg.getCode()
        new_code = new_svg.getCode()
        list_of_trees = []


        # cria uma lista contendo listas que contém uma árvore linear (os elementos de uma arvore xml)
        for tag in tag_id_list:
            xml_tree = self.getElementById(svg_code.documentElement, tag)
            linear_tree = []
            for elem in xml_tree:
                linear_tree.append(svg_code.importNode(elem, False))
            list_of_trees.append( linear_tree )

        #
        # procura em new_svg algum elemento existente (container), se houver, adiciona dentro dele
        # o elemento desejado
        #
        for tree in list_of_trees:
            desired_elem = tree[-1]
            if self.getElementById(new_code, desired_elem.attributes['id'].value):
                continue
            for pos in range(len(tree)-1, -1, -1):
                elem = tree[pos]
                node = self.getElementById(new_code.documentElement, elem.attributes['id'].value)
                if node:
                    last = node[-1]
                    for index in range(pos+1, len(tree)):
                        last.appendChild(tree[index])
                        last = tree[index]
                    break
            else:
                last = new_code.documentElement
                for child in tree:
                    last.appendChild(child)
                    last = child

        return new_code                           

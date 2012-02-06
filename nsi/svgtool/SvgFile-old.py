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

class SvgFile(object):

    """
        A classe SvgFile implementa os metodos referentes a um arquivo.
        
        Atributos:
        __DIR: diretorio onde está armazenado o arquivo
        __NAME: nome do arquivo
        __file: o arquivo ao qual a instancia refere-se
    """

    def __init__(self, filename="noname", dir_name='/tmp'):
        """
            Create a new SvgFile, initializing the the values of self atributes
        """
        if(dir_name == '/tmp'):
            self.__DIR = dir_name
        else:
            self.__DIR = os.path.abspath(os.path.join(os.getcwd(),dir_name))
            
        self.__NAME = filename
        if self.exists():
            self.__file = open(self.getAbsolutePath(), "a+")
        else:
            self.__file = open(self.getAbsolutePath(), "w+")
            
    def exists(self, filename=None, directory=None):
        """
            Verify if exists a file, on directory passed by parameter, 
            with name same as filename.
            
        """
        return (filename or self.__NAME) in os.listdir(directory or self.__DIR)
        
    def getAbsolutePath(self):
        """
            Return the absolute path of the file referenced by instance.
        """
        return os.path.join(self.__DIR, self.__NAME)
    
    @property
    def file(self):
        return self.__file
    
    def getName(self):
        """
            Return the name of the file referenced by instance
        """
        return self.__NAME
        
    def setName(self, new_name):
        """
            Alter attribute __NAME and create new file with the new name, 
            but with equals contents
        """
        self.__NAME = new_name
        self.__file = self.deepCopy(self.__NAME, self.__DIR).__file
    
    # Property to set and get attribute name of SvgFile    
    name = property(getName, setName)

    def getDirectory(self):
        """
            Return the directory of the file referenced by instance
        """
        return self.__DIR
        
    def setDirectory(self, new_dir):
        """
            Alter attribute __DIR and create new file in other directory, 
            but with equals contents
        """
        self.__DIR = new_dir
        self.__file = self.deepCopy(self.__NAME, self.__DIR).__file

    # Property to set and get attribute directory of SvgFile 
    directory = property(getDirectory, setDirectory)

    
    def deepCopy(self, filename=None, directory=None):
        """
            Make a copy of the file with other name or in other directory.
        """
        new_file = SvgFile(filename or ("CP_" + self.__NAME), directory or self.__DIR)
        new_file.__file = open(new_file.getAbsolutePath(), "a+")
        new_file.setContent(self.getContent())
        new_file.save()
        return new_file
    
    # TODO: generalizar o metodo para retornar o conteudo de outros tipos de arquivos
    # Para generalizar este metodo será necessario utilizar algo semelhante 
    # a um strategy para decidir qual é o tipo de conteudo, e assim 
    # implementar o metodo de acordo com o conteudo.
    def getContent(self):
        """
            return the file of file (atribute self._file)
            
            ps: in this case, the file has been text
        """
        self.__file.seek(0)
        content = self.__file.read()
        self.__file.seek(0)
        return content
        
    def setContent(self, content):
        """
            Write a file in file referenced by instance
        """
        self.__file.close()
        self.__file = open(self.getAbsolutePath(), "w")
        self.__file.write(content.encode('utf-8'))
        self.__file.close()
        self.__file = open(self.getAbsolutePath(), "a+")
    
    def save(self):
        """
            Save the file already open, in atribute self._file, 
            with filename (or self._filename, if parameter filename was None)
        """
        self.setContent(self.getContent())
    
    def close(self):
        """
        """
        self.file.close()

        
class SvgStringIO(SvgFile):
    """
        A classe SvgStringIO, assim como a sua super classe SvgFile
        implementa os metodos referentes a um arquivo. Porém o conteudo
        referenciado pelo file agora é um StringIO.
    """        
    def __init__(self, content):
        self.__file = content
        
        
    def setContent(self, content):
        self.__file = StringIO.StringIO(content)
        
            
        

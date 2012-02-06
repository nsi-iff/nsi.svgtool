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
import StringIO

class SvgContent(object):
    """
        TODO
    """
    
    def __init__(self, content_name = "noname", dir_name = "/tmp"):
        """
            TODO
        """    
        self.__NAME = content_name
        
        if(dir_name == '/tmp'):
            self.__DIR = dir_name
        else:
            self.__DIR = os.path.abspath(os.path.join(os.getcwd(),dir_name))
    
    
    def getDirectory(self):
        """
            Return the directory of the file referenced by instance
        """
        return self.__DIR
        
    def setDirectory(self, dir_name):
        """
            Alter attribute __DIR and create new file in other directory, 
            but with equals contents
        """
        if(dir_name == '/tmp'):
            self.__DIR = dir_name
        else:
            self.__DIR = os.path.abspath(os.path.join(os.getcwd(),dir_name))

    # Property to set and get attribute directory of SvgFile 
    directory = property(getDirectory, setDirectory)

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
    
    # Property to set and get attribute name of SvgFile    
    name = property(getName, setName)


    def getAbsolutePath(self):
        """
            Return the absolute path of the file referenced by instance.
        """
        return os.path.join(self.__DIR, self.__NAME)
    
    @property
    def content(self):
        """
            TODO
        """
        self._content.seek(0)
        _content = self._content.read()
        
        return _content


class SvgFile(SvgContent):

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
        super(SvgFile, self).__init__(filename, dir_name)

        super(SvgFile, self).setName(filename)
        super(SvgFile, self).setDirectory(dir_name)
        
        if self.exists():
            self._content = open(super(SvgFile, self).getAbsolutePath(), "a+")
        else:
            self._content = open(super(SvgFile, self).getAbsolutePath(), "w+")

            
    def exists(self, filename=None, directory=None):
        """
            Verify if exists a file, on directory passed by parameter, 
            with name same as filename.
            
        """
        return (filename or super(SvgFile, self).name) in os.listdir(directory or self.directory)


    def setName(self, new_name):
        """
            Alter attribute __NAME and create new file with the new name, 
            but with equals contents
        """
        super(SvgFile, self).setName(new_name)
        self._content = self.deepCopy(super(SvgFile, self).name, self.directory)._content
        
    # Property to set and get attribute name of SvgFile    
    name = property(SvgContent.getName, setName)        
    
        
    def setDirectory(self, new_dir):
        """
            Alter attribute __DIR and create new file in other directory, 
            but with equals contents
        """
        super(SvgFile, self).setDirectory(new_dir)
        self._content = self.deepCopy(super(SvgFile, self).name, self.directory)._content


    # Property to set and get attribute directory of SvgFile 
    directory = property(SvgContent.getDirectory, setDirectory)

    
    def deepCopy(self, filename=None, directory=None):
        """
            Make a copy of the file with other name or in other directory.
        """
        new_file = SvgFile(filename or ("CP_" + super(SvgFile, self).name), directory or self.directory)
        new_file._content = open(new_file.getAbsolutePath(), "a+")
        new_file.setContent(self.content)
        new_file.save()
        return new_file
    
    def setContent(self, content):
        """
            Write a file in file referenced by instance
        """
        self._content.close()
        self._content = open(self.getAbsolutePath(), "w")
        self._content.write(content.encode('utf-8'))
        self._content.close()
        self._content = open(self.getAbsolutePath(), "a+")
    
    def save(self):
        """
            Save the file already open, in atribute self._file, 
            with filename (or self._filename, if parameter filename was None)
        """
        self.setContent(self.content)
    
    def close(self):
        """
            TODO
        """
        self._content.close()


        
class SvgStringIO(SvgContent):
    """
        A classe SvgStringIO, assim como a sua super classe SvgFile
        implementa os metodos referentes a um arquivo. Porém o conteudo
        referenciado pelo file agora é um StringIO.
    """
    
    def __init__(self, filename, content):
        """
            TODO
        """    
        super(SvgStringIO, self).__init__(filename)
        super(SvgStringIO, self).setName(filename)
        self._content = content
        
        self._file = SvgFile(filename)
        content.seek(0)
        c = content.read()
        #print c
        self._file.setContent(c)
        
        
    def setContent(self, content):
        """
            TODO
        """    
        self._content = StringIO.StringIO(content)
        
    """    
    def __del__(self):
        #os.remove("/tmp/"+super(SvgFile, self).name)
        print "/tmp/"+super(SvgFile, self).name
    """        

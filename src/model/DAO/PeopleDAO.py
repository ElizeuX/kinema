#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# Kinema - a GTK+/GNOME based Movies Manager.
#
# Copyright (C) 2019  Elizeu Ribeiro Sanches Xavier
#
#This file is part of Kinema.
#
#Kinema is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#Kinema is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with Kinema.  If not, see <https://www.gnu.org/licenses/>
#

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Kinema - a GTK+/GNOME based Movies Manager.
#
# Copyright (C) 2019  Elizeu Ribeiro Sanches Xavier
#
#This file is part of Kinema.
#
#Kinema is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#Kinema is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with Kinema.  If not, see <https://www.gnu.org/licenses/>
#

from src.model.People import People
from src.model.connect.DAConnectFactory import DAConexaoFactory

class PeopleDAO:

    def __init__(self):
        self.__erro = None
        self.__con = None
        self.__factory = None        
        try:
            # Cria Conexão com o Factory Method Pattern
            # Você pode ter uma classe para cada fonte de dados
            # Unimos as três fontes para o exemplo
            conexao = DAConexaoFactory()
            self.__con = conexao.getConexao(4)
            self.__factory = conexao.getFactory()                        
        except Exception as e:
            self.__erro = str(e)

    def create(self, people):    
        try:
            sql = "INSERT INTO PEOPLE (name, artisticname, born, citizenship, bio ) VALUES (\'" 
            sqlValuesList = [people.getName(), people.getArtisticname(), people.getBorn(), people.getCitizenship(), people.getBio()]            
            sqlValues = "','"
            sqlValues =  sqlValues.join(sqlValuesList)                        
            sql += sqlValues + "');"
                                
            cursor=self.__con.cursor()
            cursor.execute(sql)
            self.__con.commit()
            return True        
            
        except Exception as e:
            self.__erro = str(e)
            print(e)
            return False
    
    def read(self, people):
        raise NotImplementedError        
    
    def update(self, people):
        #  Define SQL
       sql = "UPDATE PEOPLE SET " + \
             "NAME = '" + people.getName() + "', " + \
             "CITIZENSHIP = '" + people.getCitizenship() + "'" + \
             " WHERE ID = " + str(people.getId())
 
       # Executa SQL
       try:           
            cursor=self.__con.cursor()
            cursor.execute(sql)
            self.__con.commit()
            return True
       except Exception as e:
           self.__erro = str(e)
           return False
    
    def delete(self, people):
        # Define SQL        
        sql = "DELETE FROM PEOPLE WHERE ID = " + str(people.getId()) 
         
        # Executa SQL
        try:            
            cursor=self.__con.cursor()
            cursor.execute(sql)
            self.__con.commit()
            return True
        except Exception as e:
            self.__erro = str(e)
            return False

    def addPeople(self, people):
        raise NotImplementedError   
    

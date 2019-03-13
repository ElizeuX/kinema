# coding=utf-8
# DAConexaoFactory.py

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

__author__ = 'Elizeu Xavier'

import sqlite3
 
class DAConexaoFactory():
 
 
    def __init__(self):
        self.__ORACLE = 1
        self.__DB2 = 2
        self.__MSSQL = 3
        self.__SQLite = 4
        self.__erroCon = None
        self.__factory = None
        self.__IBMDriver = None # IBM DB2 driver (ibm_db)
 
    # Cria Factory para objetos
    def getConexao(self, banco):
 
        # Define conexão e fonte de dados
        con = None
        self.__factory = banco
 
        # Cria string de conexão Oracle
        if (banco == self.__ORACLE):
            sconexao = "user/pass@localhost/XE"
            try:
                con = cx_Oracle.connect(sconexao)
            except Exception as e:
                self.__erroCon = str(e)
 
        # Cria string de conexão IBM DB2
        if (banco == self.__DB2):
            sconexao = "DATABASE=DEVA" + \
                       ";HOSTNAME=localhost;PORT=50000;PROTOCOL=TCPIP;" + \
                       "UID=user;" + \
                       "PWD=pass"
            try:
                self.__IBMDriver = ibm_db
                con = ibm_db.connect(sconexao, "", "")
            except Exception as e:
                self.__erroCon = str(e)
 
        # Cria string de conexão MSSQL
        if (banco == self.__MSSQL):
            sconexao = "MSSQLSERVER/user/pass"
            try:
                con = odbc.odbc(sconexao)
            except Exception as e:
                self.__erroCon = str(e)
                
        if (banco == self.__SQLite):
           sconexao = "C:\\Users\\ersxavier\\Videos\\Filmoteca do Kinema\\kinema.db"                        
           try:
                con = sqlite3.connect(sconexao)
           except Exception as e:
                self.__erroCon = str(e)                    
 
        return con
 
    # Retorna Erros
    def getErros(self):
        return self.__erroCon
 
    # Retorna Factory da conexão
    def getFactory(self):
        return self.__factory
 
    # Retorna Driver da IBM (Oracle e MSSQL possui outro padrão)
    def getIbmDriver(self):
        return self.__IBMDriver

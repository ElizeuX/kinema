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

import time
import os
import configparser
from pathlib import Path
from utils import utils
from view.mainUI import MainUI
from view.splash import Splash 

# import controller.kinemaapp as app

home = str(Path.home()) 

# mostrar a splash screen
print ("Mostrar tela splash screeen.")

# ler o arquivo de configuração na pasta oculta
print ("lendo o arquivo de configuração na pasta oculta do sistema.")

config = configparser.ConfigParser()
config.sections() 
config.read(home + "//kinema.conf")
dirLibrary = config['PATH']['kinema_library']
theDir = home + dirLibrary

print(theDir)

# verificar se existe o diretório da biblioteca de filmes
# caso não exista , criar diretório.
# verificar se existe banco de dados e checar integridade
# se não existir, criar, se o banco de dados estiver corrompido 
# perguntar se quer reparar.
print ("Verificando se existe diretório")
if utils.ValidateDirectory(theDir) == None:
    utils.CreateDirectory(theDir)

if os.path.exists(theDir + '\\kinema.db'):
    print("verificar banco de dados.")
    print("Conferir se os diretórios batem com os diretores e se os filmes batem com os arquivos")
else:
    utils.CreateNewDataBaseSQLite(theDir, '\\kinema.db')

# verificar plugins instalados
print ("Verificando plugins.")
#thePath = config['PATH']['plugins_dir']

#utils.WalkPath(thePath)

print("Gravando o arquivo")


# esconder a splash screen
print("esconder splash screeen")


# iniciar a aplicação
#app.main()
print("iniciando a aplicação.")

MainUI()


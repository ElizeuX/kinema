#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Kinema - a GTK+/GNOME based Movies Manager.
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

from utils import utils

utils.check_version_info()

import os
import sys
import configparser
from pathlib import Path
from model.Options import Options

from view.mainUI import MainUI
from view.main2UI import Application
from view.splash import Splash 

splash = Splash()
splash.start()

# import controller.kinemaapp as app

home = str(Path.home()) 
options = Options.instance()

data = utils.ReadJson(os.path.join(home, ".kinema.json"))

# carregar os dados do kinema.json para a classe options
options = Options.instance()
options.localOfLibrary = data['PATH']['kinema_library']
options.pluginsDir = data['PATH']['plugins_dir']
options.databaseName = data['DB']['database_name']


try:
    theDirLibrary = options.localOfLibrary
    theDatabase = os.path.join(theDir, options.databaseName)
    thePathPlugins = options.pluginsDir        
    
    if utils.ValidateDirectory(theDirLibrary) == None:
        utils.CreateDirectory(theDirLibrary)

    if os.path.exists(theDatabase):
        print("verificar banco de dados.")
        print("Conferir se os diretórios batem com os diretores e se os filmes batem com os arquivos")    
        utils.executeDataBaseVacuum(theDatabase)
    else:
        utils.CreateNewDataBaseSQLite(theDatabase)    

    utils.WalkPath(thePathPlugins)
except Exception as e:
    pass

# Destroy splash
splash.destroy()

app = Application()
app.run(sys.argv)

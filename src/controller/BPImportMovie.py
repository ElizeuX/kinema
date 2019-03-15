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

import os
from utils import utils 
from model.Movie import Movie
from model.DAO.MovieDAO import MovieDAO

#
# Controladora da tela de importação de filmes
#
class ImportMovie:

    def __init__(self, theFile):
        metainfo = utils.ExtractMetaInfoDictionary(theFile)
        self.__theFile = theFile
        self.__title = metainfo['title']
        self.__year =  metainfo['year']   
        self.__director = metainfo['director']
        self.__writer = metainfo['writer']
    
    def getMetadata(self, keyword):
        listIMDB = utils.GetInformationsIMDB(keyword)
        listMovieDatabase= utils.GetInformationsMovieDatabase(keyword)
        listaGeral = listIMDB + listMovieDatabase


        # listar fonte|title|director|ano

    def importMovieToLibrary(self, pmovie):        
        
        movie = pmovie

        theDirLybraryKinema = "C:\\Users\\ersxavier\\Videos\\Filmoteca do Kinema"
        theDir = os.path.join(theDirLybraryKinema, self.__director)

        if not utils.ValidateDirectoryWritable(theDir):
            utils.CreateDirectory(theDir)
        
        theDir = os.path.join(theDir, self.__title) 

        if not utils.ValidateDirectoryWritable(theDir):
            utils.CreateDirectory(theDir)
        # IMPORTAR FILME PARA BIBLIOTECA
        # COPIAR PARA PASTA
        # utils.copyFileToKinemaLibrary(self.__theFile, theDir)       

        # ATUALIZAR BANCO DE DADOS
        movieDAO = MovieDAO()        
        movieDAO.addMovie(pmovie)

        # BAIXAR E COPIAR COVER.JPG
        data = utils.downloadFile(pmovie.getPoster())
        
        # como pegar a extensão do arquivo ou tipo
        #with open(os.path.join(theDir,"COVER", "wb") as code:
        #    code.write(data)



        # GERAR XML
        utils.gerar_xml(pmovie.__dict__, os.path.join(theDir, movie.getTitleMovie() + ".xml"))

    def view(self):
        print(self.__title)
    
    

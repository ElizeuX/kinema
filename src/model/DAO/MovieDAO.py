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

#TODO: incluir campo data de cadastro

from src.model.Movie import Movie
from src.model.connect.DAConnectFactory import DAConexaoFactory


class MovieDAO():
     
    # Construtor da classe
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
 
    # Metodo de Manipulação de dados
      
    def getMovie(self, id):
        
        movie = Movie()         
        sql = "SELECT * FROM MOVIE WHERE ID = " + str(id)         
        try:
                cursor= self.__con.cursor()
                cursor.execute(sql)
                date = cursor.fetchone() 
                movie.setTitleMovie(date[MovieEnum.title])
                movie.setYear(date[MovieEnum.year]) 
                movie.setRated(date[MovieEnum.rated])

        except Exception as e:
            self.__erro = str(e)
 
        # Alimenta objeto        
        # Ex. genre.setId(date[0])
        
        
 
        # Retorna Objeto
        return movie
 
    def addMovie(self, movie):
       
        try:             
            sql = "INSERT INTO MOVIE (title, year, rated, released, runtime, plot, country, poster, metascore, imdbRating, imdbVotes, imdbId, typeId, certificated, file, isComplete, isPrivate) VALUES (\'" 
            sqlValuesList = [movie.getTitleMovie(), movie.getYear(), movie.getRated(), movie.getReleased(), movie.getRuntime(), movie.getPlot(), movie.getCountry(), movie.getPoster(), movie.getMetascore(), movie.getImdbRating(), movie.getImdbVotes(), movie.getImdbId(), movie.getTypeId(), movie.getCertificated(), movie.getFileAddress(), movie.getIsComplete(), movie.getIsPrivate()]            
            sqlValues = "','"
            sqlValues =  sqlValues.join(sqlValuesList)            
            #sql +=  self.replace_right(sqlValues, ",'", ")", 1)
            sql += sqlValues + "');"
        
            cursor=self.__con.cursor()
            cursor.execute(sql)
            self.__con.commit()
            return True        
 
        except Exception as e:
            self.__erro = str(e)
            print(e)
            return False
 
    def updateMovie(self, movie): 
       #  Define SQL
       sql = "UPDATE MOVIE SET " + \
             "YEAR = '" + movie.getYear() + "', " + \
             "TITLE = '" + movie.getTitleMovie() + "'" + \
             " WHERE ID = " + str(movie.getMovieId())
 
       # Executa SQL
       try:           
            cursor=self.__con.cursor()
            cursor.execute(sql)
            self.__con.commit()
            return True
       except Exception as e:
           self.__erro = str(e)
           return False
 
    def deleteMovie(self, movie):
 
        # Define SQL        
        sql = "DELETE FROM MOVIE WHERE ID = " + str(movie.getMovieId()) 
         
        # Executa SQL
        try:            
            cursor=self.__con.cursor()
            cursor.execute(sql)
            self.__con.commit()
            return True
        except Exception as e:
            self.__erro = str(e)
            return False

    def listAllMovie(self):
        listAll = []
        movie = Movie()         
        sql = "SELECT * FROM MOVIE" 

        try:       
            cursor= self.__con.cursor()
            cursor.execute(sql)
            for row in cursor.fetchall():
                id, title, year, rated, released, runtime, plot, language, country, awards, poster, metascore, imdbRating, imdbVotes, imdbID, typeID, certificated, file, iscomplete, isprivate = row                
                movie.setMovieId(id)
                movie.setTitleMovie(title)
                movie.setYear(year)
                movie.setRated(rated)
                movie.setReleased(released)
                movie.setRuntime(runtime)
                movie.setPlot(plot)
                movie.setLanguage(language) 
                movie.setCountry(country)
                movie.setAwards(awards)     
                movie.setPoster(poster)
                movie.setMetascore(metascore)
                movie.setImdbRating(imdbRating)
                movie.setImdbVotes(imdbVotes)
                movie.setImdbId(imdbID)
                movie.setTypeId(typeID)
                movie.setCertificated(certificated)
                movie.setFileAddress(file)
                movie.setIsComplete(iscomplete)
                movie.setIsPrivate(isprivate)                
                listAll.append(movie)
                movie = object.__new__(Movie)
            
        except Exception as e:
            self.__erro = str(e)
            return None 
        
        return listAll

    def replace_right(self, source, target, replacement, replacements=None):
        return replacement.join(source.rsplit(target, replacements))

    # Retorna Erro
    def getErro(self):
        return self.__erro

from enum import IntEnum
class MovieEnum(IntEnum):
    title = 1
    year = 2
    rated = 3


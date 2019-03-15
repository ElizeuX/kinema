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

class Movie:
    

    def __init__(self):
        self.__movieId = ""
        self.__titleMovie = ""
        self.__year = ""
        self.__rated = ""
        self.__released	= ""
        self.__runtime = ""
        self.__plot = ""
        self.__country = ""	    
        self.__poster = ""
        self.__metascore = ""
        self.__imdbRating = ""
        self.__imdbVotes = ""
        self.__imdbId = ""
        self.__typeId = ""
        self.__certificated = ""
        self.__fileAddress = ""
        self.__isComplete = ""
        self.__isPrivate = ""

    def getMovieId(self):
        return self.__movieId

    def setMovieId(self, movieId):
        self.__movie_id = movieId 
        
    def getTitleMovie(self):
        return self.__titleMovie

    def setTitleMovie(self, titleMovie):
        self.__titleMovie = titleMovie

    def getYear(self):
        return self.__year

    def setYear(self, year):
        self.__year = year

    def getRated(self):
        return self.__rated

    def setRated(self, rated):
        self.__rated = rated

    def getReleased(self):
        return self.__released

    def setReleased(self, released):
        self.__released = released

    def getRuntime(self):
        return self.__runtime 

    def setRuntime(self, runtime):
        self.__runtime = runtime

    def getPlot(self):
        return self.__plot

    def setPlot(self, plot):
        self.__plot = plot

    def getCountry(self):
        return self.__country

    def setCountry(self, country):
        self.__country = country

    def getPoster(self):
        return self.__poster

    def setPoster(self, poster):
        self.__poster = poster

    def getMetascore(self):
        return self.__metascore

    def setMetascore(self, metascore):
        self.__metascore = metascore

    def getImdbRating(self):
        return self.__imdbRating

    def setImdbRating(self, imdbRating):
        self.__imdbRating = imdbRating

    def getImdbVotes(self):
        return self.__imdbVotes

    def setImdbVotes(self, imdbVotes):
        self.__imdbVotes = imdbVotes

    def getImdbId(self):
        return self.__imdbId

    def setImdbId(self, imdbId):
        self.__imdbId = imdbId

    def getTypeId(self):
        return self.__typeId

    def setTypeId(self, typeId):
        self.__typeId = typeId

    def getCertificated(self):
        return self.__certificated

    def setCertificated(self, certificated):
        self.__certificated = certificated

    def getFileAddress(self):
        return self.__fileAddress

    def setFileAddress(self, fileAddress):
        self.__fileAddress = fileAddress

    def getIsComplete(self):
        return self.__isComplete

    def setIsComplete(self, isComplete):
        self.__isComplete = isComplete

    def getIsPrivate(self):
        return self.__isPrivate

    def setIsPrivate(self, isPrivate):
        self.__isPrivate = isPrivate   
    

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

class People:

    objects = []

    def __init__(self):
        self.__id = ""
        self.__name = ""
        self.__artisticname =""
        self.__born = ""
        self.__citizenship = ""
        self.__bio = ""
        self.__objects = []
    
    def getId(self):
        return self.__id
    
    def setId(self, id):
        self.__id = id

    def getName(self):
        return self.__name
    
    def setName(self, name):
        self.__name = name
    
    def getArtisticname(self):
        return self.__artisticname
    
    def setArtisticname(self, artisticname):
        self.__artisticname = artisticname
    
    def getBorn(self):
        return self.__born
    
    def setBorn(self, born):
        self.__born = born
    
    def getCitizenship(self):
        return self.__citizenship
    
    def setCitizenship(self, citizenship):
        self.__citizenship = citizenship
    
    def getBio(self):
        return self.__bio
    
    def setBio(self, bio):
        self.__bio = bio

    def add(self):                
        self.__class__.objects.append(self)
        self = object.__new__(People)
    
    def save(self):
        print("Salvando pessoas")







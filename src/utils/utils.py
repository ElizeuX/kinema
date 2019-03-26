#!/usr/bin/env python3
# vim:fileencoding=utf-8
import os

__license__ = 'GPL v3'
__copyright__ = '2019, Elizeu Xavier <elizeu.xavier at gmail.comt>'

# This file is part of Kinema.

# Kinema is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Kinema is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Kinema.  If not, see <https://www.gnu.org/licenses/>.

#!/usr/bin/env python3
# vim:fileencoding=utf-8

import os
import configparser
import sqlite3
import shutil
import xml.etree.cElementTree as ET
import urllib.request, urllib.parse, urllib.error

__license__ = 'GPL v3'
__copyright__ = '2019, Elizeu Xavier <elizeu.xavier at gmail.comt>'

class structMovieResponse:  
    titleMovie = ""
    year = ""
    imdbId = ""
    

def ValidateDirectoryWritable(theDir):

    # Validate the path is a directory
    if not os.path.isdir(theDir):
        return None

    # Validate the path is writable
    if os.access(theDir, os.W_OK):
        return theDir
    else:
        raise RuntimeError('Directory is not writablee') from EnvironmentError

def ValidateDirectory(theDir):

    # Validate the path is a directory
    if not os.path.isdir(theDir):
        return None

    # Validate the path is readable
    if os.access(theDir, os.R_OK):
        return theDir
    else:
        raise argparse.ArgumentTypeError('Directory is not readable')

def CreateDirectory(theDir):
    #verificar se o diretório não existe
    try:
        if not os.path.isdir(theDir):
            os.makedirs(theDir)
        return True
    except expression as identifier:
        raise RuntimeError('Erro') from error
        
def GetParam(section, key):
    config = configparser.ConfigParser()
    config.sections() 
    config.read("C:\\Desenvolvimento\\pyForensic\\Teste\\src\\kinema.conf")
    theDir = config['PATH']['kinema_library']
        
def HashFile(theFile, simpleName, o_result):
    
    # Verify that the path is valid
    if os.path.exists(theFile):

        #Verify that the path is not a symbolic link
        if not os.path.islink(theFile):

            #Verify that the file is real
            if os.path.isfile(theFile):

                try:
                    #Attempt to open the file
                    f = open(theFile, 'rb')
                except IOError:
                    #if open fails report the error
                    log.warning('Open Failed: ' + theFile)
                    return
                else:
                    try:
                        # Attempt to read the file
                        rd = f.read()
                    except IOError:
                        # if read fails, then close the file and report error
                        f.close()
                        log.warning('Read Failed: ' + theFile)
                        return
                    else:
                        #success the file is open and we can read from it
                        #lets query the file stats

                        theFileStats =  os.stat(theFile)
                        (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(theFile)

                        #Print the simple file name
                        DisplayMessage("Processing File: " + theFile)

                        # print the size of the file in Bytes
                        fileSize = str(size)

                        #print MAC Times
                        modifiedTime = time.ctime(mtime)
                        accessTime = time.ctime(atime)
                        createdTime = time.ctime(ctime)
                        
                        ownerID = str(uid)
                        groupID = str(gid)
                        fileMode = bin(mode)

                        #process the file hashes

                        
                        #Calcuation and Print the MD5
                        hash = hashlib.md5()
                        hash.update(rd)
                        hexMD5 = hash.hexdigest()
                        hashValue = hexMD5.upper()
                        
                        #File processing completed
                        #Close the Active File
                        print ("================================")
                        f.close()
                        
                        # write one row to the output file                                                
                        
                        
                        return hashValue
            else:
                log.warning('[' + repr(simpleName) + ', Skipped NOT a File' + ']')
                return False
        else:
            log.warning('[' + repr(simpleName) + ', Skipped Link NOT a File' + ']')
            return False
    else:
            log.warning('[' + repr(simpleName) + ', Path does NOT exist' + ']')        
    return False

def CreateNewDataBaseSQLite( theDir, theNameNewDataBase ):
    conn = None
    tableGenre = "CREATE TABLE genre( id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,  name VARCHAR (20) NOT NULL);"
    tableCast = """CREATE TABLE [cast] (
                                        idmovie  BIGINT       REFERENCES movie (id) NOT NULL,
                                        idpeople BIGINT       REFERENCES people (id) NOT NULL,
                                        role     VARCHAR (30) NOT NULL
                                    );"""
    tableMovie = """CREATE TABLE movie (
                                        id          INTEGER        PRIMARY KEY AUTOINCREMENT
                                                                    UNIQUE
                                                                    NOT NULL,
                                        title       VARCHAR (255)  NOT NULL,
                                        year        INTEGER (4),
                                        rated		CHAR(2),
                                        released	DATE,
                                        runtime		DOUBLE (5, 2),
                                        plot		VARCHAR2(5000),
                                        language	INT(4),
                                        country		BIGINT,
                                        awards		BIGINT,
                                        poster		VARCHAR2(256),
                                        metascore	INT(2),
                                        imdbRating  DOUBLE (5, 2),
                                        imdbVotes   INT (8),
                                        imdbID		VARCHAR2(9),
                                        typeID		BIGINT,
                                        certificated INT (2),	
                                        file         VARCHAR (255),
                                        iscomplete   BOOLEAN,    
                                        isprivate    BOOLEAN
                                    );"""

    tableMovieGenre = """CREATE TABLE movie_genre (
                                                    idMovie BIGINT REFERENCES movie (id) 
                                                                NOT NULL,
                                                    idGenre BIGINT REFERENCES genre (id) 
                                                );"""

    tableMovieRole = """CREATE TABLE movie_role (
                                                    idmovie BIGINT REFERENCES movie (id),
                                                    idrole  BIGINT REFERENCES roles (id) 
                                                );"""
    tablePeople = """CREATE TABLE people (
                                            id           INTEGER        PRIMARY KEY AUTOINCREMENT
                                                                        UNIQUE,
                                            name         VARCHAR (100),
                                            artisticname VARCHAR (30),
                                            born         DATE,
                                            local        VARCHAR (50),
                                            citizenship  VARCHAR (30),
                                            bio          VARCHAR (1000) 
                                        );"""

    tableRole = """CREATE TABLE role (
                                        id   INTEGER      PRIMARY KEY AUTOINCREMENT
                                                        UNIQUE
                                                        NOT NULL,
                                        name VARCHAR (20) NOT NULL
                                    );"""

    



    try:
        conn = sqlite3.connect(theDir + theNameNewDataBase) 
        CreateTable(conn, tableGenre)
        CreateTable(conn, tableCast)
        CreateTable(conn, tableMovie)
        CreateTable(conn, tableMovieGenre)
        CreateTable(conn, tableMovieRole)
        CreateTable(conn, tablePeople)
        CreateTable(conn, tableRole)

    except Exception as e:
        print(e)
    finally:
        conn.close()

def CreateTable(conn, strDDL):        
        # Executa SQL
        try:             
            cursor= conn.cursor()
            cursor.execute(strDDL)
            conn.commit()
            return True        
 
        except Exception as e:
            erro = str(e)
            print(e)
            return False

def WalkPath(thePath):
    
    processCount = 0
    errorCount = 0

    for root, dirs, files in os.walk(thePath):

        # for each file obtain the filename and call the HashFile Function
        for file in files:
            fname = os.path.join(root, file)
            print(fname)
        
    return(processCount)

def ExtractMetaInfoDictionary(theFile):

    #dicionário com metadata
    metadata = {
		"title" : "Roma" ,
		"cast" : "Colin Farrell, Rachel Weisz, Jessica Barden",
		"year" : 2018,
		"genre" : "Comedy, Drama, Romance",
		"director" : "Alfonso Cuarón",
		"writer" : "Alfonso Cuarón"
	}
    return metadata

def GetInformationsIMDB(keyword):

    listaDeFilmes =[]
    #get_keyword(keyword, results=5)
    movieResponse = structMovieResponse()
    movieResponse.imdbId = 'tt3464902'
    movieResponse.titleMovie = 'The Lobster'
    movieResponse.year = '2015'
    listaDeFilmes.append(movieResponse)

    movieResponse = object.__new__(structMovieResponse)
    movieResponse = structMovieResponse()
    movieResponse.imdbId = 'tt6155172'
    movieResponse.titleMovie = 'Roma'
    movieResponse.year = '2018'
    listaDeFilmes.append(movieResponse)


    # retornar lista com os ids do IMDB, títulos do filme, Ano.
    return [listaDeFilmes]

def GetFullInformationsIMDB(movieID):
    
    # get_movie(movieID)
    #dicionário com metadata
    metadata = {
		"title" : "The Lobster" ,
		"cast" : "Colin Farrell, Rachel Weisz, Jessica Barden",
		"year" : 2015,
		"genre" : "Comedy, Drama, Romance",
		"director" : "Yorgos Lanthimos",
		"writer" : "Yorgos Lanthimos, Efthymis Filippou"
	}
    return metadata

def GetInformationsMovieDatabase(keyword):

    listaDeFilmes =[]
    #get_keyword(keyword, results=5)
    movieResponse = structMovieResponse()
    movieResponse.imdbId = 'tt3464902'
    movieResponse.titleMovie = 'The Lobster'
    movieResponse.year = '2015'
    listaDeFilmes.append(movieResponse)

    movieResponse = object.__new__(structMovieResponse)
    movieResponse = structMovieResponse()
    movieResponse.imdbId = 'tt6155172'
    movieResponse.titleMovie = 'Roma'
    movieResponse.year = '2018'
    listaDeFilmes.append(movieResponse)

    # # retornar lista com os ids do IMDB, títulos do filme, Ano.
    return []

def GetFullInformationsMovieDatabase(idMovie):    
    
    #dicionário com metadata
    metadata = {
		"title" : "The Lobster" ,
		"cast" : "Colin Farrell, Rachel Weisz, Jessica Barden",
		"year" : 2015,
		"genre" : "Comedy, Drama, Romance",
		"director" : "Yorgos Lanthimos",
		"writer" : "Yorgos Lanthimos, Efthymis Filippou"
	}
    return metadata

def moveFileToKinemaLibrary(theFile):

    # obter o endereço da biblioteca kinema
    theDirLybraryKinema = "C:/Users/ersxavier/Videos/Filmoteca do Kinema"
    shutil.move(theFile, os.path.join(theDirLybraryKinema,'dir'))

def copyFileToKinemaLibrary(theFile, theDir):          
    shutil.copyfile(theFile, theDir)

def gerar_xml(theMovie, theDir):    
    # x = di['Julio']
    titleMovie =  str(theMovie['_Movie__titleMovie'])
    

    lista = ET.Element("root", response = "True")
    no_movie = ET.SubElement(lista, "movie", title = theMovie['_Movie__titleMovie'], year = theMovie['_Movie__year'], rated = theMovie['_Movie__rated'], released=theMovie['_Movie__released'], runtime=theMovie['_Movie__runtime'], genre="a, b, c", director="a, b, c", writer="a, b, c", actors="a, b, c", plot=theMovie['_Movie__plot'], language="Inglês", country=theMovie['_Movie__country'], awards="Prêmios", poster=theMovie['_Movie__poster'], metascore=theMovie['_Movie__metascore'], imdbRating=theMovie['_Movie__imdbRating'], imdbVotes=theMovie['_Movie__imdbVotes'], imdbID=theMovie['_Movie__imdbId'], type=theMovie['_Movie__typeId'])
    arquivo = ET.ElementTree(lista)        
    arquivo.write(theDir, encoding='utf-8', xml_declaration=True)

    #_Movie__movieId = ""
    #_Movie__titleMovie = ""
    #_Movie__year = ""      
    #_Movie__certificated = ""
    #_Movie__fileAddress = ""
    #_Movie__isComplete = ""
    #_Movie__isPrivate = ""

def downloadFile(theURL):
    
    #url = 'https://m.media-amazon.com/images/M/MV5BNDQ1NDE5NzQ1NF5BMl5BanBnXkFtZTgwNzA5OTM2NTE@._V1_SX300.jpg'
    f = urllib.request.urlopen(url)

    data = f.read()
    return data

def ReadMarkDown(theFile):
    #f = open(theFile, 'r')
    #htmlmarkdown=markdown.markdown( f.read() )
    pass

def ReadJson(theFile):
    import json
    data = None

    try:
        with open(theFile) as f:
            data = json.load(f)
    except Exception as e:
        raise("Não foi possível ler arquivo JSON: %s", theFile)

    finally:
        return data

def WriteJson(theDict, theFile):
    import json

    try:
        with open(theFile, 'w') as json_file:
            json.dump(theDict,json_file, indent=4, sort_keys=True)
        return True

    except:
        raise("Não foi possível escrever arquivo JSON: %s", theFile)
        return False        



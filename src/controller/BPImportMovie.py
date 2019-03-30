import os
from utils import utils 
from model.Movie import Movie
from model.People import People

from model.DAO.MovieDAO import MovieDAO

from model.DAO.PeopleDAO import PeopleDAO
from model.Options import Options


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
        self.__genre = metainfo['genre']
        self.__cast = metainfo['cast']
    
    def getMetadata(self, keyword):
        listIMDB = utils.GetInformationsIMDB(keyword)
        listMovieDatabase= utils.GetInformationsMovieDatabase(keyword)
        listaGeral = listIMDB + listMovieDatabase
        return utils.GetFullInformationsIMDB(1)


        # listar fonte|title|director|ano

    def importMovieToLibrary(self, pmovie):        
        
        cast_list = self.__cast.split(',')
        director_list = self.__director.split(',')
        writer_list = self.__writer.split(',')

        # incluir Actors
        self.IncludePeople(cast_list)

        # incluir director
        self.IncludePeople(director_list)

        # incluir writer
        self.IncludePeople(writer_list)

        options = Options.instance()
        theDirLybraryKinema = options.localOfLibrary 

        # SENÃO EXISTIR, CRIAR DIRETORIO COM O NOME DO DIRETOR
        theDir = os.path.join(theDirLybraryKinema, self.__director)
        if not utils.ValidateDirectoryWritable(theDir):
            utils.CreateDirectory(theDir)
        
        # SENÃO EXISTIR, CRIAR DIRETORIO COM O NOME DO FILME
        theDir = os.path.join(theDir, self.__title) 
        if not utils.ValidateDirectoryWritable(theDir):
            utils.CreateDirectory(theDir)

        # CRIAR UM ARQUIVO JSON COM OS METADADOS DO FILME
        utils.createTheMovieJSONInfo(theDir, pmovie)
        
        # COPIAR FILME PARA PASTA DIRETOR/FILME
        # utils.copyFileToKinemaLibrary(self.__theFile, theDir)       

        # ATUALIZAR BANCO DE DADOS DE FILME       
        movieDAO = MovieDAO()        
        movieDAO.addMovie(pmovie)

        # BAIXAR E COPIAR COVER.JPG
        data = utils.downloadFile(pmovie.getPoster())
        #with open(os.path.join(theDir,"COVER", "wb") as code:
        #    code.write(data)    

    def view(self):
        print(self.__title)
    
    
    def IncludePeople(self, listOfPeople):
        # incluir Actors
        peopleDAO = PeopleDAO()                
        people = People()
        peopleList = []
        
        for actor in listOfPeople:
            people.setArtisticname(actor.strip(" "))
            peopleList.append(people)
            people = People()

        # cadastre se o artista não estiver cadastrado
        for item in peopleList:
            if peopleDAO.read(item).getId() != '':
               # associo 
               pass
            else:
                peopleDAO.create(item)
        #--------------------------------------

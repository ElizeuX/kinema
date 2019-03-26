class Options:
    __instance = None
 
    @property
    def localOfLibrary(self):
        return self.__localOfLibrary
 
    @localOfLibrary.setter
    def localOfLibrary(self, value):
        self.__localOfLibrary = value
    
    @property
    def pluginsDir(self):
        return self.__pluginsDir
 
    @pluginsDir.setter
    def pluginsDir(self, value):
        self.__pluginsDir = value    

    @property
    def databaseName(self):
        return self.__databaseName
 
    @databaseName.setter
    def databaseName(self, value):
        self.__databaseName = value    
 
    @staticmethod
    def instance():
        if not Options.__instance:
            Options.__instance = Options()
        return Options.__instance

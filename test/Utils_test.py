from unittest import TestCase
from src.utils import utils

class TestUtils(TestCase):
    
    # Serve para incializar variavei que usaremos
    # globalmente nos testes
    def setUp(self):
        TestCase.setUp(self)
        self.util = utils
    
    # Retorna uma NotImplementedError
    # O nome do metodo deve comecar com test
    def test_readjson(self):  
        import json                      
        
        data = self.util.ReadJson("C:\Desenvolvimento\kinema\kinema.json")
        
        
        print (json.dumps(data))
        assert(data['DB']['database_name'] == 'kinema.db')
        assert(not data['DB']['cipher'])
        assert(data['PATH']['kinema_library'] == "C:\\Users\\ersxavier\\Videos\\Filmoteca do Kinema")
        assert(data['PATH']['plugins_dir'] == "C:\\Desenvolvimento\\kinema\\src\\plugin")
    
    def test_writejson(self):

        import json
        
        kinema_dict = {
                        "DB": {
                                "database_name": "kinema.db",
                                "cipher": False
                              },
        
                        "PATH": {
                                    "kinema_library" : "C:\\Users\\ersxavier\\Videos\\Filmoteca do Kinema",
                                    "plugins_dir" : "C:\\Desenvolvimento\\kinema\\src\\plugin"            
                                }
                        }
        
        assert(self.util.WriteJson(kinema_dict, "C:\\Users\\ersxavier\\.kinema.json"))

    




#from controllers.main_controller import *
from database.database import PermisosDb
db = PermisosDb()

class Permisos:
    def __init__ (self):
        self._row = []	  
    
    def mecanico_vista(self,main):
        self._row = db.leer(1)
        if self._row[1] is False:
            main.pushButton_7.hide()
        
        if self._row[2] is False:
            main.pushButton_13.hide()
        
        if self._row[3] is False:
            main.pushButton_4.hide()
        
        if self._row[4] is False:
            main.pushButton_6.hide()
        
        if self._row[5] is False:
            main.pushButton.hide()
        
        # if self._row[6] is False:
        #     main.pushButton_3.hide()
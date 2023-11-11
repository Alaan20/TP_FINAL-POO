#from controllers.main_controller import *
from database.database import PermisosDb
db = PermisosDb()
class VistaMecanico:
    def __init__(self):
        self._row = None
        
    def mostrar_vista(self,main):
        self._row = db.leer(1)
        
        if self._row[0][1] is False: #editar usurio
            main.pushButton_7.hide()
        
        if self._row[0][2] is False: # Eliminar usuario
            main.pushButton_13.hide()
        
        if self._row[0][3] is False: # añadir usuario
            main.pushButton_4.hide()
        
        # if self._row[4] is False: # añadir mecanic
        #     main.pushButton_6.hide()
        
        if self._row[0][4] is False: # gestion de claves
            main.pushButton.hide()
        
        if self._row[0][5] is False: # listado de mecanicos
            main.pushButton_3.hide()
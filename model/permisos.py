#from controllers.main_controller import *
from database.database import PermisosDb

class Vista:
    def __init__(self):
        self._row = []
        self._db = PermisosDb()
        
    def mostrar_vista(self,main,numero): 
        self._row = self._db.leer(numero)

        if self._row[0][1] is False: #editar usurio
            main.pushButton_7.hide()
        
        if self._row[0][2] is False: # Eliminar usuario
            main.pushButton_13.hide()
        
        if self._row[0][3] is False: # añadir usuario
            main.pushButton_4.hide()
        
        if self._row[0][4] is False: # gestion de claves
            main.pushButton.hide()
        
        if self._row[0][5] is False: # listado de mecanicos
            main.pushButton_3.hide()
            
        if self._row[0][6] is False: # añadir auto
            main.pushButton_10.hide()
            
        if self._row[0][7] is False: # editar autos
            main.pushButton_9.hide()
            
        if self._row[0][8] is False: # eliminar autos
            main.pushButton_15.hide()
        
        if self._row[0][9] is False: # listado de autos
            main.pushButton_5.hide()
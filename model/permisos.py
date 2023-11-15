#from controllers.main_controller import *
from model.ui import Ui

class Vista(Ui):
    def __init__(self):
        super().__init__()
        
    def mostrar_vista(self,main,numero): 
        self._selected_rows = self._db1.leer(numero)

        if self._selected_rows[0][1] is False: #editar usurio
            main.pushButton_7.hide()
        
        if self._selected_rows[0][2] is False: # Eliminar usuario
            main.pushButton_13.hide()
        
        if self._selected_rows[0][3] is False: # añadir usuario
            main.pushButton_4.hide()
        
        if self._selected_rows[0][4] is False: # gestion de claves
            main.pushButton.hide()
        
        if self._selected_rows[0][5] is False: # listado de mecanicos
            main.pushButton_3.hide()
            
        if self._selected_rows[0][6] is False: # añadir auto
            main.pushButton_10.hide()
            
        if self._selected_rows[0][7] is False: # editar autos
            main.pushButton_9.hide()
            
        if self._selected_rows[0][8] is False: # eliminar autos
            main.pushButton_15.hide()
        
        if self._selected_rows[0][9] is False: # listado de autos
            main.pushButton_5.hide()
        
        if self._selected_rows[0][10] is False: # añadir informe
            main.pushButton_16.hide()
        
        if self._selected_rows[0][11] is False: # añadir informe
            main.pushButton_18.hide()
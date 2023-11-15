from  PyQt5 import QtWidgets
from model.permisos import *
from model.ui import Ui
from database.database import PersonaDb, AutosDb
import time

class ListadoController(Ui):
    def __init__(self,main):
        super().__init__()
        self._main = main

    def listado_usuarios_mecanicos(self):
            self._selected_rows = self._db.leer_mecanicos()
            self.completar_tabla('Tableuser_2',self._selected_rows,0)

            self._selected_rows = self._db.leer_usuarios()
            self.completar_tabla('table_user',self._selected_rows,0)
    
    def autos_usuario(self,numero):
        self._selected_rows_autos = self._db2.leer_autos(numero)
        if self._db2.leer_autos(numero) != []:
            self._selected_rows_autos = self._db2.leer_autos(numero)
            self.completar_tabla('table_auto',self._selected_rows_autos,1)
        self._main.stackedWidget.setCurrentIndex(5)
        
    def cargar_listado_autos(self,numero):
        if self._main.table_user.currentRow() >= 0:
            if self._db2.leer_autos(self._selected_rows[numero-1][0]) != []:
                self._selected_rows_autos = self._db2.leer_autos(self._selected_rows[numero-1][0])
                self.completar_tabla('table_auto',self._selected_rows_autos,1)
            self._main.stackedWidget.setCurrentIndex(5)
from  PyQt5 import QtWidgets, uic
from model.permisos import *
from database.database import PersonaDb
db1 = PersonaDb()

class MainController(): # Logica de negocio
    def __init__(self,main):
        self._main = main
    def listado_usuarios_mecanicos(self):
            rows,rows_id = db1.leer_usuarios()
            c = len(rows[0])
            f = len(rows)
                
            self._main.table_user.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
            self._main.table_user.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
            self._main.table_user.setRowCount(f +1)
            self._main.table_user.setColumnCount(c)

            for i in range(f):
                for j in range(c):
                    self._main.table_user.setItem(i+1,j,QtWidgets.QTableWidgetItem(f'{rows[i][j]}'))

            rows,rows_id = db1.leer_mecanicos()
            c = len(rows[0])
            f = len(rows)
            
            self._main.Tableuser_2.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
            self._main.Tableuser_2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
            self._main.Tableuser_2.setRowCount(f +1)
            self._main.Tableuser_2.setColumnCount(c)

            for i in range(f):
                for j in range(c):
                    self._main.Tableuser_2.setItem(i+1,j,QtWidgets.QTableWidgetItem(f'{rows[i][j]}'))
    
    def cargar_listado_autos(self,numero,id_row):
        self._row = id_row(numero)
        rows = db1.leer_autos(id_row(numero))
        c = len(rows[0])
        f = len(rows)
            
        self._main.table_user.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self._main.table_user.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self._main.table_user.setRowCount(f +1)
        self._main.table_user.setColumnCount(c)

        for i in range(f):
            for j in range(c):
                self._main.table_user.setItem(i+1,j,QtWidgets.QTableWidgetItem(f'{rows[i][j]}'))
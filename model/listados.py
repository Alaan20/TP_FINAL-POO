from  PyQt5 import QtWidgets, uic
from model.permisos import *
from database.database import PersonaDb, AutosDb
db1 = PersonaDb()
db2 = AutosDb()

class MainController(): # Logica de negocio
    def __init__(self,main):
        self._main = main
        self._rows = []
        self._rows_id = []

    def listado_usuarios_mecanicos(self):
        
            self._rows,self._rows_id = db1.leer_mecanicos()
            
            self._main.Tableuser_2.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
            self._main.Tableuser_2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
            self._main.Tableuser_2.setRowCount(len(self._rows) +1)
            self._main.Tableuser_2.setColumnCount(len(self._rows[0]))
            for i in range(len(self._rows)):
                for j in range(len(self._rows[0])):
                    self._main.Tableuser_2.setItem(i+1,j,QtWidgets.QTableWidgetItem(f'{self._rows[i][j]}'))

            self._rows,self._rows_id = db1.leer_usuarios()

            self._main.table_user.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
            self._main.table_user.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
            self._main.table_user.setRowCount(len(self._rows) +1)
            self._main.table_user.setColumnCount(len(self._rows[0]))
            for i in range(len(self._rows)):
                for j in range(len(self._rows[0])):
                    self._main.table_user.setItem(i+1,j,QtWidgets.QTableWidgetItem(f'{self._rows[i][j]}'))
        
    def cargar_listado_autos(self,numero):
        
        self._rows = db2.leer_autos(self._rows_id[numero-1])
            
        self._main.table_auto.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self._main.table_auto.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self._main.table_auto.setRowCount(len(self._rows) +1)
        self._main.table_auto.setColumnCount(len(self._rows[0]))

        for i in range(len(self._rows)):
            for j in range(self._rows[0]):
                self._main.table_auto.setItem(i+1,j,QtWidgets.QTableWidgetItem(f'{self._rows[i][j]}'))
        
        self._main.stackedWidget.setCurrentIndex(5)
    
    def buscar_usuarios(self):
        # Obtener el texto del QLineEdit
        texto = self._main.lineEdit.text()
        # Realizar la búsqueda en el QTableWidget
        for i in range(self._main.table_user.rowCount()):
            for j in range(self._main.table_user.columnCount()):
                cell_widget = self._main.table_user.item(i, j)
                if cell_widget is not None and cell_widget.text() == texto:
                    # Se encontró el texto, seleccionar la fila
                    self._main.table_user.selectRow(i)
    
    def buscar_mecanicos(self):
        # Obtener el texto del QLineEdit
        texto = self._main.lineEdit_2.text()
        # Realizar la búsqueda en el QTableWidget
        for i in range(self._main.Tableuser_2.rowCount()):
            for j in range(self._main.Tableuser_2.columnCount()):
                cell_widget = self._main.Tableuser_2.item(i, j)
                if cell_widget is not None and cell_widget.text() == texto:
                    # Se encontró el texto, seleccionar la fila
                    self._main.Tableuser_2.selectRow(i)
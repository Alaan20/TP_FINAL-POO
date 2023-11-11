from  PyQt5 import QtWidgets
from database.database import AutosDb,PersonaDb, ServiceDb 

class ServiceController():
    def __init__(self,main):
        self._main=main
        self._bd1=PersonaDb()
        self._bd2=AutosDb()
        self._db3=ServiceDb()
        self._patente = None
        self._lista_service = []
    
    def mostrar_service(self):
        self._main.stackedWidget.setCurrentIndex(8)
        
        self._patente = self._main.table_auto.item(self._main.table_auto.currentRow(),0)
        self._lista_service = self._db3.leer_service(self._patente.text())
        if self._db3.leer_service(self._patente.text()) != []:
            self.llenar_tabla()

    def llenar_tabla(self):       
        self._main.table_informes.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self._main.table_informes.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self._main.table_informes.setRowCount(len(self._lista_service) +1)
        self._main.table_informes.setColumnCount(len(self._lista_service[0]))

        for i in range(len(self._lista_service)):
            for j in range(len(self._lista_service[0])):
                if self._lista_service[i][j] == None:
                    self._main.table_informes.setItem(i+1,j,QtWidgets.QTableWidgetItem(f''))
                else:
                    self._main.table_informes.setItem(i+1,j,QtWidgets.QTableWidgetItem(f'{self._lista_service[i][j]}'))
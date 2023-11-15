from  PyQt5.QtWidgets import *
from database.database import ServiceDb 
from controllers.controller_2 import CreacionServiceController, ServiceImpreso

class ServiceController():
    def __init__(self, main):
        self._main= main
        self._db3=ServiceDb()
        self._patente = None
        self._lista_service = []
        self._service_creacion = CreacionServiceController
        self._service_impresion = ServiceImpreso
    
    def mostrar_service(self):
        self._main.stackedWidget.setCurrentIndex(8)
        
        self._patente = self._main.table_auto.item(self._main.table_auto.currentRow(),0)
        if self._patente != None:
            self._main.stackedWidget.setCurrentIndex(8)
            if self._db3.leer_service(self._patente.text()) != []:
                self._lista_service = self._db3.leer_service(self._patente.text())
                self.llenar_tabla()

    def llenar_tabla(self):       
        self._main.table_informes.setSelectionBehavior(QAbstractItemView.SelectRows)
        self._main.table_informes.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self._main.table_informes.setRowCount(len(self._lista_service) +1)
        self._main.table_informes.setColumnCount(3)
        for i in range(len(self._lista_service)):
            self._main.table_informes.setItem(i,0,QTableWidgetItem(f'{self._lista_service[i][0]}'))
            self._main.table_informes.setItem(i,1,QTableWidgetItem(f'{self._lista_service[i][1]}'))
            self._main.table_informes.setItem(i,2,QTableWidgetItem(f'{self._lista_service[i][23]}'))
            self._main.table_informes.setHorizontalHeaderLabels(["nro_service","Tipo_Service","Patente_Auto"])
        self._main.table_informes.doubleClicked.connect(self.imprimo_service)
    
    def imprimo_service (self):
        self._main.table_informes.selectRow(self._main.table_informes.currentRow())
        item = list(self._main.table_informes.selectedItems())
        self._service_impresion = ServiceImpreso(item[0])
        self._service_impresion.show()
    
    def crear_service(self):
        self._patente = self._main.table_auto.item(self._main.table_auto.currentRow(),0)
        self._service_creacion = CreacionServiceController(self._patente.text())
        self._service_creacion.show()
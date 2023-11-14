from  PyQt5.QtWidgets import *
from database.database import ServiceDb 
from database.service_dao import ServiceDao
from controllers import controller_2
from views.builder_ventana import VentanaGeneral

class ServiceController():
    def __init__(self,main):
        self._main=main
        self._db3=ServiceDb()
        self._service_dao = ServiceDao()
        self._patente = None
        self._lista_service = []
        self._controller_2 = controller_2.ServiceController
    def mostrar_service(self):
        self._main.stackedWidget.setCurrentIndex(8)
        
        self._patente = self._main.table_auto.item(self._main.table_auto.currentRow(),0)
        self._lista_service = self._db3.leer_service(self._patente.text())
        if self._db3.leer_service(self._patente.text()) != []:
            self.llenar_tabla()

    def llenar_tabla(self):       
        self._main.table_informes.setSelectionBehavior(QAbstractItemView.SelectRows)
        self._main.table_informes.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self._main.table_informes.setRowCount(len(self._lista_service) +1)
        #self._main.table_informes.setColumnCount(len(self._lista_service[0]))

        self._main.table_informes.setColumnCount(3)

        for i in range(len(self._lista_service)):
            #for j in range(len(self._lista_service[0])):
            self._main.table_informes.setItem(i,0,QTableWidgetItem(f'{self._lista_service[i][0]}'))
            self._main.table_informes.setItem(i,1,QTableWidgetItem(f'{self._lista_service[i][1]}'))
            self._main.table_informes.setItem(i,2,QTableWidgetItem(f'{self._lista_service[i][23]}'))
            self._main.table_informes.setHorizontalHeaderLabels(["nro_service","Tipo_Service","Patente_Auto"])
            
            #    if self._lista_service[i][j] == None:
            #        self._main.table_informes.setItem(i+1,j,QtWidgets.QTableWidgetItem(f''))
            #    else:
        #        self._main.table_informes.setItem(i+1,j,QtWidgets.QTableWidgetItem(f'{self._lista_service[i][j]}'))
        self._main.table_informes.doubleClicked.connect(self.imprimo_service)
    
    def imprimo_service (self):
        widget = QWidget()
        layout = QVBoxLayout()
        self._main.table_informes.selectRow(self._main.table_informes.currentRow())
        item = list(self._main.table_informes.selectedItems())
        lista_informacion = self._service_dao.get_by_id(item[0])
        ventana = VentanaGeneral().armo_service_con_datos(lista_informacion)
        self._main.hide()
        layout.addWidget(ventana)
        widget.setLayout(layout)
        widget.show()
        #self.layout.addWidget(ventana)
    
    def crear_service(self):
        self._patente = self._main.table_auto.item(self._main.table_auto.currentRow(),0)
        self._controller_2 = controller_2.ServiceController(self._patente.text())
        self._controller_2.show()
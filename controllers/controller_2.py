from PyQt5.QtWidgets import *
from views.builder_ventana import AlmacenVentana
from database.database import ServiceDb, AutosDb
import sys

app = QApplication([])

service_db = ServiceDb()
almacen_ventana = AlmacenVentana()

class CreacionServiceController(QWidget):
    
    def __init__(self, patente):
        super().__init__()
        self.gui_service(patente)
        self.auto_db = AutosDb()
        self.__validacion = bool
    
    def gui_service (self,patente):
        layout = QVBoxLayout()
        self.__combo_box = QComboBox()
        self.__combo_box.addItems(["Basico","Estandar","Completo"])
        self.__combo_box.currentTextChanged.connect(self.__actualizar_ventana)
        self.etiqueta1 = QLabel()
        self.line = QLineEdit()
        self.line.setText(patente)
        self.etiqueta1.setMaximumSize(400,100)
        self.line.textChanged.connect(self.__busco_auto)
        self.__ventana_basica = almacen_ventana.basica
        self.__ventana_estandar = almacen_ventana.estandar
        self.__ventana_completa = almacen_ventana.completa
        self.__btn = QPushButton("Guardar")
        layout.addWidget(self.__combo_box)
        layout.addWidget(self.line)
        layout.addWidget(self.etiqueta1)
        layout.addWidget(self.__ventana_basica.plantilla)
        layout.addWidget(self.__ventana_estandar.plantilla)
        layout.addWidget(self.__ventana_completa.plantilla)
        layout.addWidget(self.__btn)
        self.__btn.pressed.connect(self.__guardo_datos)
        self.setLayout(layout)
        self.__reinicio_ventana()
        self.__actualizar_ventana()

    def __busco_auto (self):
        texto = self.line.text()
        marca = self.auto_db.get_one(texto)
        if marca is not None:
            self.etiqueta1.setText("Patente ingresada correctamente")
            print(marca)
            self.__validacion = True
        else:
            self.__validacion = False
            self.etiqueta1.setText("Se equivoco de patente")

    def __guardo_datos (self):
        opcion = self.__combo_box.currentText()
        l = []
        l = almacen_ventana.listo_hijos(opcion)
        
        if self.__validacion == True:
            service_db.commit(l,f"{self.line.text()}")
            print(l)

    def __actualizar_ventana (self):
        opcion = self.__combo_box.currentText()
        for item in [self.__ventana_basica, self.__ventana_estandar, self.__ventana_completa]:
            if opcion == item.nombre:
                self.__mostrar_ventana(item)
                break

    def __reinicio_ventana (self):
        for v in [self.__ventana_basica, self.__ventana_estandar,self.__ventana_completa]:
            v.plantilla.hide()
    
    def __mostrar_ventana (self, ventana):
        self.__reinicio_ventana()
        ventana.plantilla.show()
        self.resize(0,0)
        self.setMinimumSize(self.width(),self.height())
        self.setMaximumSize(self.width(),self.height())
        self.etiqueta1.setFixedSize(500,15)
        self.etiqueta1.setMaximumSize(500,15)
        self.etiqueta1.setMinimumSize(500,15)

##Los separe en clases para evitar inconvenientes con los atributos no existentes
class ServiceImpreso (QWidget):
    
    def __init__(self, id):
        super().__init__()
        self.imprimo_service(id)
    
    def imprimo_service (self, id):
        layout2 = QVBoxLayout()
        lista_informacion = list(service_db.get_by_id(id))
        self.ventana_impresion = almacen_ventana.armo_ventana_con_datos(lista_informacion)
        layout2.addWidget(self.ventana_impresion)
        self.__reinicio_ventana_impresion()  ##oculta todas las ventanas (nuevas y existentes)
        self.ventana_impresion.show() ##es para mostrar la ventana nueva
        self.setLayout(layout2)
    
    def __reinicio_ventana_impresion (self):
        self.ventana_impresion.hide()
from PyQt5.QtWidgets import *
from views.builder_ventana import *
#from database.auto_dao import AutoDao
from database.database import ServiceDb, AutosDb
import sys

app = QApplication([])

service_db = ServiceDb()

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
        self.__ventana_basica = VentanaGeneral().armo_service("Basico")
        self.__ventana_estandar = VentanaGeneral().armo_service("Estandar")
        self.__ventana_completa = VentanaGeneral().armo_service("Completo")
        self.__btn = QPushButton("Guardar")
        layout.addWidget(self.__combo_box)
        layout.addWidget(self.line)
        layout.addWidget(self.etiqueta1)
        layout.addWidget(self.__ventana_basica)
        layout.addWidget(self.__ventana_estandar)
        layout.addWidget(self.__ventana_completa)
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
        if opcion == "Basico":
            l = self.__ventana_basica.listo_hijos()
            l.insert(0,"Basico")
        elif opcion == "Estandar":
            l = self.__ventana_estandar.listo_hijos()
            l.insert(0,"Estandar")
        else:
            l = self.__ventana_completa.listo_hijos()
            l.insert(0,"Completo")
        
        if self.__validacion == True:
            service_db.commit(l,f"{self.line.text()}")
            print(l)

    def __actualizar_ventana (self):
        opcion = self.__combo_box.currentText()
        if opcion == "Basico":
            self.__mostrar_ventana(self.__ventana_basica)
        elif opcion == "Estandar":
            self.__mostrar_ventana(self.__ventana_estandar)
        elif opcion == "Completo":
            self.__mostrar_ventana(self.__ventana_completa)

    def __reinicio_ventana (self):
        for v in [self.__ventana_basica, self.__ventana_estandar,self.__ventana_completa]:
            v.hide()
    
    def __mostrar_ventana (self, ventana):
        self.__reinicio_ventana()
        ventana.show()
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
        self.ventana_impresion = VentanaGeneral().armo_service_con_datos(lista_informacion)
        layout2.addWidget(self.ventana_impresion)
        self.__reinicio_ventana_impresion()  ##oculta todas las ventanas (nuevas y existentes)
        self.ventana_impresion.show() ##es para mostrar la ventana nueva
        self.setLayout(layout2)
    
    def __reinicio_ventana_impresion (self):
        self.ventana_impresion.hide()
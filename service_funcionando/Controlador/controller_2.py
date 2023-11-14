#from Modelo.interfaz_impresion import MainWindow
from PyQt5.QtWidgets import *
from Vista.builder_ventana import *
from Dao.auto_dao import AutoDao
from Dao.service_dao import ServiceDao
import sys

app = QApplication([])
# mw = MainWindow()

class ServiceController(QWidget):
    
    def __init__(self):
        super().__init__()
        self.gui_service()
        self.auto_dao = AutoDao()
        self.__service_dao = ServiceDao()
        self.__validacion = bool
    
    def gui_service (self):
        layout = QVBoxLayout()
        self.__combo_box = QComboBox()
        self.__combo_box.addItems(["Basico","Estandar","Completo"])
        
        self.__combo_box.currentTextChanged.connect(self.__actualizar_ventana)
        self.etiqueta1 = QLabel()
        self.line = QLineEdit()
        self.line.setPlaceholderText("Ingrese una patente")
        self.etiqueta1.setMaximumSize(400,100)
        self.line.textChanged.connect(self.__busco_auto)
        
        self.__ventana_basica = VentanaBasica().armo_service("Basico")
        self.__ventana_estandar = VentanaBasica().armo_service("Estandar")
        self.__ventana_completa = VentanaBasica().armo_service("Completo")

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
        marca = self.auto_dao.get_one(texto)
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
            self.__service_dao.commit(l,f"{self.line.text()}")
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

class Service():
    
    def __init__(self):
        self.service_controller = ServiceController()
        self.service_controller.show()
        app.exec()
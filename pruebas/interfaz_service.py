from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
from ejemplo_builder_para_proyecto_final import Director, concretebuilderService

class VentanaPrincipal (QWidget):

    def __init__(self):
        super().__init__()
        self.__init_ui()
    
    def __init_ui(self):
        layout = QVBoxLayout()
        self.__combo_box = QComboBox()
        self.__combo_box.addItems(["Basico","Estandar","Completo"])
        layout.addWidget(self.__combo_box)
        
        self.__combo_box.currentTextChanged.connect(self.__actualizar_ventana)
        
        self.__ventana_basica = VentanaService("Basico")
        self.__ventana_estandar = VentanaService("Estandar")
        self.__ventana_completa = VentanaService("Completo")

        layout.addWidget(self.__ventana_basica)
        layout.addWidget(self.__ventana_estandar)
        layout.addWidget(self.__ventana_completa)
        
        self.setLayout(layout)
        self.__reinicio_ventana()
        self.__actualizar_ventana()

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


class VentanaService(QWidget):
    
    def __init__(self, nombre):
        super().__init__()
        self.__busco_ui(nombre)

    def __busco_ui (self, nombre):
        if nombre == "Basico":
            self.__init_ui_basico()
        elif nombre == "Estandar":
            self.__init_ui_estandar()
        elif nombre == "Completo":
            self.__init_ui_completo()

    def __init_ui_basico (self):
        layout = QVBoxLayout()
        direc = Director()
        direc.builder = concretebuilderService() 
        direc.service_basico()
        
        layout = asigno_layout(direc.builder.service._parts)
        self.setLayout(layout)

    def __init_ui_estandar (self):
        layout = QVBoxLayout()
        direc = Director()
        direc.builder = concretebuilderService()
        direc.service_estandar()
        
        layout = asigno_layout(direc.builder.service._parts)
        self.setLayout(layout)

    def __init_ui_completo (self):
        direc = Director()
        direc.builder = concretebuilderService()
        direc.service_completo()
        
        layout = asigno_layout(direc.builder.service._parts)
        self.setLayout(layout)

def asigno_layout (lista):
    layout1 = QVBoxLayout()
    layout2 = QVBoxLayout()
    layout_completo = QHBoxLayout()
    
    for i in lista:
        lbl = QLabel(i)
        layout1.addWidget(lbl)
        combo = QComboBox()
        combo.addItem('Excelente')
        combo.addItem('Intermedio')
        combo.addItem('Defectuoso')
        layout2.addWidget(combo)

    layout_completo.addLayout(layout1)
    layout_completo.addLayout(layout2)
    
    return layout_completo

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana_principal = VentanaPrincipal()
    ventana_principal.show()
    sys.exit(app.exec())
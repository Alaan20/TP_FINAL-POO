from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from ejemplo_builder_para_proyecto_final import ServiceBasico, ServiceEstandar, ServiceCompleto

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
        service = ServiceBasico()
        layout = asigno_layout(service._partes_service())
        self.setLayout(layout)

    def __init_ui_estandar (self):
        service = ServiceEstandar()
        layout = asigno_layout(service._partes_service())
        self.setLayout(layout)

    def __init_ui_completo (self):
        #lista = list
        service = ServiceCompleto()
        layout= asigno_layout(service._partes_service())
        self.setLayout(layout)

    def listo_hijos (self):
        l = []
        try:
            for i in range(1,23):
                combo = self.findChild(QComboBox,f"combo{i}")
                l.append(combo.currentText())
        except AttributeError:
            return l

def asigno_layout (lista):
    layout1 = QVBoxLayout()
    layout2 = QVBoxLayout()
    layout_completo = QHBoxLayout()
    j = 0
    for i in lista:
        j += 1
        lbl = QLabel(i)
        layout1.addWidget(lbl)
        combo = QComboBox()
        combo.setObjectName(f"combo{j}")
        combo.addItem('Excelente')
        combo.addItem('Intermedio')
        combo.addItem('Defectuoso')
#        print(combo.objectName())
        layout2.addWidget(combo)

    layout_completo.addLayout(layout1)
    layout_completo.addLayout(layout2)
    
    return layout_completo

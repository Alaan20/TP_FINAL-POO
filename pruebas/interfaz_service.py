from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
from ejemplo_builder_para_proyecto_final import Director, concretebuilderService


class Window (QMainWindow):

    def __init__(self):
        super(QMainWindow,self).__init__()
        self.layout1 = QVBoxLayout()
        
        btn1 = QRadioButton('Basico')
        btn1.pressed.connect(self.service_basico)
        
        btn2 = QRadioButton('Estandar')
        btn2.pressed.connect(self.service_estandar)
        
        btn3 = QRadioButton('Completo')
        btn3.pressed.connect(self.service_completo)
        
        self.layout1.addWidget(btn1)
        self.layout1.addWidget(btn2)
        self.layout1.addWidget(btn3)
        
        widget1 = QWidget()
        widget1.setLayout(self.layout1)
        self.setCentralWidget(widget1)

    def service_basico (self):
        widget_completo = QWidget()
        direc = Director()
        direc.builder = concretebuilderService() 
        direc.service_basico()
        
        self.asigno(direc.builder.service._parts,widget_completo)
        self.setCentralWidget(widget_completo)

    def service_estandar (self):
        widget_completo = QWidget()
        direc = Director()
        direc.builder = concretebuilderService()
        direc.service_standar()
        
        self.asigno(direc.builder.service._parts, widget_completo)
        self.setCentralWidget(widget_completo)


    def service_completo (self):
        widget_terminado = QWidget()
        direc = Director()
        direc.builder = concretebuilderService()
        direc.service_completo()
        
        self.asigno(direc.builder.service._parts, widget_terminado)
        self.setCentralWidget(widget_terminado)

    def asigno (self, lista, widget):
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
        widget.setLayout(layout_completo)
        return widget

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())

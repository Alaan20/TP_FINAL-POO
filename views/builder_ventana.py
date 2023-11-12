from abc import ABC, abstractmethod
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class BuilderVentana (ABC):
    
    @property
    @abstractmethod
    def ventana (self):
        pass
    
    @abstractmethod
    def ventana_basica (self):
        pass
    
    @abstractmethod
    def ventana_estandar (self):
        pass
    
    @abstractmethod
    def ventana_completa (self):
        pass
    
    @abstractmethod
    def armo_layout (self):
        pass


class ConcreteBuilderVentana (BuilderVentana):
    
    def __init__(self):
        self.reset()
    
    def reset (self):
        self._ventana = Ventana()
    
    @property
    def ventana (self):
        ventana = self._ventana
        return ventana

    def ventana_basica(self):
        self._ventana.agregar(QLabel("Elementos de Seguridad: Revision y reposicion de luces exteriores y baul"),"Label")
        self._ventana.agregar(QLabel("Elementos de Seguridad: Amortiguadores"),"Label")
        self._ventana.agregar(QLabel("Elementos de Seguridad: Revision general de presion de neumaticos"),"Label")
        self._ventana.agregar(QLabel("Elementos de Seguridad: Revision tuerca neumaticos"),"Label")
        self._ventana.agregar(QLabel("Fluidos del Vehiculo: Bateria"),"Label")
        self._ventana.agregar(QLabel("Lubricantes y Filtros: Revision filtro de combustible"),"Label")
        self._ventana.agregar(QLabel("Lubricantes y Filtros: Revision aceite diferencial"),"Label")
        self._ventana.agregar(QLabel("Lubricantes y Filtros: Cambio de aceite y filtro"),"Label")
    
    def ventana_estandar(self):
        self.ventana_basica()
        self._ventana.agregar(QLabel("Fluidos del Vehiculo: Liquido de direccion hidraulica y del limpiaparabrisas"),"Label")
        self._ventana.agregar(QLabel("Fluidos del Vehiculo: Revision liquido de frenos"),"Label")
        self._ventana.agregar(QLabel("Partes Mecanicas: Bisagras de puertas y engrase retenedor de puertas"),"Label")
        self._ventana.agregar(QLabel("Partes Mecanicas: Caño de escape"),"Label")
        self._ventana.agregar(QLabel("Partes Mecanicas: Correa alternador y de Direccion Asistida"),"Label")
        self._ventana.agregar(QLabel("ABS: Airbag"),"Label")
        self._ventana.agregar(QLabel("ABS: Inyeccion"),"Label")
        self._ventana.agregar(QLabel("ABS: Sensores y Actuadores"),"Label")
    
    def ventana_completa(self):
        self.ventana_estandar()
        self._ventana.agregar(QLabel("Pruebas Dinamicas: Cinturon de Seguridad (Comprobar Funcionamiento Inercial)"),"Label")
        self._ventana.agregar(QLabel("ABS: Climatizacion"),"Label")
        self._ventana.agregar(QLabel("ABS: Historial de fallas"),"Label")
        self._ventana.agregar(QLabel("ABS: Instrumental"),"Label")
        self._ventana.agregar(QLabel("Escaneo con computadora: Diagnostico y reparacion de errores"),"Label")
    
    def __asigno_combos (self):
        lista_items = ['Excelente','Intermedio','Defectuoso']
        numero = self._ventana.contador
        for i in range(0,numero):
            combo = QComboBox()
            combo.setObjectName(f"combo{i}")
            combo.addItems(lista_items)
            self._ventana.agregar(combo, "Combo")
    
    def armo_layout (self):
        self.__asigno_combos()
        self._ventana.armo_widget()
        return self.ventana


class Ventana (QWidget):
    
    def __init__(self):
        super().__init__()
        self.__layout_combos = QVBoxLayout()
        self.__layout_etiquetas = QVBoxLayout()
        self.__contador = 0
    
    def agregar (self, elemento, tipo):
        if tipo == "Combo":
            self.__layout_combos.addWidget(elemento)
        elif tipo == "Label":
            self.__layout_etiquetas.addWidget(elemento)
            self.__contador += 1
    
    @property
    def contador (self):
        return self.__contador
    
    def armo_widget (self):
        layout = QHBoxLayout()
        layout.addLayout(self.__layout_etiquetas)
        layout.addLayout(self.__layout_combos)
        self.setLayout(layout)
    
    def listo_hijos (self):
        l = []
        try:
            for i in range(0,23):
                combo = self.findChild(QComboBox,f"combo{i}")
                print(i)
                if combo.currentText() is not None:
                    l.append(combo.currentText())
        except AttributeError:
            return l


class Director ():
    
    def __init__(self):
        self.__builder = None
    
    @property
    def builder (self):
        return self.__builder
    
    @builder.setter
    def builder (self,builder):
        self.__builder = builder
    
    def preparo_ventana (self, cadena):
        if cadena == "Basico":
            self.__builder.ventana_basica()
        elif cadena == "Estandar":
            self.__builder.ventana_estandar()
        elif cadena == "Completo":
            self.__builder.ventana_completa()
        return self.builder.armo_layout()

class VentanaBasica:
    
    def __init__(self):
        self._director = Director()
    
    def armo_service (self, cadena):
        self._director.builder = ConcreteBuilderVentana()
        return self._director.preparo_ventana(cadena)

#1. partes de labels,combo
#2. creo_layout
#3. devuelvo_layout
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
        self._ventana = VentanaCreadora()
    
    @property
    def ventana (self):
        ventana = self._ventana
        return ventana

    def ventana_basica(self):
        self._ventana.agregar(QLabel("Elementos de Seguridad: Revision y reposicion de luces exteriores y baul"),"Label",1)
        self._ventana.agregar(QLabel("Elementos de Seguridad: Amortiguadores"),"Label",1)
        self._ventana.agregar(QLabel("Elementos de Seguridad: Revision general de presion de neumaticos"),1,"Label")
        self._ventana.agregar(QLabel("Elementos de Seguridad: Revision tuerca neumaticos"),"Label",1)
        self._ventana.agregar(QLabel("Fluidos del Vehiculo: Bateria"),"Label",1)
        self._ventana.agregar(QLabel("Lubricantes y Filtros: Revision filtro de combustible"),"Label",1)
        self._ventana.agregar(QLabel("Lubricantes y Filtros: Revision aceite diferencial"),"Label",1)
        self._ventana.agregar(QLabel("Lubricantes y Filtros: Cambio de aceite y filtro"),"Label",1)
    
    def ventana_estandar(self):
        self.ventana_basica()
        self._ventana.agregar(QLabel("Fluidos del Vehiculo: Liquido de direccion hidraulica y del limpiaparabrisas"),"Label",1)
        self._ventana.agregar(QLabel("Fluidos del Vehiculo: Revision liquido de frenos"),"Label",1)
        self._ventana.agregar(QLabel("Partes Mecanicas: Bisagras de puertas y engrase retenedor de puertas"),"Label",1)
        self._ventana.agregar(QLabel("Partes Mecanicas: Caño de escape"),"Label",1)
        self._ventana.agregar(QLabel("Partes Mecanicas: Correa alternador y de Direccion Asistida"),"Label",1)
        self._ventana.agregar(QLabel("ABS: Airbag"),"Label",1)
        self._ventana.agregar(QLabel("ABS: Inyeccion"),"Label",1)
        self._ventana.agregar(QLabel("ABS: Sensores y Actuadores"),"Label",1)
    
    def ventana_completa(self):
        self.ventana_estandar()
        self._ventana.agregar(QLabel("Pruebas Dinamicas: Cinturon de Seguridad (Comprobar Funcionamiento Inercial)"),"Label",1)
        self._ventana.agregar(QLabel("ABS: Climatizacion"),"Label",1)
        self._ventana.agregar(QLabel("ABS: Historial de fallas"),"Label",1)
        self._ventana.agregar(QLabel("ABS: Instrumental"),"Label",1)
        self._ventana.agregar(QLabel("Escaneo con computadora: Diagnostico y reparacion de errores"),"Label",1)
    
    def __asigno_combos (self):
        lista_items = ['Excelente','Intermedio','Defectuoso']
        numero = self._ventana.contador
        for i in range(0,numero+1):
            combo = QComboBox()
            combo.setObjectName(f"combo{i}")
            combo.addItems(lista_items)
            self._ventana.agregar(combo, "Combo",1)
    
    def armo_layout_con_datos (self, lista):
        minimo = 1
        maximo = len(lista) -1
        cont = 0
        for i in lista:
            if cont > minimo and cont<maximo and i != None:
                self.ventana.agregar(QLabel(f'{i}'),"Label",2)
            cont += 1
        self.ventana.armo_impresion()
        return self.ventana
    
    def armo_layout (self):
        self.__asigno_combos()
        self._ventana.armo_widget()
        return self.ventana


class VentanaCreadora (QWidget):
    
    def __init__(self):
        super().__init__()
        self.__layout_combos = QVBoxLayout()
        self.__layout_etiquetas = QVBoxLayout()
        self.__layout_informacion = QVBoxLayout()
        self.__contador = 0
    
    def agregar (self, elemento, tipo, nro):
        if tipo == "Combo":
            self.__layout_combos.addWidget(elemento)
        elif tipo == "Label":
            if nro == 1:
                self.__layout_etiquetas.addWidget(elemento)
                self.__contador += 1
            else:
                self.__layout_informacion.addWidget(elemento)
    
    @property
    def contador (self):
        return self.__contador
    
    def armo_widget (self):
        layout = QHBoxLayout()
        layout.addLayout(self.__layout_etiquetas)
        layout.addLayout(self.__layout_combos)
        self.setLayout(layout)
    
    def armo_impresion (self):
        layout = QHBoxLayout()
        layout.addLayout(self.__layout_etiquetas)
        layout.addLayout(self.__layout_informacion)
        self.setLayout(layout)
    
    def listo_hijos (self):
        l = []
        try:
            for i in range(0,23):
                combo = self.findChild(QComboBox,f"combo{i}")
                
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
        return self.__builder.armo_layout()
    
    def creo_ventana (self, lista):
        if lista[1] == "Basico":
            self.__builder.ventana_basica()
        elif lista[1] == "Estandar":
            self.__builder.ventana_estandar()
        elif lista[1] == "Completo":
            self.__builder.ventana_completa()
        return self.__builder.armo_layout_con_datos(lista)

class CreadorVentanaGenerico (ABC):
    
    def __init__(self, nombre):
        self._director = Director()
        self._nombre = nombre
        self._plantilla = None
    
    @property
    def nombre (self):
        return self._nombre
    
    @property
    def plantilla (self):
        return self._plantilla
    
    def armo_service (self):
        self._director.builder = ConcreteBuilderVentana()
        self._plantilla = self._director.preparo_ventana(self._nombre)
    
    def armo_ventana_con_datos (self, lista):
        self._director.builder = ConcreteBuilderVentana()
        return self._director.creo_ventana(lista)
    
    def listo_hijos (self, lista):
        lista = self._plantilla.listo_hijos()
        lista.insert(0,f'{self._nombre}')
        return lista


class VentanaBasica(CreadorVentanaGenerico):
    
    def __init__(self):
        super().__init__("Basico")
        self.armo_service()
    
    def armo_service(self):
        super().armo_service()

    def listo_hijos(self, lista):
        return super().listo_hijos(lista)


class VentanaEstandar (CreadorVentanaGenerico):
    
    def __init__(self):
        super().__init__("Estandar")
        self.armo_service()
    
    def armo_service(self):
        super().armo_service()

    def listo_hijos(self, lista):
        return super().listo_hijos(lista)


class VentanaCompleta (CreadorVentanaGenerico):
    
    def __init__(self):
        super().__init__("Completo")
        self.armo_service()

    def armo_service(self):
        super().armo_service()
    
    def listo_hijos(self, lista):
        return super().listo_hijos(lista)

class AlmacenVentana:
    
    def __init__(self):
        self.__creador = CreadorVentanaGenerico('')
        self.__ventana_basica = VentanaBasica()
        self.__ventana_estandar = VentanaEstandar()
        self.__ventana_completa = VentanaCompleta()
    
    @property
    def basica (self):
        return self.__ventana_basica
    
    @basica.setter
    def basica (self, ventana):
        self.__ventana_basica = ventana
    
    @property
    def estandar (self):
        return self.__ventana_estandar
    
    @estandar.setter
    def estandar (self, ventana):
        self.__ventana_estandar = ventana

    @property
    def completa (self):
        return self.__ventana_completa
    
    @completa.setter
    def completa (self, ventana):
        self.__ventana_completa = ventana
    
    def listo_hijos (self, nombre):
        l = []
        for elemento in [self.__ventana_basica, self.__ventana_estandar, self.__ventana_completa]:
            if elemento.nombre == nombre:
                l = elemento.listo_hijos(l)
                return l
    
    def armo_ventana_con_datos (self, lista):
        return self.__creador.armo_ventana_con_datos(lista)
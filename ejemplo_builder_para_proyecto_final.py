from __future__ import annotations
from abc import ABC,abstractmethod
from typing import Any

class builderService(ABC):

    @property
    @abstractmethod
    def service(self)-> None:
        pass
    
    @abstractmethod
    def servicios_basico(self)->None:
        pass
    @abstractmethod
    def servicios_estandar(self)->None:
        pass
    @abstractmethod
    def servicios_completo(self)->None:
        pass

class concretebuilderService(builderService):
    def __init__(self) -> None:
        self.reset()
    def reset(self)->None:
        self._service= Service()
    
    @property
    def service(self)->Service:
        service=self._service
        return service
    
    def servicios_basico(self) -> None:
        self._service.agregar("Elementos de Seguridad: Revision y reposicion de luces exteriores y baul")
        self._service.agregar("Elementos de Seguridad: Amortiguadores")
        self._service.agregar("Elementos de Seguridad: Revision general de presion de neumaticos")
        self._service.agregar("Elementos de Seguridad: Revision tuerca neumaticos")
        
        self._service.agregar("Fluidos del Vehiculo: Bateria")
        
        self._service.agregar("Lubricantes y Filtros: Revision filtro de combustible")
        self._service.agregar("Lubricantes y Filtros: Revision aceite diferencial")
        self._service.agregar("Lubricantes y Filtros: Cambio de aceite y filtro")
        self._service.ordenar()
    
    def servicios_estandar(self) -> None:
        self._service.agregar("Fluidos del Vehiculo: Liquido de direccion hidraulica y del limpiaparabrisas")
        self._service.agregar("Fluidos del Vehiculo: Revision liquido de frenos")
        
        self._service.agregar("Partes Mecanicas: Bisagras de puertas y engrase retenedor de puertas")
        self._service.agregar("Partes Mecanicas: Caño de escape")
        self._service.agregar("Partes Mecanicas: Correa alternador y de Direccion Asistida")
        
        self._service.agregar("ABS: Airbag")
        self._service.agregar("ABS: Inyeccion")
        self._service.agregar("ABS: Sensores y Actuadores")
        self._service.ordenar()
    
    def servicios_completo(self) -> None:
        self._service.agregar("Pruebas Dinamicas: Cinturon de Seguridad (Comprobar Funcionamiento Inercial)")
        self._service.agregar("ABS: Climatizacion")
        self._service.agregar("ABS: Historial de fallas")
        self._service.agregar("ABS: Instrumental")
        self._service.agregar("Escaneo con computadora: Diagnostico y reparacion de errores")
        self._service.ordenar()

class Service():
    def __init__(self) -> None:
        self._parts=[]
    
    def agregar(self,servicios:Any)->None:
        self._parts.append(servicios)
    
    def listado_De_servicios(self):
        print(f"Servicios a aplicar:\n")
        for i in self._parts:
            print(i,end='\n')
    
    def ordenar(self):
        self._parts.sort()

class Director():
    def __init__(self) -> None:
        self._builder=None
    
    @property
    def builder(self)->builderService:
        return self._builder
    @builder.setter
    def builder(self,builder: builderService)->None:
        self._builder=builder
    def service_basico(self):
        self.builder.servicios_basico()
    def service_estandar(self):
        self.builder.servicios_basico()
        self.builder.servicios_estandar()
    def service_completo(self):
        self.builder.servicios_basico()
        self.builder.servicios_estandar()
        self.builder.servicios_completo()

director=Director()
builder=concretebuilderService()
director.builder=builder
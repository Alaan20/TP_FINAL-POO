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
    def servicios_standar(self)->None:
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
        self._service.agregar("Elementos de seguridad: revision y resposicion de luces exteriores y baul")
        self._service.agregar("Elementos de seguridad: revision de presion de neuomaticos(TI)")
        self._service.agregar("Elementos de seguridad: revision de presion de neuomaticos(TD)")
        self._service.agregar("Elementos de seguridad: revision de presion de neuomaticos(DI)")
        self._service.agregar("Elementos de seguridad: revision de presion de neuomaticos(DD)")
        self._service.agregar("Fluidos del vehiculo: bateria")
        self._service.agregar("Lubricantes y filtros: revision filtro de combustible")
        self._service.agregar("Lubricantes y filtros: revision aceite diferencial")
        self._service.agregar("Lubricantes y filtros: cambio de aceite y filtro")
        self._service.ordenar()
    
    def servicios_standar(self) -> None:
        self._service.agregar("Elementos de seguridad: revision tuerca neumaticos")
        self._service.agregar("Elementos de seguridad: revisar/reemplazar escobillas limpiaparabrisas")
        self._service.agregar("Elementos de seguridad: pastillas de freno")
        self._service.agregar("Elementos de seguridad: disco de freno")
        self._service.agregar("Elementos de seguridad: amortiguadores")
        self._service.agregar("Fluidos del vehiculo: liquido de direccion hidraulica")
        self._service.agregar("Fluidos del vehiculo: liquido limpiaparabrisas")
        self._service.agregar("Fluidos del vehiculo: revision liquido de frenos")
        self._service.agregar("Lubricantes y filtros: revision aceite caja de transferencia")
        self._service.agregar("Lubricantes y filtros: reemplazo de filtro de aire")
        self._service.agregar("Partes mecanicas: bisagras de puertas y engrase retenedor de puertas")
        self._service.agregar("Partes mecanicas: caño de escape")
        self._service.agregar("Partes mecanicas: correa alternador")
        self._service.agregar("Partes mecanicas: correa direccion asistida")
        self._service.agregar("ABS: airbag")
        self._service.agregar("ABS: inyeccion")
        self._service.agregar("ABS: sensores y actuadores")
        self._service.ordenar()
    
    def servicios_completo(self) -> None:
        self._service.agregar("Elementos de seguridad: flexibles de freno")
        self._service.agregar("Elementos de seguridad: ajuste de presion de los neumaticos T")
        self._service.agregar("Elementos de seguridad: ajuste de presion de los neumaticos D")
        self._service.agregar("Fluidos del vehiculo: revision liquido refrigerante/anticongelante")
        self._service.agregar("Fluidos del vehiculo: punto de congelamiento")
        self._service.agregar("Lubricantes y filtros: revision aceite caja de cambios")
        self._service.agregar("Partes mecanicas: arandela tapon de carter")
        self._service.agregar("Partes mecanicas: correa aire condicionado")
        self._service.agregar("Partes mecanicas: guardapolvos y holguras de transmicion")
        self._service.agregar("Partes mecanicas: revision de mangueras")
        self._service.agregar("Pruebas dinamicas: cinturon de seguridad(comprobar funcionamiento inercial)")
        self._service.agregar("ABS: climatizacion")
        self._service.agregar("ABS: historial de fallas")
        self._service.agregar("ABS: instrumental")
        self._service.agregar("Escaneo con computadora: diagnostico y reparacion de errores")
        self._service.ordenar()

class Service():
    def __init__(self) -> None:
        self._parts=[]
    
    def agregar(self,servicios:Any)->None:
        self._parts.append(servicios)
    
    def listado_De_servicios(self):
        print(f"servivios a aplicar:\n")
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
    def service_standar(self):
        self.builder.servicios_basico()
        self.builder.servicios_standar()
    def service_completo(self):
        self.builder.servicios_basico()
        self.builder.servicios_standar()
        self.builder.servicios_completo()

director=Director()
builder=concretebuilderService()
director.builder=builder

# print("service basico: \n")
# director.service_basico()
# builder.service.listado_De_servicios()
# print("service standar:\n")
# director.service_standar()
# builder.service.listado_De_servicios()
# print("service completo: \n")
# director.service_completo()
# builder.service.listado_De_servicios()

from model.ui import Ui
from model.permisos import Vista
from model.listados import ListadoController
from model.busqueda import BusquedaController
from model.editar import EditarController
from model.agregar_usuarios import Agregar
from model.eliminar import Eliminar
from model.autos import AutosController
from model.service import ServiceController

class Main(Ui):
        def __init__(self,row,app,main):
            super().__init__()
            self._row = row
            self._app = app
            self._main = main
            self._mainController = ListadoController(main)
            self._busquedaController = BusquedaController(main)
            self._editar = EditarController(main)
            self._agregar=Agregar(main)
            self._eliminar = Eliminar(main)
            self._autos=AutosController(main)
            self._vista = Vista()
            self._service = ServiceController(main)
            
            if self._row[8] == 1:
                self._vista.mostrar_vista(main,1)
            
            elif self._row[8] == 2:
                self._vista.mostrar_vista(main,2)
                self._main.stackedWidget.setCurrentIndex(5)
                self._mainController.autos_usuario(self._row[0])
                
            self._mainController.listado_usuarios_mecanicos()
            self._main.pushButton_3.clicked.connect(lambda: self._main.stackedWidget.setCurrentIndex(0))
            self._main.pushButton_5.clicked.connect(lambda: self._main.stackedWidget.setCurrentIndex(1))
            self._main.pushButton_4.clicked.connect(lambda: (self.limpiar_texto(), self._main.stackedWidget.setCurrentIndex(3)))
            self._main.pushButton.clicked.connect(lambda: (self.limpiar_texto(), self._main.stackedWidget.setCurrentIndex(4)))
            self._main.table_user.cellDoubleClicked.connect(lambda: self._mainController.cargar_listado_autos(self._main.table_user.currentRow()) if main.table_user.currentRow() != 0 else None)
            self._main.pushButton_6.clicked.connect(lambda: self._mainController.cargar_listado_autos(self._main.table_user.currentRow()) if main.table_user.currentRow() != 0 else None)
            self._main.pushButton_2.clicked.connect(self._busquedaController.buscar_usuarios)
            self._main.pushButton_8.clicked.connect(self._busquedaController.buscar_mecanicos)
            self._main.pushButton_7.clicked.connect(self._editar.editar_usuarios)
            self._main.pushButton_19.clicked.connect(self._editar.editar_mecanicos)
            self._main.pushButton_22.clicked.connect(self._editar.guardar_cambios)
            self._main.pushButton_14.clicked.connect(self._agregar.agregar_usuario)
            self._main.refrescar_2.clicked.connect(lambda: self._mainController.listado_usuarios_mecanicos())
            self._main.refrescar_3.clicked.connect(lambda: self._mainController.listado_usuarios_mecanicos())
            self._main.log_in_1.clicked.connect(self._editar.editar_admin)
            self._main.pushButton_13.clicked.connect(self._eliminar.eliminar_usuarios)
            self._main.pushButton_20.clicked.connect(self._eliminar.elimininar_mecanico)
            self._main.pushButton_10.clicked.connect(lambda: (self.limpiar_texto(), self._main.stackedWidget.setCurrentIndex(7)))
            self._main.pushButton_23.clicked.connect(self._autos.agregar_autos)
            self._main.pushButton_9.clicked.connect(self._autos.editar_autos)
            self._main.pushButton_15.clicked.connect(self._autos.borrar_autos)
            self._main.pushButton_11.clicked.connect(self._service.mostrar_service)
            self._main.pushButton_16.clicked.connect(self._service.crear_service)
            self._main.pushButton_12.clicked.connect(lambda: self._main.stackedWidget.setCurrentIndex(5))
            main.show()
from  PyQt5 import QtWidgets, uic
#from main import app, main, db1, db
from model.permisos import *
from model.main_model import *

class Main():
        def __init__(self,row,app,main):
            self._row = row
            self._app = app
            self._main = main
            self._posicion = 0
            self._mainController = MainController(main)
            if self._row[8] == 1:
                db.mecanico_vista(self._main)
                
            self._mainController.listado_usuarios_mecanicos()
            self._main.pushButton_3.clicked.connect(lambda: main.stackedWidget.setCurrentIndex(0))
            self._main.pushButton_5.clicked.connect(lambda: main.stackedWidget.setCurrentIndex(1))
            self._main.pushButton_4.clicked.connect(lambda: main.stackedWidget.setCurrentIndex(3))
            self._main.pushButton_6.clicked.connect(lambda: main.stackedWidget.setCurrentIndex(2))
            self._main.pushButton.clicked.connect(lambda: main.stackedWidget.setCurrentIndex(4))
            self._main.table_user.cellDoubleClicked.connect(lambda: self._mainController.cargar_listado_autos(self._main.table_user.currentRow()) if main.table_user.currentRow() != 0 else None)

            self._main.show()
            app.exec()
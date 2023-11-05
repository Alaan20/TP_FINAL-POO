from  PyQt5 import QtWidgets, uic
#from main import app, main, db1, db
from model.permisos import *
from model.main_model import *

# app = QtWidgets.QApplication([])
# main = uic.loadUi('views/main.ui')
# db1 = PersonaDb()
# db = Permisos()

class Main():
        def __init__(self,row,app,main):
            self._row = row
            self._app = app
            self._main = main
            self._mainController = MainController(main)
            if self._row[8] == 1:
                db.mecanico_vista(self._main)
            
            self._mainController.listado_usuarios_mecanicos()
            self._main.pushButton_3.clicked.connect(lambda: main.stackedWidget.setCurrentIndex(0))
            self._main.pushButton_5.clicked.connect(lambda: main.stackedWidget.setCurrentIndex(1))
            self._main.pushButton_4.clicked.connect(lambda: main.stackedWidget.setCurrentIndex(3))
            self._main.pushButton_6.clicked.connect(lambda: main.stackedWidget.setCurrentIndex(2))
            self._main.pushButton.clicked.connect(lambda: main.stackedWidget.setCurrentIndex(4))
            self._main.table_user.cellDoubleClicked.connect(lambda: MainController.cargar_listado_autos(main.table_user.currentRow(),MainController.get_rows) if main.table_user.currentRow() != 1 else None)
            main.table_user.cellDoubleClicked.connect(lambda: main.stackedWidget.setCurrentIndex(5))
            self._main.show()
            app.exec()
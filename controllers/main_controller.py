from  PyQt5 import QtWidgets, uic
from database.database import PermisosDb
from database.database import PersonaDb
from model.model import *

app = QtWidgets.QApplication([])
main = uic.loadUi('views/main.ui')
db1 = PersonaDb()
db = Permisos()

class MainController(): # Logica de negocio
    
    def listado_usuarios_mecanicos(row):
            rows = db1.leer_usuarios()
            c = len(rows[0])
            f = len(rows)
            
            main.table_user.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
            main.table_user.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
            main.table_user.setRowCount(f +1)
            main.table_user.setColumnCount(c)

            for i in range(f):
                for j in range(c):
                    main.table_user.setItem(i+1,j,QtWidgets.QTableWidgetItem(f'{rows[i][j]}'))

            rows = db1.leer_mecanicos()
            c = len(rows[0])
            f = len(rows)
            
            main.Tableuser_2.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
            main.Tableuser_2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
            main.Tableuser_2.setRowCount(f +1)
            main.Tableuser_2.setColumnCount(c)

            for i in range(f):
                for j in range(c):
                    main.Tableuser_2.setItem(i+1,j,QtWidgets.QTableWidgetItem(f'{rows[i][j]}'))
                    
class Main():
        def __init__(self,row):
            self._row = row
            MainController.listado_usuarios_mecanicos(self._row)
            main.pushButton_3.clicked.connect(lambda: main.stackedWidget.setCurrentIndex(0))
            main.pushButton_5.clicked.connect(lambda: main.stackedWidget.setCurrentIndex(1))
            main.pushButton_4.clicked.connect(lambda: main.stackedWidget.setCurrentIndex(3))
            main.pushButton_6.clicked.connect(lambda: main.stackedWidget.setCurrentIndex(2))
            main.pushButton.clicked.connect(lambda: main.stackedWidget.setCurrentIndex(4))
            main.show()
            app.exec()
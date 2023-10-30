from  PyQt5 import QtWidgets, uic
from database.database import PermisosDb
from database.database import PersonaDb
from controllers.login_controller import *
from model.model import *

app = QtWidgets.QApplication([])
main = uic.loadUi('views/main.ui')
db1 = PersonaDb()
db = Permisos()

class Main():
    
    def show_page_3(row):
        rows = db1.leer_todos()
        c = len(rows[0])
        f = len(rows)
        
        main.table_user.setRowCount(f)
        main.table_user.setColumnCount(c)

        for i in range(f):
            for j in range(c):
                main.table_user.setItem(i,j,QtWidgets.QTableWidgetItem(f'{rows[i][j]}'))
                
        # if row[9 ] == "m":
        #     db.mecanico_vista(main)
        #     print(row)
        main.show()
        app.exec()
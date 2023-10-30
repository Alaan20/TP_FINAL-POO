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
        main.table_user.setRowCount(len(rows))
        main.table_user.setColumnCount(len(rows[0]))
        
        for i, row1 in enumerate(rows):
            for j, col in enumerate(row1):
                main.table_user.setItem(rows.index(row1),j,QtWidgets.QTableWidgetItem(str(row1[i])))
                    #print("gug")
        
        # if row[9 ] == "m":
        #     db.mecanico_vista(main)
        #     print(row)
        main.show()
        app.exec()
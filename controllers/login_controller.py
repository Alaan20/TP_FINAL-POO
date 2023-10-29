from typing import Any
from  PyQt5 import QtWidgets, uic
import time
from database.database import PersonaDb

# Iniciar la aplicación
app = QtWidgets.QApplication([])
login = uic.loadUi('views/login.ui')
main = uic.loadUi('views/main.ui')
db = PersonaDb()
        
class LoginController(): # Logica de negocio 
    
    def __init__(self, login_ui):
        self.login_ui = login
        self.db = PersonaDb()
    
    def gui_login(self):
        try:
            name = self.login_ui.user.text()
            password = self.login_ui.password.text()
            row = self.db.leer(name,password)
            
            if len(name)==0 or len(password)==0:
                raise Exception("Por favor, ingrese un usuario y contraseña")
            
            if row is None:
                raise Exception("Usuario o contraseña incorrectos")
            
            self.login_ui.error.setStyleSheet("color: green")
            self.login_ui.error.setText("Iniciando sesión...")
                    
            if str(row[1]) == str("admin") and row[2] == str("admin"):
                LoginController.show_page_2(list(row))
            
            #Main.show_page_3(list(row))
            self.login_ui.close()
        
        except Exception as e:
            self.login_ui.error.setText(str(e))
            
    def show_page_2(self,row):
        try:
            name = self.login_ui.user1.text()
            password = self.login_ui.password1.text()
        
            if len(name)==0 or len(password)==0:
                raise Exception("Por favor, ingrese un usuario y contraseña")
        
            if name =="admin" and password =="admin":
                raise Exception("Ingrese un usuario y contraseña distintos")
            
            row[1] = name
            row[2] = password
            if self.db.actualizar(row) is False:
                raise Exception("Error, revise tu conexión a internet")
                
            self.login_ui.error_1.setStyleSheet("color: green")
            self.login_ui.error_1.setText("Contraseña cambiada con éxito")
            time.sleep(1)
            self.login_ui.close()
            #Main.show_page_3(row)
        
        except Exception as e:
            self.login_ui.error_1.setText(str(e))

class Login():
    
    def __init__(self):
        self.login_controller = LoginController(login)
        login.log_in.clicked.connect(self.login_controller.gui_login)
        login.log_in_1.clicked.connect(lambda: self.login_controller.show_page_2(list()))
        login.show()
        app.exec()

class Main():
    def __init__(self):    
        self.main = main
        self.db = PersonaDb()
        self.rows = self.db.leer_todos()
        
    def show_page_3(self): 
        for i, row in enumerate(self.rows):
            for j, column in enumerate(row):
                self.main.tableWidget.setItem(i,j,QTableWidgetItem(str(column)))
                #self.main.tableWidget.item(i,j).setFlags(QtCore.Qt.ItemIsEnabled)
        main.show()




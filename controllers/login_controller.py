from typing import Any
from  PyQt5 import QtWidgets, uic
import time
from database.database import PersonaDb
from controllers.main_controller import *

class LoginController(): # Logica de negocio 
    
    def __init__(self, login,main,app):
        self.login_ui = login
        self.main = main
        self.app = app
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
            
            Main(row,self.app,self.main)
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
            Main(row,self.app,self.main)
        
        except Exception as e:
            self.login_ui.error_1.setText(str(e))

class Login():
    
    def __init__(self,app,login,main):
        self.login_controller = LoginController(login,main,app)
        login.log_in.clicked.connect(self.login_controller.gui_login)
        login.log_in_1.clicked.connect(lambda: self.login_controller.show_page_2(list()))
        login.show()
        app.exec()
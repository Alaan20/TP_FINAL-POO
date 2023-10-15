from  PyQt5 import QtWidgets, uic
import time
from database.database import PersonaDb
# Iniciar la aplicación
app = QtWidgets.QApplication([])
login = uic.loadUi('views/login.ui')
db = PersonaDb()

# Cargar el archivo .ui
class Login():

    def gui_login(self):
        name = login.user.text()
        password = login.password.text()
        
        if len(name)==0 or len(password)==0:
            login.error.setText("Por favor, ingrese un usuario y contraseña")  
        else:
            if db.leer(name,password) is None:
                login.error.setText("Usuario o contraseña incorrectos")
            else:
                login.error.setStyleSheet("color: green")
                login.error.setText("Iniciando sesión...")
      
            if str(db.leer(name,password)[11]) == str("admin"):
                login.stackedWidget.setCurrentIndex(1)
                login.log_in_1.clicked.connect(Login.show_page_2) 
                # Login.show_page_2(self)

    def show_page_2(self):
        name = login.user1.text()
        password = login.password1.text()
        

        if len(name)==0 or len(password)==0:
            login.error_1.setText("Por favor, ingrese un usuario y contraseña")
        if name =="admin" and password =="admin":
            login.error_1.setText("Ingrese un usuario y contraseña distintos")
        
                   
login.log_in.clicked.connect(Login.gui_login)

login.show()
app.exec()
    # def gui_changePassword(self):
    #     login.changePassword.clicked.connect(self.gui_changePassword)
    # # Ejecutable

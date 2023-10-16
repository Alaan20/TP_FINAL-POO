from  PyQt5 import QtWidgets, uic
import time
from database.database import PersonaDb
# Iniciar la aplicación
app = QtWidgets.QApplication([])
login = uic.loadUi('views/login.ui')
db = PersonaDb()

# Cargar el archivo .ui
class Login():
    
    def gui_login():
        name = login.user.text()
        password = login.password.text()
        row = db.leer(name,password)
        
        if len(name)==0 or len(password)==0:
            login.error.setText("Por favor, ingrese un usuario y contraseña")  
        else:
            if row is None:
                login.error.setText("Usuario o contraseña incorrectos")
            else:
                login.error.setStyleSheet("color: green")
                login.error.setText("Iniciando sesión...")
                print(row)
                if str(row[1]) == str("admin") and row[2] == str("admin"):
                    login.stackedWidget.setCurrentIndex(1)
                    print(row)
                    login.log_in_1.clicked.connect(lambda: Login.show_page_2(list(row))) 

    def show_page_2(row):
        name = login.user1.text()
        password = login.password1.text()
        
        print("hh")
        if len(name)==0 or len(password)==0:
            login.error_1.setText("Por favor, ingrese un usuario y contraseña")
        else:
            if name =="admin" and password =="admin":
                login.error_1.setText("Ingrese un usuario y contraseña distintos")
            else:
                row[2] = name
                row[3] = password
                db.actualizar(row)
                   
login.log_in.clicked.connect(Login.gui_login)

login.show()
app.exec()
    # def gui_changePassword(self):
    #     login.changePassword.clicked.connect(self.gui_changePassword)
    # # Ejecutable

from  PyQt5 import QtWidgets, uic
import time
from database.database import PersonaDb
# Iniciar la aplicación
app = QtWidgets.QApplication([])
login = uic.loadUi('views/login.ui')
main = uic.loadUi('views/main.ui')
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
                if str(row[1]) == str("admin") and row[2] == str("admin"):
                    login.stackedWidget.setCurrentIndex(1)
                    login.log_in_1.clicked.connect(lambda: Login.show_page_2(list(row))) 
                
                time.sleep(1)
                login.close()
                app.quit()
                login.log_in.clicked.connect(main.show())
        # login.stackedWidget.setCurrentIndex(2)
        # login.log_in_2.clicked.connect(lambda: Login.show_page_3(row))
        
    def show_page_2(row):
        name = login.user1.text()
        password = login.password1.text()
        
        if len(name)==0 or len(password)==0:
            login.error_1.setText("Por favor, ingrese un usuario y contraseña")
        else:
            if name =="admin" and password =="admin":
                login.error_1.setText("Ingrese un usuario y contraseña distintos")
            else:
                row[1] = name
                row[2] = password
                if db.actualizar(row) is False:
                 login.error_1.setText("Error, revise tu conexión a internet")
                else:
                    login.error_1.setStyleSheet("color: green")
                    login.error_1.setText("Contraseña cambiada con éxito")
                    time.sleep(1)
                    login.close()
                    app.quit()
                    # login.stackedWidget.setCurrentIndex(2)
                    # login.log_in_2.clicked.connect(lambda: Login.show_page_3(row))
    
    # def show_page_3(row):
login.log_in.clicked.connect(Login.gui_login)

login.show()
app.exec()
    # def gui_changePassword(self):
    #     login.changePassword.clicked.connect(self.gui_changePassword)
    # # Ejecutable

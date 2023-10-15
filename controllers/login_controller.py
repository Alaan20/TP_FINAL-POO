from  PyQt5 import QtWidgets, uic
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
        login.log_in.clicked.connect(self.gui_login)
    # Ejecutable
    login.show()
    app.exec()
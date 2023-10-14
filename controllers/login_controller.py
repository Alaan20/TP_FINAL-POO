from  PyQt5 import QtWidgets, uic
from database.database import PersonaDb
from views import *
# Iniciar la aplicación
app = QtWidgets.QApplication([])

# Cargar el archivo .ui
login = uic.loadUi('views/login.ui')

def gui_login():
    db = PersonaDb()
    name = login.user.text()
    password = login.password.text()
    if len(name)==0 or len(password)==0:
        login.error.setText("Por favor, ingrese un usuario y contraseña")  
    else:
        if db.leer(name,password) is None:
            login.error.setText("Usuario o contraseña incorrectos")
        else:
            login.error.setText("Iniciando sesión...")
login.log_in.clicked.connect(gui_login)

# Ejecutable
login.show()
app.exec()
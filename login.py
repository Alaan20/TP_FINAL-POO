from  PyQt5 import QtWidgets, uic
from database.database import Persona,PersonaDb
# Iniciar la aplicación
app = QtWidgets.QApplication([])

# Cargar el archivo .ui
login = uic.loadUi('login.ui')

def gui_login():
    db = PersonaDb()
    name = login.user.text()
    password = login.password.text()
    if len(name)==0 or len(password)==0:
        login.error.setText("Por favor, ingrese un usuario y contraseña")  
    else:
<<<<<<< HEAD
        if PersonaDb.leer(self,name) is not None:
=======
        if db.leer(name) is None:
>>>>>>> 2619223cb684b200ca692fd4cab9d5cf0e6907ad
            login.error.setText("Usuario o contraseña incorrectos")
login.log_in.clicked.connect(gui_login)

# Ejecutable
login.show()
app.exec()
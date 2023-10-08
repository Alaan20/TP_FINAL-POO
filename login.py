from  PyQt5 import QtWidgets, uic

# Iniciar la aplicación
app = QtWidgets.QApplication([])

# Cargar el archivo .ui
login = uic.loadUi("C:/login.ui")

def gui_login():
    name = login.user.text()
    password = login.user.text()
    if len(name)==0 or len(password)==0:
        login.error.setText("Por favor, ingrese un usuario y contraseña")  
    else:
        login.error.setText("Usuario o contraseña incorrectos")
login.log_in.clicked.connect(gui_login)
# Ejecutable
login.show()
app.exec()
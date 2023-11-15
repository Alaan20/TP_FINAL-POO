from controllers.login_controller import Login
from views import *
from  PyQt5 import QtWidgets, uic
from database.usuariodao import PersonaDb
from model.permisos import *
from model.login import *

app = QtWidgets.QApplication([])
login = uic.loadUi('views/login.ui')
main = uic.loadUi('views/main.ui')
db1 = PersonaDb()

Login(app,login,main)

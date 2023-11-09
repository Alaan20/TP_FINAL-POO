from controllers.login_controller import Login
from views import *
from  PyQt5 import QtWidgets, uic
from database.database import PersonaDb
from model.permisos import *
from model.login import *
app = QtWidgets.QApplication([])
login = uic.loadUi('views/login.ui')
main = uic.loadUi('views/main.ui')
db1 = PersonaDb()
db = Permisos()

Login(app,login,main)

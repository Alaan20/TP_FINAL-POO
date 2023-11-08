from controllers import login_controller
from views import *
from  PyQt5 import QtWidgets, uic
from database.database import PersonaDb
from model.permisos import *

app = QtWidgets.QApplication([])
login = uic.loadUi('views/login.ui')
main = uic.loadUi('views/main.ui')
db1 = PersonaDb()
db = Permisos()

login_controller.Login(app,login,main)

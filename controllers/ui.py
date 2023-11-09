from controllers.login_controller import Login
from views import *
from  PyQt5 import QtWidgets, uic
from database.database import PersonaDb
from model.permisos import *
from model.login import *

class ui:
    def __init__(self):
        self._app = QtWidgets.QApplication([])
        self._login = uic.loadUi('views/login.ui')
        self._main = uic.loadUi('views/main.ui')
        self._db1 = PersonaDb()
        self._db = Permisos()
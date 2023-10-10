import psycopg2
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore
# from  PyQt5 import uic, QtWidgets
# app2 = QtWidgets.QApplication([])
# login = uic.loadUi('login.ui')

class Window(QMainWindow):
    
    def __init__(self):
        super(QMainWindow,self).__init__()
        self.layout_vertical= QVBoxLayout()
        self.user = QLineEdit('user')
        self.passw = QLineEdit('pass')
        self.btn = QPushButton('ola')
        self.layout_vertical.addWidget(self.user)
        self.layout_vertical.addWidget(self.passw)
        self.layout_vertical.addWidget(self.btn)
        self.btn.clicked.connect(self.valido)
        self.widget = QWidget()
        self.widget.setLayout(self.layout_vertical)
        self.setCentralWidget(self.widget)
    
    def valido (self):
        try:
            conexion=psycopg2.connect(database="base_prueba", user="postgres", password="bd2372")
            cursor01=conexion.cursor()
            cursor01.execute('select version()')
            version=cursor01.fetchone()
        except Exception as err:
            print('Erro al conectar a la base\n',err)
        else:
            print(f'{version}')
        # if self.passw == None or self.user.text() == :
        #     print('los campos estan vacios')
        cursor01.execute(f"select * from usuarios where clave='{str(self.passw.text())}'  and nombre='{str(self.user.text())}'")
        consulta = cursor01.fetchone()
        # if consulta[3] == 'C':
        #     self.gui_login()
        print(consulta)
        conexion.close()
    
    # def gui_login(self):
    #     l=QLabel('ola')
    #     ly=QVBoxLayout()
    #     ly.addWidget(l)
    #     w1 = QWidget()
    #     w1.setLayout(ly)
    #     self.setCentralWidget(w1)
        # login.show()
        # app2.exec_()
        # name = login.user.text()
        # password = login.password.text()
        # if len(name)==0 or len(password)==0:
        #     login.error.setText("Por favor, ingrese un usuario y contraseña")  
        # elif PersonaDb.leer(name) is None:
        #     login.error.setText("Usuario o contraseña incorrectos")
        # login.log_in.clicked.connect(login)
        # self.setCentralWidget(w1)
        # login.show()
        # app.exec()

# Ejecutable
# login.show()


app = QApplication (sys.argv)
window = QMainWindow()
window = Window()
window.show()
sys.exit(app.exec_())
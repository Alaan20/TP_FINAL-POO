import psycopg2
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


class MainWindow (QMainWindow):
    
    def __init__(self):
        super(QMainWindow, self).__init__()
        self._connection = psycopg2.connect(
            user="postgres",
            password="teclas",
            host="tpphost.duckdns.org",
            port="5432",
            database="[autosoft]"
        )
        layout_2 = QVBoxLayout()
        
        self.user = QLineEdit('user')
        self.passw = QLineEdit('pass')
        btn1 = QPushButton("Validar")
        layout_2.addWidget(self.user)
        layout_2.addWidget(self.passw)
        layout_2.addWidget(btn1)
        btn1.clicked.connect(self.valido)
        
        btn2 = QPushButton("Impresion de usuarios")
        btn2.pressed.connect(self.inserto)
        layout_2.addWidget(btn2)
        
        self.widget = QWidget()
        self.widget.setLayout(layout_2)
        self.setCentralWidget(self.widget)

    def valido (self):
        self._cursor =self._connection.cursor()
        self._cursor.execute(
            f"select usuario,clave,nombre,apellido from usuarios where clave='{str(self.passw.text())}' and usuario='{str(self.user.text())}'"
            )
        consulta = self._cursor.fetchone()
        lbl1 = QLabel(f"Hola {consulta[2]+ ' ' + consulta[3]}")
        layout_3 = QVBoxLayout()
        layout_3.addWidget(lbl1)
        
        self.user2 = QLineEdit('nombre nuevo')
        self.passw2 = QLineEdit('apellido nuevo')
        btn3 = QPushButton("Actualizar")
        layout_3.addWidget(self.user2)
        layout_3.addWidget(self.passw2)
        layout_3.addWidget(btn3)
        btn3.clicked.connect(self.actualizo)
        self.clave = self.passw2.text()
        self.usuario = self.user2.text()
        wid = QWidget()
        wid.setLayout(layout_3)
        self.setCentralWidget(wid)

    def actualizo(self):
        self._cursor =self._connection.cursor()
        self._cursor.execute(f"UPDATE usuarios  SET nombre ='{self.user2.text()}',apellido ='{self.passw2.text()}' where clave='{self.clave}' and usuario='{self.usuario}'")
        self.imprimo_actu()
    
    def imprimo_actu (self):
        self._cursor =self._connection.cursor()
        self._cursor.execute(
            f"select usuario,clave,nombre,apellido from usuarios where clave='{self.clave}' and usuario='{self.usuario}'"
            )
        consulta2 = self._cursor.fetchone()
        lbl1 = QLabel(f"Hola {consulta2[2]+ ' ' + consulta2[3]}")
        lbl2 = QLabel(f"Usuario: {consulta2[0]}, Contraseña: {consulta2[1]}")
        layout_3 = QVBoxLayout()
        layout_3.addWidget(lbl1)
        layout_3.addWidget(lbl2)
        wid2 = QWidget()
        wid2.setLayout(layout_3)
        self.setCentralWidget(wid2)

    def inserto (self):
        layout= QVBoxLayout()
        self.tabla = QTableWidget()
        self.tabla.setObjectName("Persona")
        self._cursor =self._connection.cursor()
        self._cursor.execute(f"select usuario, clave,nombre, apellido,dni,tipo from usuarios")

        v = self._cursor.fetchall()
        c = len(v[0])
        f = len(v)
        self.tabla.setRowCount(f)
        self.tabla.setColumnCount(c)

        for i in range(f):
            for j in range(c):
                self.tabla.setItem(i,j,QTableWidgetItem(f'{v[i][j]}'))
        
        self.tabla.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabla.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.tabla.cellClicked.connect(self.reviso)
        layout.addWidget(self.tabla)
        w = QWidget()
        w.setLayout(layout)
        self.setCentralWidget(w)

    def reviso(self):
        self.tabla.selectRow(self.tabla.currentRow())


app = QApplication(sys.argv)
window = QMainWindow()
window = MainWindow()
window.show()
sys.exit(app.exec_())
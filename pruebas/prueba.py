import psycopg2
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


class MainWindow (QMainWindow):
    
    def __init__(self):
        super(QMainWindow, self).__init__()
        self._connection = psycopg2.connect(
            user ="postgres",
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
        
        btn3 = QPushButton("Eliminar Usuario")
        btn3.pressed.connect(self.eliminar)
        layout_2.addWidget(btn3)
        
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
        self.nombre = consulta[0]
        self.contra = consulta[1]
        layout_3 = QVBoxLayout()
        layout_3.addWidget(lbl1)
        
        self.user2 = QLineEdit('nombre nuevo')
        self.passw2 = QLineEdit('apellido nuevo')
        btn3 = QPushButton("Actualizar")
        layout_3.addWidget(self.user2)
        layout_3.addWidget(self.passw2)
        layout_3.addWidget(btn3)
        btn3.clicked.connect(self.actualizo)
        wid = QWidget()
        wid.setLayout(layout_3)
        self.setCentralWidget(wid)

    def actualizo(self):
        self._cursor =self._connection.cursor()
        self._cursor.execute(f"UPDATE usuarios SET nombre ='{str(self.user2.text())}',apellido ='{str(self.passw2.text())}' where clave='{self.contra}' and usuario='{self.nombre}'")
        self.imprimo_actu()
    
    def imprimo_actu (self):
        self._cursor =self._connection.cursor()
        self._cursor.execute(
            f"select usuario,clave,nombre,apellido from usuarios where clave='{self.contra}' and usuario='{self.nombre}'"
            )
        consulta2 = self._cursor.fetchone()
        print(consulta2)
        self._connection.commit()

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
    
    def eliminar(self):
        layout_4 = QVBoxLayout()
        self.user4 = QLineEdit('nombre_usuario del usuario a eliminar')
        self.passw4 = QLineEdit('clave del usuario a eliminar')
        btn4 = QPushButton("Presione para eliminar")
        layout_4.addWidget(self.user4)
        layout_4.addWidget(self.passw4)
        layout_4.addWidget(btn4)
        btn4.clicked.connect(self.actualizo_borrado)
        wid3 = QWidget()
        wid3.setLayout(layout_4)
        self.setCentralWidget(wid3)

    def actualizo_borrado (self):
        self._cursor =self._connection.cursor()
        self._cursor.execute(f"DELETE FROM usuarios WHERE usuario= '{self.user4.text()}' and clave = '{self.passw4.text()}'")
        self._connection.commit()
        self.imprimo_actu_borrado()
    
    def imprimo_actu_borrado(self):
        self._cursor =self._connection.cursor()
        self._cursor.execute("select * from usuarios")
        consulta = self._cursor.fetchall()
        print(consulta)

    def reviso(self):
        self.tabla.selectRow(self.tabla.currentRow())

app = QApplication(sys.argv)
window = QMainWindow()
window = MainWindow()
window.show()
sys.exit(app.exec_())
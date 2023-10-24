import psycopg2
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class seleccion(Exception):
    pass

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
        
        self.user = QLineEdit()
        self.user.setPlaceholderText('Usuario')
        self.passw = QLineEdit()
        self.passw.setPlaceholderText('Contraseña')
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
        
        btn4 =QPushButton("agregar usuario")
        btn4.pressed.connect(self.interfaz_agregar)
        layout_2.addWidget(btn4)
        
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
        
        self.user2 = QLineEdit()
        self.user2.setPlaceholderText('nuevo nombre')
        self.passw2 = QLineEdit()
        self.passw2.setPlaceholderText('nuevo apellido')
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
        self._cursor.execute(f"select usuario, clave,nombre, apellido,dni,id_rol from usuarios")

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
        self.user4 = QLineEdit()
        self.user4.setPlaceholderText('ingrese el usuario a eliminar')
        self.passw4 = QLineEdit()
        self.passw4.setPlaceholderText('ingrese contraseña a eliminar')
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

    def interfaz_agregar(self):
        lbl=QLabel("Agregar usuario:")
        lbl2=QLabel("los campos marcados con * son obligatorios")
        
        
        usuario_y_contraseña=QGroupBox("usuario y contraseña:")
        self._nombre_usuario=QLineEdit()
        self._nombre_usuario.setPlaceholderText("nombre de usuario (*)")
        self._contrasenia=QLineEdit()
        self._contrasenia.setPlaceholderText("contraseña (*)")
        group_layout1=QVBoxLayout()
        group_layout1.addWidget(self._nombre_usuario)
        group_layout1.addWidget(self._contrasenia)
        usuario_y_contraseña.setLayout(group_layout1)
        
        datos_personales=QGroupBox("datos personales:")
        self._nombre=QLineEdit()
        self._nombre.setPlaceholderText("nombre (*)")
        self._apellido=QLineEdit()
        self._apellido.setPlaceholderText("apellido (*)")
        self._dni=QLineEdit()
        self._dni.setPlaceholderText("dni (*)")
        group_layout2=QVBoxLayout()
        group_layout2.addWidget(self._nombre)
        group_layout2.addWidget(self._apellido)
        group_layout2.addWidget(self._dni)
        datos_personales.setLayout(group_layout2)
        
        contacto=QGroupBox("contacto")
        self._email=QLineEdit()
        self._email.setPlaceholderText("e-mail")
        self._nro_telefono=QLineEdit()
        self._nro_telefono.setPlaceholderText("telefono")
        group_layout3=QVBoxLayout()
        group_layout3.addWidget(self._email)
        group_layout3.addWidget(self._nro_telefono)
        contacto.setLayout(group_layout3)
        
        rol=QGroupBox("rol")
        self.cliente=QRadioButton("cliente")
        self.mecanico=QRadioButton("mecanico")
        self.administrativo=QRadioButton("administrativo")
        group_layout4=QHBoxLayout()
        group_layout4.addWidget(self.cliente)
        group_layout4.addWidget(self.mecanico)
        group_layout4.addWidget(self.administrativo)
        self._id_rol=None
        
        rol.setLayout(group_layout4)
        
        
        self.agregar=QPushButton("agregar ususario")
        self.agregar.clicked.connect(self.agregar_usuario)
        
        
        layout=QVBoxLayout()
        layout.addWidget(lbl)
        layout.addWidget(lbl2)
        layout.addWidget(usuario_y_contraseña)
        layout.addWidget(datos_personales)
        layout.addWidget(contacto)
        layout.addWidget(rol)
        layout.addWidget(self.agregar)
        contenedor=QWidget()
        contenedor.setLayout(layout)
        self.setCentralWidget(contenedor)
        self.setWindowTitle("agregar usuario")
        
    def validar_datos(self,variable,lista:list):
            if not variable:
                raise seleccion("campos obligatorios vacios")
            lista.append(variable)
        
    def agregar_usuario(self):
        llave=True
        try:
            lista=[]
            if self.cliente.isChecked():
                self._id_rol=int(0)
            elif self.mecanico.isChecked():
                self._id_rol=int(1)
            elif self.administrativo.isChecked():
                self._id_rol=int(2)
            else:
                raise seleccion("seleccione un rol")
            
            try:
                self.validar_datos(self._nombre_usuario.text(),lista)
                self.validar_datos(self._contrasenia.text(),lista)
                self.validar_datos(self._nombre.text(),lista)
                self.validar_datos(self._apellido.text(),lista)
                self.validar_datos(self._dni.text(),lista)
            except seleccion as e:
                llave=False
                QMessageBox.critical(self,"error",str(e))
            if llave==True:
                lista.append(self._id_rol)
                for i in range(len(lista)):
                    if not lista[i]:
                        lista[i]+='null'
                self._cursor =self._connection.cursor()
                self._cursor.execute(f"insert into usuarios (usuario,clave,nombre,apellido,dni,id_rol,estado) values ('{self._nombre_usuario.text()}','{self._contrasenia.text()}','{self._nombre.text()}','{self._apellido.text()}','{self._dni.text()}','{self._id_rol}','a')")
                self._connection.commit()
                print(lista)
        except seleccion as e:
            QMessageBox.critical(self,"error",str(e))
        
        

    def reviso(self):
        self.tabla.selectRow(self.tabla.currentRow())

app = QApplication(sys.argv)
window = QMainWindow()
window = MainWindow()
window.show()
sys.exit(app.exec_())
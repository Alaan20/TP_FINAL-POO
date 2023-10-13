# chequear si la base de datos usuarios.db existe
# si no existe, crearla
import sqlite3
import os.path
from os import path
import psycopg2

def conectar_base_de_datos():
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="teclas",
            host="tpphost.duckdns.org",
            port="5432",
            database="[autosoft]"
        )
        return connection
    except (Exception, psycopg2.Error) as error:
        print("Error al conectar a la base de datos:", error)
        return None

    
class PersonaDb:
    def __init__(self):
        self._conn = sqlite3.connect('usuarios.db')
        self._cursor = self._conn.cursor()
    
    def crear(self,persona):
        self._cursor.execute("INSERT INTO usuarios (usuario, contraseña, tipo) VALUES (?,?,?)",(persona._usuario,persona._contraseña,persona._tipo)) 
        self._conn.commit()
        
    def leer(self,usuario,clave):
        self._cursor.execute(f"SELECT * FROM usuarios WHERE nombre_usuario = '{usuario}' AND contraseña = '{clave}'")
        row = self._cursor.fetchone()
        return row[0],row[1],row[2]
        
    def actualizar(self,persona):
        self._cursor.execute("UPDATE usuario=?, contraseña=? WHERE tipo=?",(persona._usuario,persona._contraseña,persona._tipo))
        self._conn.commit()
    
    def borrado(self,usuario):
        self._cursor.execute("DELETE FROM usuarios WHERE usuario=?",(persona._usuario,))
        self._conn.commit()
    
        self._conn.close()

usuario1=Persona("admin","admin123","admin")
usuario3=Persona("usuario12","pass123","usuario")
bd = PersonaDb()
# bd.crear(usuario1)
# bd.buscar(usuario3._usuario)

# if  bd.leer(usuario3._usuario) is not None:
#      print("El usuario ya existe")
# else:
#      bd.crear(usuario3)
#      print("El usuario fue creado")
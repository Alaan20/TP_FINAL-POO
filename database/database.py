# chequear si la base de datos usuarios.db existe
# si no existe, crearla
import sqlite3
import os.path
from os import path

class Persona:
    def __init__(self,usuario,contraseña):
        self._usuario = usuario
        self._contraseña = contraseña
    

class PersonaDb:
    def __init__(self):
        self._conn = sqlite3.connect('usuarios.db')
        self._cursor = self._conn.cursor()
    
    def crear(self,persona):
        self._cursor.execute("INSERT INTO usuarios (usuario, contraseña, tipo) VALUES (?,?,?)",(persona._usuario,persona._contraseña,persona._tipo)) 
        self._conn.commit()
        
    def leer(self,usuario):
        self._cursor.execute("SELECT * FROM usuarios WHERE usuario={}".format(usuario))
        row = self._cursor.fetchone()
        return row[0],row[1],row[2]
        # return Persona(row[0],row[1],row[2])
        
    def actualizar(self,persona):
        self._cursor.execute("UPDATE usuario=?, contraseña=? WHERE tipo=?",(persona._usuario,persona._contraseña,persona._tipo))
        self._conn.commit()
    
    # def borrado(self,usuario):
    #     self._cursor.execute("DELETE FROM usuarios WHERE usuario=?",(persona._usuario,))
    #     self._conn.commit()
    
    #     self._conn.close()

# bd = PersonaDb()
# # bd.crear(usuario1)
# bd.buscar(usuario3._usuario)

# if  bd.leer(usuario3._usuario) is not None:
#      print("El usuario ya existe")
# else:
#      bd.crear(usuario3)
#      print("El usuario fue creado")
# chequear si la base de datos usuarios.db existe
# si no existe, crearla
import sqlite3
import os.path
from os import path

class Persona:
    def __init__(self,usuario,contraseña,tipo):
        self._usuario = usuario
        self._contraseña = contraseña
        self._tipo = tipo
    
    # @property
    # def usuario(self):
    #     return self._usuario
    
    # @property
    # def contraseña(self):
    #     return self._contraseña
    
    # @property
    # def tipo(self):
    #     return self._tipo
    
    # @usuario.setter
    # def mostrarusuario(self):
    #     return self._usuario
    
    # @contraseña.setter
    # def mostrarcontraseña(self):
    #     return self._contraseña

    # @tipo.setter
    # def mostrartypo(self):
    #     return self._tipo

class PersonaDb:
    def __init__(self):
        self._conn = sqlite3.connect('usuarios.db')
        self._cursor = self._conn.cursor()
    
    def crear(self,persona):
        self._cursor.execute("INSERT INTO usuarios (usuario, contraseña, tipo) VALUES (?,?,?)",(persona._usuario,persona._contraseña,persona._tipo)) 
        self._conn.commit()
        
    def leer(self,usuario):
        self._cursor.execute("SELECT * FROM usuarios WHERE usuario=?",(usuario,))
        row = self._cursor.fetchone()
        return Persona(row[0],row[1],row[2])
        
    def actualizar(self,persona):
        self._cursor.execute("UPDATE usuario=?, contraseña=? WHERE tipo=?",(persona._usuario,persona._contraseña,persona._tipo))
        self._conn.commit()
    
    def borrado(self,usuario):
        self._cursor.execute("DELETE FROM usuarios WHERE usuario=?",(persona._usuario,))
        self._conn.commit()
    
        self._conn.close()

usuario1=Persona("admin","admin123","admin")
usuario3=Persona("usuario12","pass123","usuario")
# bd = PersonaDb()
# # bd.crear(usuario1)
# bd.buscar(usuario3._usuario)

# if  bd.leer(usuario3._usuario) is not None:
#      print("El usuario ya existe")
# else:
#      bd.crear(usuario3)
#      print("El usuario fue creado")
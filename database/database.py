import psycopg2
import sqlite3

class Conection():
    def __init__(self):
        self._connection = psycopg2.connect(
            user="postgres",
            password="teclas",
            host="tpphost.duckdns.org",
            port="5432",
            database="[autosoft]"
        )
        
class PersonaDb(Conection):
    def __init__(self):
        super().__init__()
        self._cursor =  self._connection.cursor()
    
    def crear(self,persona):
        self._cursor.execute("INSERT INTO usuarios (usuario, contraseña, tipo) VALUES (?,?,?)",(persona._usuario,persona._contraseña,persona._tipo)) 
        self._conn.commit()
        
    def leer(self,usuario,clave):
        self._cursor.execute(f"SELECT * FROM usuarios WHERE usuario = '{usuario}' AND clave = '{clave}'")
        row = self._cursor.fetchone()
        return row
        
    def actualizar(self,row):
        self._cursor.execute("SELECT * FROM usuarios WHERE id_usuario = %s", (row[0],))
        if self._cursor.fetchone() is not None:
            self._cursor.execute("UPDATE usuarios SET usuario = %s, clave = %s,nombre = %s, apellido = %s, dni = %s, correo_electronico = %s, nro_telefono = %s, id_rol = %s, estado = %s, tipo = %s, dir_calle = %s, dir_ciudad = %s, dir_provincia = %s, dir_codigopostal = %s, dir_pais = %s", (row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11],row[12],row[13],row[14],row[15]))
            self._connection.commit()
            return True
            print("true")
        else:
            return False
            print("false")
        
    def borrado(self,usuario):
        self._cursor.execute("DELETE FROM usuarios WHERE usuario= '{usuario}'")
        self._conn.commit()
    
        self._conn.close()

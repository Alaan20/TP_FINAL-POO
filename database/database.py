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
        self._cursor.execute(f"INSERT INTO usuarios (usuario, contraseña, tipo) VALUES ({persona._usuario},{persona._contraseña},{persona._tipo})") 
        self._conn.commit()
        
    def leer(self,usuario,clave):
        self._cursor.execute(f"SELECT * FROM usuarios WHERE usuario = '{usuario}' AND clave = '{clave}'")
        row = self._cursor.fetchone()
        return row
        
    def actualizar(self,row):
        self._cursor.execute(f"SELECT * FROM usuarios WHERE id_usuario = '{row[0]}'")
        self.setcolumn(row)
        if self._cursor.fetchone() is not None:
            self._cursor.execute(f"UPDATE usuarios SET usuario ={row[1]},clave ={row[2]},nombre ={row[3]},apellido ={row[4]},dni ={row[5]},correo_electronico={row[6]} WHERE id_usuario = {row[0]}")
            self._connection.commit()
            return True
        else:
            return False
    def setcolumn(self,row):
        cadena=""
        long = 0
        for fila in row:
            if fila==None:
                cadena+="null"
                fila=cadena
            else:
                cadena=f"'{fila}'"
                fila=cadena
            row[long]=fila
            long += 1
        return row
        
    def borrado(self,usuario):
        self._cursor.execute(f"DELETE FROM usuarios WHERE usuario= '{usuario}'")
        self._conn.commit()
    
        self._conn.close()

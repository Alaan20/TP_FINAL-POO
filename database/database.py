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
        self._cursor.execute(f"SELECT * FROM usuarios WHERE id_usuario = '{int(row[0])}'")
        if self._cursor.fetchone() is not None:
            self._cursor.execute(f"UPDATE usuarios SET usuario ='row[1]', clave ='row[2]',nombre ='row[3]', apellido ='row[4]', dni ='{int(row[5])}', correo_electronico ='row[6]', nro_telefono ='{int(row[7])}', id_rol ='row[8]', estado ='row[9]', tipo ='row[10]', dir_calle ='row[11]', dir_ciudad ='row[12]', dir_provincia ='row[13]', dir_codigopostal ='row[14]', dir_pais ='row[15]' WHERE id_usuario = '{int(row[0])}'")
            self._connection.commit()
            return True
        else:
            return False
        
    def borrado(self,usuario):
        self._cursor.execute("DELETE FROM usuarios WHERE usuario= '{usuario}'")
        self._conn.commit()
    
        self._conn.close()

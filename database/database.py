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
        self._cursor.execute(f"SELECT * FROM usuarios WHERE nombre_usuario = '{usuario}' AND contraseña = '{clave}'")
        row = self._cursor.fetchone()
        return row
        
    def actualizar(self,persona):
        self._cursor.execute("UPDATE usuario=?, contraseña=? WHERE tipo=?",(persona._usuario,persona._contraseña,persona._tipo))
        self._conn.commit()
    
    def borrado(self,usuario):
        self._cursor.execute("DELETE FROM usuarios WHERE usuario=?",(persona._usuario,))
        self._conn.commit()
    
        self._conn.close()

# db = PersonaDb()
# des = db.leer("admin","admin")
# if des is not None:
#     print("El usuario ya existe")
# else:
#     print("El usuario fue creado")
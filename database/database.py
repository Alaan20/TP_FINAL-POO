import psycopg2

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
    
    def crear(self,persona: list,rol):
        if persona[6]=='null':
            self._cursor.execute(f"insert into usuarios (usuario,clave,nombre,apellido,dni,correo_electronico,nro_telefono,id_rol,estado) values ('{persona[0]}','{persona[1]}','{persona[2]}','{persona[3]}','{persona[4]}',{persona[5]},{persona[6]},'{rol}','a')") 
            self._connection.commit()
        else:
            self._cursor.execute(f"insert into usuarios (usuario,clave,nombre,apellido,dni,correo_electronico,nro_telefono,id_rol,estado) values ('{persona[0]}','{persona[1]}','{persona[2]}','{persona[3]}','{persona[4]}','{persona[5]}','{persona[6]}','{rol}','a')") 
            self._connection.commit()
        
    def leer(self,usuario,clave):
        self._cursor.execute(f"SELECT * FROM usuarios WHERE usuario = '{usuario}' AND clave = '{clave}'")
        row = self._cursor.fetchone()
        return row
    
    # def obtener_nombres_columnas(self):
    #     self._cursor.execute("SELECT * FROM usuarios LIMIT 0")
    #     nombres_columnas = [description[0] for description in self._cursor.description]
    #     return nombres_columnas

    def actualizar(self,row):
        self._cursor.execute(f"SELECT * FROM usuarios WHERE id_usuario = '{row[0]}'")
        if self._cursor.fetchone() is not None:
            self._cursor.execute(f"UPDATE usuarios SET usuario ='{row[1]}', clave ='{row[2]}', nombre ='{row[3]}', apellido ='{row[4]}', dni ='{row[5]}', correo_electronico='{row[6]}' WHERE id_usuario = '{row[0]}'")
            self._connection.commit()
            return True
        else:
            return False
    
    def actualizar_admin(self,usuario,clave):
        self._cursor.execute(f"UPDATE usuarios SET usuario ='{usuario}', clave ='{clave}' WHERE id_usuario = 1")
        self._connection.commit()
        
        
    def setcolumn(self, row):
        row = [f"'{fila}'" if fila is not None else "null" for fila in row]
        return row
        
    def borrado(self,usuario):
        self._cursor.execute(f"UPDATE usuarios SET estado='i' WHERE id_usuario={usuario}")
        self._connection.commit()

    def leer_usuarios(self):
            self._cursor.execute("SELECT id_usuario, usuario, nombre, apellido, dni, correo_electronico, nro_telefono FROM usuarios WHERE id_rol = 2 and estado='a' ")
            rows = self._cursor.fetchall()
            return rows
    
    def leer_mecanicos(self):
            self._cursor.execute("SELECT id_usuario, usuario, nombre, apellido, dni, correo_electronico, nro_telefono FROM usuarios WHERE id_rol = 1 and estado='a' ")
            rows = self._cursor.fetchall()
            return rows

class AutosDb(Conection):
    def __init__(self):
        super().__init__()
        self._cursor =  self._connection.cursor()
        
    def leer_autos(self,numero):
            self._cursor.execute(f"SELECT * FROM autos WHERE id_dueño = '{numero}'")
            rows = self._cursor.fetchall()
            return rows
    
    def agregar_autos(self,row):
        self._cursor.execute(f"insert into autos (patente,id_dueño,marca,modelo,año,kilometros,tipo_combustible,notas) values ('{row[0]}',{row[1]},'{row[2]}','{row[3]}',{row[4]},{row[5]},'{row[6]}','{row[7]}')")
        self._connection.commit()
        
    def actualizar_auto(self,row):
        self._cursor.execute(f"SELECT * FROM autos WHERE patente = '{row[0]}'")
        if self._cursor.fetchone() is not None:
            self._cursor.execute(f"UPDATE autos SET marca ='{row[2]}', modelo ='{row[3]}', año ='{row[4]}', kilometros ='{row[5]}', tipo_combustible='{row[6]}', notas='{row[7]}' WHERE patente = '{row[0]}'")
            self._connection.commit()
            
    def borrar_auto(self,patente):
        self._cursor.execute(f"DELETE FROM autos WHERE patente = '{patente}'")
        self._connection.commit()


class PermisosDb(Conection):
    def __init__(self):
        super().__init__()
        self._cursor =  self._connection.cursor()
        
    def leer(self,rol):
        self._cursor.execute(f"SELECT * FROM roles WHERE id_rol = '{rol}'")
        row = self._cursor.fetchall()
        return row
    
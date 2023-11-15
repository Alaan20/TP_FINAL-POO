from database.database import DataBase

class PersonaDb:
    def __init__(self):
        self.base = DataBase()
    
    def leer(self, usuario, clave):
        return self.base.get("SELECT * FROM usuarios WHERE usuario = '{}' and clave = '{}'".format(usuario, clave))
    
    def crear(self,persona: list,rol):
        if persona[6]=='null':
            return self.base.query("insert into usuarios (usuario,clave,nombre,apellido,dni,correo_electronico,nro_telefono,id_rol,estado) values ('{}','{}','{}','{}','{}',{},null,'{}','a')".format(persona[0],persona[1],persona[2],persona[3],persona[4],persona[5],rol))
        else:
            return self.base.query("insert into usuarios (usuario,clave,nombre,apellido,dni,correo_electronico,nro_telefono,id_rol,estado) values ('{}','{}','{}','{}','{}','{}','{}','{}','a')".format(persona[0],persona[1],persona[2],persona[3],persona[4],persona[5],persona[6],rol))

    def actualizar(self,row):
        return self.base.query(f"UPDATE usuarios SET usuario ='{row[1]}', clave ='{row[2]}', nombre ='{row[3]}', apellido ='{row[4]}', dni ='{row[5]}', correo_electronico='{row[6]}' WHERE id_usuario = '{row[0]}'")

    def borrado(self,usuario):
        return self.base.query(f"UPDATE usuarios SET estado='i' WHERE id_usuario={usuario}")
    
    def actualizar_admin(self,usuario,clave):
        return self.base.query(f"UPDATE usuarios SET usuario ='{usuario}', clave ='{clave}' WHERE id_usuario = 1")
    
    def leer_usuarios(self):
        return self.base.getAll("SELECT id_usuario, usuario, nombre, apellido, dni, correo_electronico, nro_telefono FROM usuarios WHERE id_rol = 2 and estado='a' ")
    
    def leer_mecanicos(self):
        return self.base.getAll("SELECT id_usuario, usuario, nombre, apellido, dni, correo_electronico, nro_telefono FROM usuarios WHERE id_rol = 1 and estado='a' ")

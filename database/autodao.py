from database.database import DataBase

class AutosDb:
    def __init__(self):
        self.base = DataBase()
        
    def leer_autos(self,numero):
        return self.base.getAll("SELECT * FROM autos WHERE id_dueño = {}".format(numero))
    
    def agregar_autos(self,row):
        return self.base.query(f"insert into autos (patente,id_dueño,marca,modelo,año,kilometros,tipo_combustible,notas) values ('{row[0]}',{row[1]},'{row[2]}','{row[3]}',{row[4]},{row[5]},'{row[6]}','{row[7]}')")
    
    def actualizar_auto(self,row):
        return self.base.query(f"UPDATE autos SET marca ='{row[2]}', modelo ='{row[3]}', año ='{row[4]}', kilometros ='{row[5]}', tipo_combustible='{row[6]}', notas='{row[7]}' WHERE patente = '{row[0]}'")
    
    def borrar_auto(self,patente):
        return self.base.query(f"DELETE FROM autos WHERE patente = '{patente}'")
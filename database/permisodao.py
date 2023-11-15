from database.database import DataBase

class PermisosDb:
    def __init__(self):
        self.base = DataBase()
        
    def leer(self,rol):
        return self.base.getAll(f"SELECT * FROM roles WHERE id_rol = {rol}")
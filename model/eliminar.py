from database.database import PersonaDb

class EliminarController:
    def __init__(self,main):
        self._main = main
        self._db = PersonaDb()
        self._usuario = None
    
    def eliminar_usuario(self):    
        self._usuario = self._main.table_user.item(self._main.table_user.currentRow(),1)
        self._db.borrado(self._usuario.text())
        self._main.table_user.removeRow(self._main.table_user.currentRow())
    
    def eliminar_mecanico(self):    
        self._usuario = self._main.Tableuser_2.item(self._main.Tableuser_2.currentRow(),1)
        self._db.borrado(self._usuario.text())
        self._main.Tableuser_2.removeRow(self._main.Tableuser_2.currentRow())
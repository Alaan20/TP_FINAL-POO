from database.database import PersonaDb

class Eliminar():
    def __init__(self,main):
        self._main=main
        self._bd=PersonaDb()
        self._id=None
        self._select_row=[]
        
    def eliminar_usuarios(self):
        self._id= self._main.table_user.item(self._main.table_user.currentRow(),0)
        self._bd.borrado(self._id.text())
    def elimininar_mecanico(self):
        self._id=self._main.Tableuser_2.item(self._main.Tableuser_2.currentRow(),0)
        self._bd.borrado(self._id.text())
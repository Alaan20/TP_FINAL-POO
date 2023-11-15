from model.ui import Ui

class Eliminar(Ui):
    def __init__(self,main):
        super().__init__()
        self._main=main

    def eliminar_usuarios(self):
        self._id= self._main.table_user.item(self._main.table_user.currentRow(),0)
        self._db.borrado(self._id.text())
    
    def elimininar_mecanico(self):
        self._id=self._main.Tableuser_2.item(self._main.Tableuser_2.currentRow(),0)
        self._db.borrado(self._id.text())
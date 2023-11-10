class BusquedaController():
    def __init__(self,main):
        self._main = main
        self._texto = ""
    
    def buscar_usuarios(self):
            self._texto = self._main.lineEdit.text()
            for i in range(self._main.table_user.rowCount()):
                for j in range(self._main.table_user.columnCount()):
                    cell_widget = self._main.table_user.item(i, j)
                    if cell_widget is not None and cell_widget.text() == self._texto:
                        self._main.table_user.selectRow(i)
    
    def buscar_mecanicos(self):
        self._texto = self._main.lineEdit_2.text()
        for i in range(self._main.Tableuser_2.rowCount()):
            for j in range(self._main.Tableuser_2.columnCount()):
                cell_widget = self._main.Tableuser_2.item(i, j)
                if cell_widget is not None and cell_widget.text() == self._texto:
                    self._main.Tableuser_2.selectRow(i)
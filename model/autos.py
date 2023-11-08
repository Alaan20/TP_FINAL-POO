from database.database import AutosDb,PersonaDb

class AutosController():
    def __init__(self,main):
        self._main=main
        self._bd1=PersonaDb()
        self._bd2=AutosDb()
        self._selected_rows=[]
        self._id_usuario=None
        
    def agregar_autos(self):
        lista_auto=[]
        self._id_usuario= self._main.table_user.item(self._main.table_user.currentRow(),0)
        print(self._id_usuario.text())
        lista_auto.append(self._main.lineEdit_57.text())
        lista_auto.append(self._id_usuario.text())
        lista_auto.append(self._main.lineEdit_60.text())
        lista_auto.append(self._main.lineEdit_61.text())
        lista_auto.append(self._main.lineEdit_59.text())
        lista_auto.append(self._main.lineEdit_58.text())
        lista_auto.append(self._main.lineEdit_62.text())
        lista_auto.append(self._main.textEdit_3.toPlainText())
        print(lista_auto)
        self._bd2.agregar_autos(lista_auto)
        self._main.error_6.setStyleSheet("color:blue")
        self._main.error_6.setText("auto cragado correctamente")

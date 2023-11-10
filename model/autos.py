from database.database import AutosDb,PersonaDb

class AutosController():
    def __init__(self,main):
        self._main=main
        self._bd1=PersonaDb()
        self._bd2=AutosDb()
        self._selected_rows=[]
        self._id_usuario=None
        
    def validar_datos(self,variable,lista=list):
        if not variable:
            raise Exception("campos obligatorios vacios")
        lista.append(variable)
        
        
    def agregar_autos(self):

        lista_auto=[]
        self._id_usuario= self._main.table_user.item(self._main.table_user.currentRow(),0)
        print(self._id_usuario.text())
        lista_auto.append(self._main.lineEdit_57.text())
        lista_auto.append(self._id_usuario.text())
        lista_auto.append(self._main.comboBox.currentText())
        lista_auto.append(self._main.lineEdit_61.text())
        lista_auto.append(self._main.lineEdit_59.text())
        lista_auto.append(self._main.lineEdit_58.text())
        lista_auto.append(self._main.comboBox_2.currentText())

        lista_auto.append(self._main.textEdit_3.toPlainText())
        self._bd2.agregar_autos(lista_auto)
        self._main.error_6.setStyleSheet("color:blue")
        self._main.error_6.setText("auto cargado correctamente")
    
    def editar_autos(self):
        self._id_usuario= self._main.table_auto.item(self._main.table_auto.currentRow(),1)
        print(self._id_usuario.text())

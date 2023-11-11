from database.database import AutosDb,PersonaDb

class AutosController():
    def __init__(self,main):
        self._main=main
        self._bd1=PersonaDb()
        self._bd2=AutosDb()
        self._selected_rows=[]
        self._lista_auto = []
        self._id_usuario= None
        
    def validar_datos(self):
        for variable in self._lista_auto:
            if not variable:
                raise Exception("campos obligatorios vacios")
        
        
    def agregar_autos(self):
        self.guardar_lista()
        self.validar_datos()
        self.guardar_cambios()
    
    def editar_autos(self):

        self._main.stackedWidget.setCurrentIndex(7)
        self._selected_rows = self._main.table_auto.selectedItems()
        self._main.lineEdit_57.setText(f"{self._selected_rows[0].text()}")
        self._main.comboBox.setCurrentText(self._selected_rows[1].text())
        self._main.lineEdit_61.setText(f"{self._selected_rows[2].text()}")
        self._main.lineEdit_59.setText(f"{self._selected_rows[3].text()}")
        self._main.lineEdit_58.setText(f"{self._selected_rows[4].text()}")
        self._main.comboBox_2.setCurrentText(self._selected_rows[5].text())
        self._main.textEdit_3.setPlainText(self._selected_rows[6].text())
        

    def guardar_lista(self):

            self._lista_auto=[]
            self._id_usuario= self._main.table_user.item(self._main.table_user.currentRow(),0)
            self._lista_auto.append(self._main.lineEdit_57.text()) #patente
            self._lista_auto.append(self._id_usuario.text()) # id_auto
            self._lista_auto.append(self._main.comboBox.currentText()) # Marca
            self._lista_auto.append(self._main.lineEdit_61.text()) # Modelo
            self._lista_auto.append(self._main.lineEdit_59.text()) # Año
            self._lista_auto.append(self._main.lineEdit_58.text()) # Kilometros
            self._lista_auto.append(self._main.comboBox_2.currentText()) # Tipo de combustibl
            self._lista_auto.append(self._main.textEdit_3.toPlainText())
    
    def guardar_cambios(self):        
            self._bd2.agregar_autos(self._lista_auto)
            self._main.error_6.setStyleSheet("color:blue")
            self._main.error_6.setText("auto cargado correctamente")
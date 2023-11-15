from model.ui import Ui

class AutosController(Ui):
    def __init__(self,main):
        super().__init__()
        self._main=main
        self._lista_auto = []
        self._editar = bool    
        
    def agregar_autos(self):
        self._main.label_77.setText("Agregar auto:")
        self.guardar_lista()
        
        self.guardar_cambios()
    
    def borrar_autos(self):
        self._id= self._main.table_auto.item(self._main.table_auto.currentRow(),0)
        self._db2.borrar_auto(self._id.text())
        self._main.table_auto.setRowHidden(self._main.table_auto.currentRow(), True)
    
    def editar_autos(self):
        self.limpiar_texto()
        self._main.label_77.setText("Editar auto:")
        self._editar = True
        self._main.stackedWidget.setCurrentIndex(7)
        self._selected_rows = self._main.table_auto.selectedItems()
        self._main.lineEdit_57.setReadOnly(True)
        self._main.lineEdit_57.setText(f"{self._selected_rows[0].text()}")
        self._main.comboBox.setCurrentText(self._selected_rows[1].text())
        self._main.lineEdit_61.setText(f"{self._selected_rows[2].text()}")
        self._main.lineEdit_59.setText(f"{self._selected_rows[3].text()}")
        self._main.lineEdit_58.setText(f"{self._selected_rows[4].text()}")
        self._main.comboBox_2.setCurrentText(self._selected_rows[5].text())
        self._main.textEdit_3.setPlainText(self._selected_rows[6].text())
        

    def guardar_lista(self):

            self._lista_auto=[]
            self._id = self._main.table_user.item(self._main.table_user.currentRow(),0)
            self._lista_auto.append(self._main.lineEdit_57.text())#patente
            self._lista_auto.append(self._id.text()) # id_auto
            self._lista_auto.append(self._main.comboBox.currentText()) # Marca
            self._lista_auto.append(self._main.lineEdit_61.text()) # Modelo
            self._lista_auto.append(self._main.lineEdit_59.text()) # Año
            self._lista_auto.append(self._main.lineEdit_58.text()) # Kilometros
            self._lista_auto.append(self._main.comboBox_2.currentText()) # Tipo de combustibl
            self._lista_auto.append(self._main.textEdit_3.toPlainText())
    
    def guardar_cambios(self):
        if self._editar == True:
            self._db2.actualizar_auto(self._lista_auto)
            self._main.error_6.setStyleSheet("color:blue")
            self._main.error_6.setText("auto editado correctamente")
            self._editar = False
        else:    
            self._db2.agregar_autos(self._lista_auto)
            self._main.error_6.setStyleSheet("color:blue")
            self._main.error_6.setText("auto cargado correctamente")
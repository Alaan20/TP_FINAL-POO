class EditarController(): # Logica de negocio
    def __init__(self,main):
        self._main = main
        self._selected_rows = []
        # Obtener la fila seleccionada del QTableWidget
    
    def editar_usuarios(self,id_usuario):
        self._selected_rows = self._main.table_user.selectedItems()
        if self._selected_rows:
            # Cambiar a la nueva página
            self._main.stackedWidget.setCurrentIndex(3)
            
            self._main.lineEdit_18.setText(self._selected_rows[0].text()) #
            self._main.lineEdit_17.setText(self._selected_rows[1].text())#
            self._main.lineEdit_19.setText(self._selected_rows[2].text())#
            self._main.lineEdit_6.setText(self._selected_rows[3].text())#
            self._main.lineEdit_30.setText(self._selected_rows[4].text())
            self._main.lineEdit_23.setText(self._selected_rows[5].text())
            self._main.lineEdit_14.setText("********")
    
    # def actualizar(self):
    #     # Obtener los datos de los QLineEdit
    #     datos = [
    #         self._main.lineEdit_25.text(),
    #         self._main.lineEdit_18.text(),
    #         self._main.lineEdit_14.text(),
    #         self._main.lineEdit_19.text(),
    #         self._main.lineEdit_26.text(),
    #         self._main.lineEdit_17.text(),
    #     ]
    #     # Actualizar la fila seleccionada en el QTableWidget
    #     for i, dato in enumerate(datos):
    #         if self._selected_rows and i < len(self._selected_rows):
    #             self._selected_rows[i].setText(dato)
    
    def editar_mecanicos(self):
        self._selected_rows = self._main.Tableuser_2.selectedItems()
        if self._selected_rows:
            # Cambiar a la nueva página
            self._main.stackedWidget.setCurrentIndex(2)
            self._main.lineEdit_38.setText(self._selected_rows[0].text())
            self._main.lineEdit_31.setText(self._selected_rows[1].text())
            self._main.lineEdit_27.setText(self._selected_rows[2].text())
            self._main.lineEdit_32.setText(self._selected_rows[3].text())
            self._main.lineEdit_39.setText(self._selected_rows[4].text())
            self._main.lineEdit_30.setText(self._selected_rows[5].text())
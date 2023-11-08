from database.database import PersonaDb

class EditarController():
    
    def __init__(self,main):
        self._main = main
        self._db = PersonaDb()
        self._id = None
        self._selected_rows = []
    
    def editar_usuarios(self):
        self._selected_rows = self._main.table_user.selectedItems()
        self._id = self._main.table_user.item(self._main.table_user.currentRow(),0)
        if self._selected_rows:
            # Cambiar a la nueva página
            self._main.stackedWidget.setCurrentIndex(6)
            self.llenar_texto()
            self._main.label_61.setText("Editar Usuario")
    
    def editar_mecanicos(self):
        self._selected_rows = self._main.Tableuser_2.selectedItems()
        self._id = self._main.table_user.item(self._main.table_user.currentRow(),0)
        if self._selected_rows:
            # Cambiar a la nueva página
            self._main.stackedWidget.setCurrentIndex(6)
            self.llenar_texto()
            self._main.label_61.setText("Editar Mecanico")
    
    def llenar_texto(self):
            self._main.lineEdit_50.setText(self._selected_rows[0].text())
            self._main.lineEdit_51.setText("********")
            self._main.lineEdit_52.setText(self._selected_rows[1].text())
            self._main.lineEdit_53.setText(self._selected_rows[2].text())
            self._main.lineEdit_54.setText(self._selected_rows[3].text())
            self._main.lineEdit_55.setText(self._selected_rows[4].text())
            self._main.lineEdit_56.setText(self._selected_rows[5].text())
                
    def guardar_cambios(self):
        try:
                self._selected_rows = [self._id.text(),self._main.lineEdit_50.text(),self._main.lineEdit_51.text(),self._main.lineEdit_52.text(),self._main.lineEdit_53.text(),self._main.lineEdit_54.text(),self._main.lineEdit_55.text(),self._main.lineEdit_56.text()]
                if self._main.lineEdit_50.text() == "" or self._main.lineEdit_51.text() == "" or self._main.lineEdit_52.text() == "" or self._main.lineEdit_53.text() == "" or self._main.lineEdit_54.text() == "" or self._main.lineEdit_55.text() == "" or self._main.lineEdit_56.text() == "":
                    raise Exception("Por favor, complete todos los campos")
                if self._main.lineEdit_51.text() == ""or self._main.lineEdit_51.text() == "********":
                    raise Exception("No puede cambiar la contraseña")
                if self._db.actualizar(self._selected_rows) is False:
                    raise Exception("Error, revise su conexión a internet")
        
                self._main.error_5.setStyleSheet("color: green")
                self._main.error_5.setText("Usuario editado con éxito")
        
        except Exception as e:
            self._main.error_5.setStyleSheet("color: red")
            self._main.error_5.setText(str(e))
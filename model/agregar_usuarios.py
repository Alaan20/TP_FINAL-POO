from database.database import PersonaDb

class Agregar():
    def __init__(self,main) -> None:
        self._main=main
        self._lista=[]
        self._bd=PersonaDb()
        
    def validar_datos(self,variable,lista:list):
        if not variable:
            raise Exception("campos obligatorios vacios")
        lista.append(variable)
        
    def agregar_usuario(self):
        llave=True
        rol=None
        try:
            llave=True
            self._lista=[]
            self.validar_datos(self._main.lineEdit_80.text(),self._lista) #nombre ususario#
            self.validar_datos(self._main.lineEdit_81.text(),self._lista) #contraseña#
            self.validar_datos(self._main.lineEdit_82.text(),self._lista) #nombre#
            self.validar_datos(self._main.lineEdit_83.text(),self._lista) #apellido#
            self.validar_datos(self._main.lineEdit_84.text(),self._lista) #dni#
        except Exception as e:
            self._main.error_2.setStyleSheet("color:red")
            self._main.error_2.setText(str(e))
            llave=False

        if self._main.radioButton_4.isChecked():
            rol=2
        elif self._main.radioButton_3.isChecked():
            rol=1
        
        if llave==True:
            self._lista.append(self._main.lineEdit_85.text())
            self._lista.append(self._main.lineEdit_86.text())
            for i in range(len(self._lista)):
                if not self._lista[i]:
                    self._lista[i]+='null'
            self._bd.crear(self._lista,rol)
                
            self._main.error_2.setStyleSheet("color:blue")
            self._main.error_2.setText("usuario agregado exitosamente!")
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

        try:
            self._lista=[]
            self.validar_datos(self._main.lineEdit_18.text(),self._lista) #nombre ususario#
            self.validar_datos(self._main.lineEdit_14.text(),self._lista) #contraseña#
            self.validar_datos(self._main.lineEdit_17.text(),self._lista) #nombre#
            self.validar_datos(self._main.lineEdit_19.text(),self._lista) #apellido#
            self.validar_datos(self._main.lineEdit_6.text(),self._lista) #dni#
        except Exception as e:
            self._main.error_2.setStyleSheet("color:red")
            self._main.error_2.setText(str(e))
            llave=False
        
        if llave==True:
            self._lista.append(self._main.lineEdit_20.text())
            self._lista.append(self._main.lineEdit_23.text())
            for i in range(len(self._lista)):
                if not self._lista[i]:
                    self._lista[i]+='null'
            self._bd.crear(self._lista,2)
                
            self._main.error_2.setStyleSheet("color:blue")
            self._main.error_2.setText("usuario agregado exitosamente!")
    
    def agregar_mecanico(self):
        llave=True

        try:
            self._lista=[]
            self.validar_datos(self._main.lineEdit_31.text(),self._lista) #nombre ususario#
            self.validar_datos(self._main.lineEdit_27.text(),self._lista) #contraseña#
            self.validar_datos(self._main.lineEdit_30.text(),self._lista) #nombre#
            self.validar_datos(self._main.lineEdit_32.text(),self._lista) #apellido#
            self.validar_datos(self._main.lineEdit_3.text(),self._lista) #dni#
        except Exception as e:
            self._main.error_3.setStyleSheet("color:red")
            self._main.error_3.setText(str(e))
            llave=False
            
        if llave==True:
            self._lista.append(self._main.lineEdit_4.text())
            self._lista.append(self._main.lineEdit_5.text())
            
            for i in range(len(self._lista)):
                if not self._lista[i]:
                    self._lista[i]+='null'
                else:
                    self._lista[i]=f'{self._lista[i]}'
            
            self._bd.crear(self._lista,1)
            self._main.error_3.setStyleSheet("color:blue")
            self._main.error_3.setText("mecanico agregado exitosamente!")
        
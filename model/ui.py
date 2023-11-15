from  PyQt5 import QtWidgets, uic
from database.database import PersonaDb, AutosDb

class Ui:
    def __init__(self):
        self._db = PersonaDb()
        self._db2=AutosDb()
        self._id = None
        self._selected_rows = []
        self._lista_auto = []
        
    def completar_tabla(self,tabla,row,colum):
            tabla_obj = getattr(self._main, tabla)
            tabla_obj.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
            tabla_obj.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
            tabla_obj.setRowCount(len(row) +1)
            tabla_obj.setColumnCount(len(row[0]))
            for i in range(len(row)):
                for j in range(len(row[0])):
                    tabla_obj.setItem(i+1,j,QtWidgets.QTableWidgetItem(f'{row[i][j]}'))
            tabla_obj.setColumnHidden(colum, True)
            
    def limpiar_texto(self):
        self._main.lineEdit_57.setReadOnly(False)
        self._main.lineEdit_57.setText("")
        self._main.lineEdit_61.setText("")
        self._main.lineEdit_59.setText("")
        self._main.lineEdit_58.setText("")
        self._main.textEdit_3.setPlainText("")
        self._main.lineEdit_80.setText("")
        self._main.lineEdit_81.setText("")
        self._main.lineEdit_82.setText("")
        self._main.lineEdit_83.setText("")
        self._main.lineEdit_84.setText("")
        self._main.lineEdit_85.setText("")
        self._main.lineEdit_86.setText("")
        self._main.user1.setText("")
        self._main.password1.setText("")
        self._main.error_2.setText("")
        
    def llenar_texto(self):
        self._main.lineEdit_50.setText(self._selected_rows[0].text())
        self._main.lineEdit_51.setText("********")
        self._main.lineEdit_52.setText(self._selected_rows[1].text())
        self._main.lineEdit_53.setText(self._selected_rows[2].text())
        self._main.lineEdit_54.setText(self._selected_rows[3].text())
        self._main.lineEdit_55.setText(self._selected_rows[4].text())
        self._main.lineEdit_56.setText(self._selected_rows[5].text())
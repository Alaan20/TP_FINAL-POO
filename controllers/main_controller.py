class Main():
    def __init__(self):    
        self.main = main
        self.db = PersonaDb()
        self.rows = self.db.leer_todos()
        
    def show_page_3(self): 
        for i, row in enumerate(self.rows):
            for j, column in enumerate(row):
                self.main.tableWidget.setItem(i,j,QTableWidgetItem(str(column)))
                #self.main.tableWidget.item(i,j).setFlags(QtCore.Qt.ItemIsEnabled)
        main.show()
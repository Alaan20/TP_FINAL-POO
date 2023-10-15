import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton
from database import PersonaDb

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Crear campos de entrada de texto
        self.usuario_label = QLabel("Nuevo usuario:", self)
        self.usuario_label.move(50, 50)
        self.usuario_input = QLineEdit(self)
        self.usuario_input.move(150, 50)

        self.contraseña_label = QLabel("Nueva contraseña:", self)
        self.contraseña_label.move(50, 100)
        self.contraseña_input = QLineEdit(self)
        self.contraseña_input.move(150, 100)

        # Crear botón de guardar
        self.guardar_button = QPushButton("Guardar", self)
        self.guardar_button.move(150, 150)
        self.guardar_button.clicked.connect(self.guardar)

    def guardar(self):
        # Leer los valores de los campos de entrada de texto
        nuevo_usuario = self.usuario_input.text()
        nueva_contraseña = self.contraseña_input.text()

        # Actualizar la base de datos
        db = PersonaDb()
        db.actualizar(nuevo_usuario, nueva_contraseña)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
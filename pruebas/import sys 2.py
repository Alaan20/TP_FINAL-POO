import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QScrollArea

class VentanaConScroll(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Ventana con Barra de Desplazamiento')
        self.setGeometry(100, 100, 400, 300)

        # Crear un layout con muchos elementos (para que se necesite desplazamiento)
        layout = QVBoxLayout()
        for i in range(1, 21):
            button = QPushButton(f'Botón {i}')
            layout.addWidget(button)

        # Crear un área de desplazamiento y establecer el layout dentro de ella
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        container = QWidget()
        container.setLayout(layout)
        scroll_area.setWidget(container)

        # Agregar el área de desplazamiento a la ventana principal
        main_layout = QVBoxLayout()
        main_layout.addWidget(scroll_area)
        self.setLayout(main_layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = QMainWindow()
    ventana_con_scroll = VentanaConScroll()
    ventana.setCentralWidget(ventana_con_scroll)
    ventana.show()
    sys.exit(app.exec_())

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_autosoft(object):
    def setupUi(self, autosoft):
        
        autosoft.setWindowTitle("Autosoft 2.1")
        autosoft.resize(530, 432)
        autosoft.setMouseTracking(True)
        autosoft.setTabletTracking(True)
        
        self._iniciar_sesion = QtWidgets.QPushButton(autosoft)
        self._iniciar_sesion.setText("Log In")
        self._iniciar_sesion.setEnabled(False)
        self._iniciar_sesion.setGeometry(QtCore.QRect(240, 330, 71, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self._iniciar_sesion.setFont(font)

        self._contraseña = QtWidgets.QLineEdit(autosoft)
        self._contraseña.setGeometry(QtCore.QRect(170, 290, 201, 20))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self._contraseña.setFont(font)
        self._contraseña.setTabletTracking(True)
        self._contraseña.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self._contraseña.setAutoFillBackground(False)
        self._contraseña.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self._contraseña.setEchoMode(QtWidgets.QLineEdit.Password)
        self._contraseña.setDragEnabled(True)
        self._contraseña.setClearButtonEnabled(True)
        
        self._usuario = QtWidgets.QLineEdit(autosoft)
        self._usuario.setGeometry(QtCore.QRect(170, 220, 201, 21))
        self._usuario.setMouseTracking(True)

        self._usuario_texto = QtWidgets.QLabel(autosoft)
        self._usuario_texto.setText("Usuario:")
        self._usuario_texto.setGeometry(QtCore.QRect(170, 190, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self._usuario_texto.setFont(font)

        self._contraseña_texto = QtWidgets.QLabel(autosoft)
        self._contraseña_texto.setText("contraseña:")
        self._contraseña_texto.setGeometry(QtCore.QRect(170, 260, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self._contraseña_texto.setFont(font)
        self._line = QtWidgets.QFrame(autosoft)
        self._line.setGeometry(QtCore.QRect(170, 360, 201, 20))
        self._line.setFrameShape(QtWidgets.QFrame.HLine)
        self._line.setFrameShadow(QtWidgets.QFrame.Sunken)

        self._image = QtWidgets.QLabel(autosoft)
        self._image.setGeometry(QtCore.QRect(-20, 0, 561, 171))
        self._image.setText("")
        self._image.setPixmap(QtGui.QPixmap("C:/4.png"))
        self._image.setScaledContents(True)
 
        self._usuario.editingFinished.connect(self._contraseña.setFocus)
        self._contraseña.selectionChanged.connect(self._iniciar_sesion.toggle)
        QtCore.QMetaObject.connectSlotsByName(autosoft)
        autosoft.setTabOrder(self._usuario, self._contraseña)
        autosoft.setTabOrder(self._contraseña, self._iniciar_sesion)
        self._usuario.textChanged.connect(self.on_text_changed)
        self._contraseña.textChanged.connect(self.on_text_changed)

    def on_text_changed(self): # Activa el boton de login si se inserto texto en user y contraseña
        self._iniciar_sesion.setEnabled(bool(self._usuario.text()) and bool(self._contraseña.text()))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    autosoft = QtWidgets.QDialog()
    ui = Ui_autosoft()
    ui.setupUi(autosoft)
    autosoft.show()
    sys.exit(app.exec_())

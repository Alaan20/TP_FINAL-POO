# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_autosoft(object):
    def setupUi(self, autosoft):
        if not autosoft.objectName():
            autosoft.setObjectName(u"autosoft")
        autosoft.setEnabled(True)
        autosoft.resize(530, 432)
        autosoft.setMouseTracking(True)
        autosoft.setTabletTracking(True)
        self.log_in = QPushButton(autosoft)
        self.log_in.setObjectName(u"log_in")
        self.log_in.setEnabled(True)
        self.log_in.setGeometry(QRect(240, 330, 71, 21))
        font = QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.log_in.setFont(font)
        self.password = QLineEdit(autosoft)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(170, 290, 201, 20))
        font1 = QFont()
        font1.setStyleStrategy(QFont.PreferDefault)
        self.password.setFont(font1)
        self.password.setTabletTracking(True)
        self.password.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.password.setAutoFillBackground(False)
        self.password.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setDragEnabled(True)
        self.password.setClearButtonEnabled(True)
        self.user = QLineEdit(autosoft)
        self.user.setObjectName(u"user")
        self.user.setGeometry(QRect(170, 220, 201, 21))
        self.user.setMouseTracking(True)
        self.user_2 = QLabel(autosoft)
        self.user_2.setObjectName(u"user_2")
        self.user_2.setGeometry(QRect(170, 190, 81, 16))
        font2 = QFont()
        font2.setPointSize(14)
        self.user_2.setFont(font2)
        self.password_2 = QLabel(autosoft)
        self.password_2.setObjectName(u"password_2")
        self.password_2.setGeometry(QRect(170, 260, 111, 16))
        self.password_2.setFont(font2)
        self.line = QFrame(autosoft)
        self.line.setObjectName(u"line")
        self.line.setEnabled(True)
        self.line.setGeometry(QRect(180, 380, 201, 20))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.image = QLabel(autosoft)
        self.image.setObjectName(u"image")
        self.image.setGeometry(QRect(-20, 0, 561, 171))
        self.image.setPixmap(QPixmap(u"D:/Users/Administrador/Documents/GitHub/TP_FINAL-POO/4.png"))
        self.image.setScaledContents(True)
        self.frame = QFrame(autosoft)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(60, 350, 441, 31))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.error = QLabel(self.frame)
        self.error.setObjectName(u"error")
        self.error.setEnabled(True)
        self.error.setGeometry(QRect(100, 10, 251, 16))
        self.error.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.error.setInputMethodHints(Qt.ImhNone)
        QWidget.setTabOrder(self.user, self.password)
        QWidget.setTabOrder(self.password, self.log_in)

        self.retranslateUi(autosoft)
        self.user.editingFinished.connect(self.password.setFocus)
        self.password.selectionChanged.connect(self.log_in.toggle)

        QMetaObject.connectSlotsByName(autosoft)
    # setupUi

    def retranslateUi(self, autosoft):
        autosoft.setWindowTitle(QCoreApplication.translate("autosoft", u"Autosoft 2.1", None))
        self.log_in.setText(QCoreApplication.translate("autosoft", u"Log In", None))
        self.password.setText("")
        self.user_2.setText(QCoreApplication.translate("autosoft", u"Usuario:", None))
        self.password_2.setText(QCoreApplication.translate("autosoft", u"Password:", None))
        self.image.setText("")
        self.error.setText("")
    # retranslateUi


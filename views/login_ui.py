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
    QLineEdit, QPushButton, QSizePolicy, QStackedWidget,
    QWidget)

class Ui_autosoft(object):
    def setupUi(self, autosoft):
        if not autosoft.objectName():
            autosoft.setObjectName(u"autosoft")
        autosoft.setEnabled(True)
        autosoft.resize(331, 416)
        autosoft.setMouseTracking(True)
        autosoft.setTabletTracking(True)
        self.stackedWidget = QStackedWidget(autosoft)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(-1, -11, 331, 421))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.frame = QFrame(self.page)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 20, 331, 411))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.user = QLineEdit(self.frame)
        self.user.setObjectName(u"user")
        self.user.setGeometry(QRect(70, 230, 201, 21))
        self.user.setMouseTracking(True)
        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setEnabled(True)
        self.line.setGeometry(QRect(70, 380, 201, 20))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.log_in = QPushButton(self.frame)
        self.log_in.setObjectName(u"log_in")
        self.log_in.setEnabled(True)
        self.log_in.setGeometry(QRect(140, 340, 71, 21))
        font = QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.log_in.setFont(font)
        self.password_2 = QLabel(self.frame)
        self.password_2.setObjectName(u"password_2")
        self.password_2.setGeometry(QRect(70, 270, 111, 16))
        font1 = QFont()
        font1.setPointSize(14)
        self.password_2.setFont(font1)
        self.user_2 = QLabel(self.frame)
        self.user_2.setObjectName(u"user_2")
        self.user_2.setGeometry(QRect(70, 200, 81, 16))
        self.user_2.setFont(font1)
        self.image = QLabel(self.frame)
        self.image.setObjectName(u"image")
        self.image.setEnabled(False)
        self.image.setGeometry(QRect(60, 0, 221, 181))
        self.image.setPixmap(QPixmap(u"../icons/login.png"))
        self.image.setScaledContents(True)
        self.image.setWordWrap(False)
        self.password = QLineEdit(self.frame)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(70, 300, 201, 20))
        font2 = QFont()
        font2.setStyleStrategy(QFont.PreferDefault)
        self.password.setFont(font2)
        self.password.setTabletTracking(True)
        self.password.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.password.setAutoFillBackground(False)
        self.password.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setDragEnabled(True)
        self.password.setClearButtonEnabled(True)
        self.error = QLabel(self.frame)
        self.error.setObjectName(u"error")
        self.error.setEnabled(True)
        self.error.setGeometry(QRect(70, 370, 251, 16))
        self.error.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.error.setInputMethodHints(Qt.ImhNone)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.retranslateUi(autosoft)

        QMetaObject.connectSlotsByName(autosoft)
    # setupUi

    def retranslateUi(self, autosoft):
        autosoft.setWindowTitle(QCoreApplication.translate("autosoft", u"Autosoft 2.1", None))
        self.log_in.setText(QCoreApplication.translate("autosoft", u"Log In", None))
        self.password_2.setText(QCoreApplication.translate("autosoft", u"Password:", None))
        self.user_2.setText(QCoreApplication.translate("autosoft", u"Usuario:", None))
        self.image.setText("")
        self.password.setText("")
        self.error.setText("")
    # retranslateUi


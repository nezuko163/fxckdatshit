# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test_start.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(258, 245)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMaximumSize(QSize(764, 16777215))
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btn_create_room = QPushButton(self.centralwidget)
        self.btn_create_room.setObjectName(u"btn_create_room")
        self.btn_create_room.setMinimumSize(QSize(0, 40))

        self.verticalLayout.addWidget(self.btn_create_room)

        self.btn_illustrations = QPushButton(self.centralwidget)
        self.btn_illustrations.setObjectName(u"btn_illustrations")
        self.btn_illustrations.setMinimumSize(QSize(0, 40))

        self.verticalLayout.addWidget(self.btn_illustrations)

        self.btn_account = QPushButton(self.centralwidget)
        self.btn_account.setObjectName(u"btn_account")
        self.btn_account.setMinimumSize(QSize(0, 40))

        self.verticalLayout.addWidget(self.btn_account)


        self.horizontalLayout.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 258, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.btn_create_room, self.btn_illustrations)
        QWidget.setTabOrder(self.btn_illustrations, self.btn_account)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_create_room.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043a\u043e\u043c\u043d\u0430\u0442\u0443", None))
        self.btn_illustrations.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043b\u043b\u044e\u0441\u0442\u0440\u0430\u0446\u0438\u0438", None))
        self.btn_account.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043a\u043a\u0430\u0443\u043d\u0442", None))
    # retranslateUi


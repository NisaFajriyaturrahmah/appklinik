# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)

class Ui_main(object):
    def setupUi(self, main):
        if not main.objectName():
            main.setObjectName(u"main")
        main.resize(800, 600)
        self.actionForm_Dokter = QAction(main)
        self.actionForm_Dokter.setObjectName(u"actionForm_Dokter")
        self.actionForm_Pasien = QAction(main)
        self.actionForm_Pasien.setObjectName(u"actionForm_Pasien")
        self.actionForm_Petugas = QAction(main)
        self.actionForm_Petugas.setObjectName(u"actionForm_Petugas")
        self.actionForm_Obat = QAction(main)
        self.actionForm_Obat.setObjectName(u"actionForm_Obat")
        self.actionFrom_Pendaftaran = QAction(main)
        self.actionFrom_Pendaftaran.setObjectName(u"actionFrom_Pendaftaran")
        self.centralwidget = QWidget(main)
        self.centralwidget.setObjectName(u"centralwidget")
        main.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(main)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 18))
        self.menuHalaman_Menu = QMenu(self.menubar)
        self.menuHalaman_Menu.setObjectName(u"menuHalaman_Menu")
        main.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(main)
        self.statusbar.setObjectName(u"statusbar")
        main.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuHalaman_Menu.menuAction())
        self.menuHalaman_Menu.addAction(self.actionForm_Dokter)
        self.menuHalaman_Menu.addAction(self.actionForm_Pasien)
        self.menuHalaman_Menu.addAction(self.actionForm_Petugas)
        self.menuHalaman_Menu.addAction(self.actionForm_Obat)
        self.menuHalaman_Menu.addAction(self.actionFrom_Pendaftaran)

        self.retranslateUi(main)

        QMetaObject.connectSlotsByName(main)
    # setupUi

    def retranslateUi(self, main):
        main.setWindowTitle(QCoreApplication.translate("main", u"main", None))
        self.actionForm_Dokter.setText(QCoreApplication.translate("main", u"Form Dokter", None))
        self.actionForm_Pasien.setText(QCoreApplication.translate("main", u"Form Pasien", None))
        self.actionForm_Petugas.setText(QCoreApplication.translate("main", u"Form Petugas", None))
        self.actionForm_Obat.setText(QCoreApplication.translate("main", u"Form Obat", None))
        self.actionFrom_Pendaftaran.setText(QCoreApplication.translate("main", u"From Pendaftaran", None))
        self.menuHalaman_Menu.setTitle(QCoreApplication.translate("main", u"Halaman Menu", None))
    # retranslateUi


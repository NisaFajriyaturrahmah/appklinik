# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_pendaftaran.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QFormLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QTimeEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayoutWidget = QWidget(self.centralwidget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(90, 10, 160, 159))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.no_daftarLabel = QLabel(self.formLayoutWidget)
        self.no_daftarLabel.setObjectName(u"no_daftarLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.no_daftarLabel)

        self.no_daftarLineEdit = QLineEdit(self.formLayoutWidget)
        self.no_daftarLineEdit.setObjectName(u"no_daftarLineEdit")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.no_daftarLineEdit)

        self.nomor_rmLabel = QLabel(self.formLayoutWidget)
        self.nomor_rmLabel.setObjectName(u"nomor_rmLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.nomor_rmLabel)

        self.nomor_rmLineEdit = QLineEdit(self.formLayoutWidget)
        self.nomor_rmLineEdit.setObjectName(u"nomor_rmLineEdit")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.nomor_rmLineEdit)

        self.tanggal_daftarLabel = QLabel(self.formLayoutWidget)
        self.tanggal_daftarLabel.setObjectName(u"tanggal_daftarLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.tanggal_daftarLabel)

        self.tanggal_daftarDateEdit = QDateEdit(self.formLayoutWidget)
        self.tanggal_daftarDateEdit.setObjectName(u"tanggal_daftarDateEdit")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.tanggal_daftarDateEdit)

        self.tanggal_janjiLabel = QLabel(self.formLayoutWidget)
        self.tanggal_janjiLabel.setObjectName(u"tanggal_janjiLabel")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.tanggal_janjiLabel)

        self.tanggal_janjiDateEdit = QDateEdit(self.formLayoutWidget)
        self.tanggal_janjiDateEdit.setObjectName(u"tanggal_janjiDateEdit")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.tanggal_janjiDateEdit)

        self.jam_janjiLabel = QLabel(self.formLayoutWidget)
        self.jam_janjiLabel.setObjectName(u"jam_janjiLabel")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.jam_janjiLabel)

        self.jam_janjiTimeEdit = QTimeEdit(self.formLayoutWidget)
        self.jam_janjiTimeEdit.setObjectName(u"jam_janjiTimeEdit")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.jam_janjiTimeEdit)

        self.keluhanLabel = QLabel(self.formLayoutWidget)
        self.keluhanLabel.setObjectName(u"keluhanLabel")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.keluhanLabel)

        self.keluhanLineEdit = QLineEdit(self.formLayoutWidget)
        self.keluhanLineEdit.setObjectName(u"keluhanLineEdit")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.keluhanLineEdit)

        self.kd_petugasLabel = QLabel(self.formLayoutWidget)
        self.kd_petugasLabel.setObjectName(u"kd_petugasLabel")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.kd_petugasLabel)

        self.kd_petugasLineEdit = QLineEdit(self.formLayoutWidget)
        self.kd_petugasLineEdit.setObjectName(u"kd_petugasLineEdit")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.kd_petugasLineEdit)

        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 7):
            self.tableWidget.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(50, 220, 256, 91))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(50, 200, 56, 18))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(120, 200, 56, 18))
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(190, 200, 56, 18))
        self.lineCari = QLineEdit(self.centralwidget)
        self.lineCari.setObjectName(u"lineCari")
        self.lineCari.setGeometry(QRect(90, 170, 161, 20))
        self.btnCetak = QPushButton(self.centralwidget)
        self.btnCetak.setObjectName(u"btnCetak")
        self.btnCetak.setGeometry(QRect(250, 200, 56, 18))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 18))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.no_daftarLabel.setText(QCoreApplication.translate("MainWindow", u"no_daftar", None))
        self.nomor_rmLabel.setText(QCoreApplication.translate("MainWindow", u"nomor_rm", None))
        self.tanggal_daftarLabel.setText(QCoreApplication.translate("MainWindow", u"tanggal_daftar", None))
        self.tanggal_janjiLabel.setText(QCoreApplication.translate("MainWindow", u"tanggal_janji", None))
        self.jam_janjiLabel.setText(QCoreApplication.translate("MainWindow", u"jam_janji", None))
        self.keluhanLabel.setText(QCoreApplication.translate("MainWindow", u"keluhan", None))
        self.kd_petugasLabel.setText(QCoreApplication.translate("MainWindow", u"kd_petugas", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"no_daftar", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"nomor_rm", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"tanggal_daftar", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"tanggal_janji", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"jam_janji", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"keluhan", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"kd_petugas", None));
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Simpan", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Ubah", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Hapus", None))
        self.btnCetak.setText(QCoreApplication.translate("MainWindow", u"Cetak", None))
    # retranslateUi


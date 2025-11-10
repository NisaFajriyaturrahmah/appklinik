# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_dokter.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayoutWidget = QWidget(self.centralwidget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(90, 10, 160, 161))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.kd_dokterLabel = QLabel(self.formLayoutWidget)
        self.kd_dokterLabel.setObjectName(u"kd_dokterLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.kd_dokterLabel)

        self.kd_dokterLineEdit = QLineEdit(self.formLayoutWidget)
        self.kd_dokterLineEdit.setObjectName(u"kd_dokterLineEdit")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.kd_dokterLineEdit)

        self.nama_dokterLabel = QLabel(self.formLayoutWidget)
        self.nama_dokterLabel.setObjectName(u"nama_dokterLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.nama_dokterLabel)

        self.nama_dokterLineEdit = QLineEdit(self.formLayoutWidget)
        self.nama_dokterLineEdit.setObjectName(u"nama_dokterLineEdit")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.nama_dokterLineEdit)

        self.jenis_kelaminLabel = QLabel(self.formLayoutWidget)
        self.jenis_kelaminLabel.setObjectName(u"jenis_kelaminLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.jenis_kelaminLabel)

        self.jenis_kelaminComboBox = QComboBox(self.formLayoutWidget)
        self.jenis_kelaminComboBox.setObjectName(u"jenis_kelaminComboBox")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.jenis_kelaminComboBox)

        self.tempat_lahirLabel = QLabel(self.formLayoutWidget)
        self.tempat_lahirLabel.setObjectName(u"tempat_lahirLabel")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.tempat_lahirLabel)

        self.tempat_lahirLineEdit = QLineEdit(self.formLayoutWidget)
        self.tempat_lahirLineEdit.setObjectName(u"tempat_lahirLineEdit")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.tempat_lahirLineEdit)

        self.alamatLabel = QLabel(self.formLayoutWidget)
        self.alamatLabel.setObjectName(u"alamatLabel")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.alamatLabel)

        self.alamatLineEdit = QLineEdit(self.formLayoutWidget)
        self.alamatLineEdit.setObjectName(u"alamatLineEdit")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.alamatLineEdit)

        self.no_teleponLabel = QLabel(self.formLayoutWidget)
        self.no_teleponLabel.setObjectName(u"no_teleponLabel")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.no_teleponLabel)

        self.no_teleponLineEdit = QLineEdit(self.formLayoutWidget)
        self.no_teleponLineEdit.setObjectName(u"no_teleponLineEdit")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.no_teleponLineEdit)

        self.spesialisasiLabel = QLabel(self.formLayoutWidget)
        self.spesialisasiLabel.setObjectName(u"spesialisasiLabel")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.spesialisasiLabel)

        self.spesialisasiLineEdit = QLineEdit(self.formLayoutWidget)
        self.spesialisasiLineEdit.setObjectName(u"spesialisasiLineEdit")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.spesialisasiLineEdit)

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
        self.tableWidget.setGeometry(QRect(40, 200, 256, 192))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(60, 180, 56, 18))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(150, 180, 56, 18))
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(230, 180, 56, 18))
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
        self.kd_dokterLabel.setText(QCoreApplication.translate("MainWindow", u"kd_dokter", None))
        self.nama_dokterLabel.setText(QCoreApplication.translate("MainWindow", u"nama_dokter", None))
        self.jenis_kelaminLabel.setText(QCoreApplication.translate("MainWindow", u"jenis_kelamin", None))
        self.tempat_lahirLabel.setText(QCoreApplication.translate("MainWindow", u"tempat_lahir", None))
        self.alamatLabel.setText(QCoreApplication.translate("MainWindow", u"alamat", None))
        self.no_teleponLabel.setText(QCoreApplication.translate("MainWindow", u"no_telepon", None))
        self.spesialisasiLabel.setText(QCoreApplication.translate("MainWindow", u"spesialisasi", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"kd_dokter", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"nama_dokter", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"jenis_kelamin", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"tempat_lahir", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"alamat", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"no_telepon", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"spesialisasi", None));
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Simpan", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Ubah", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Hapus", None))
    # retranslateUi


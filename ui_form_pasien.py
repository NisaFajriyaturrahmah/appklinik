# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_pasien.ui'
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
        self.formLayoutWidget.setGeometry(QRect(90, 10, 160, 182))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.nomor_rmLabel = QLabel(self.formLayoutWidget)
        self.nomor_rmLabel.setObjectName(u"nomor_rmLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.nomor_rmLabel)

        self.nomor_rmLineEdit = QLineEdit(self.formLayoutWidget)
        self.nomor_rmLineEdit.setObjectName(u"nomor_rmLineEdit")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.nomor_rmLineEdit)

        self.nama_pasienLabel = QLabel(self.formLayoutWidget)
        self.nama_pasienLabel.setObjectName(u"nama_pasienLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.nama_pasienLabel)

        self.nama_pasienLineEdit = QLineEdit(self.formLayoutWidget)
        self.nama_pasienLineEdit.setObjectName(u"nama_pasienLineEdit")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.nama_pasienLineEdit)

        self.no_identitasLabel = QLabel(self.formLayoutWidget)
        self.no_identitasLabel.setObjectName(u"no_identitasLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.no_identitasLabel)

        self.no_identitasLineEdit = QLineEdit(self.formLayoutWidget)
        self.no_identitasLineEdit.setObjectName(u"no_identitasLineEdit")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.no_identitasLineEdit)

        self.jenis_kelaminLabel = QLabel(self.formLayoutWidget)
        self.jenis_kelaminLabel.setObjectName(u"jenis_kelaminLabel")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.jenis_kelaminLabel)

        self.jenis_kelaminComboBox = QComboBox(self.formLayoutWidget)
        self.jenis_kelaminComboBox.setObjectName(u"jenis_kelaminComboBox")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.jenis_kelaminComboBox)

        self.golongan_darahLabel = QLabel(self.formLayoutWidget)
        self.golongan_darahLabel.setObjectName(u"golongan_darahLabel")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.golongan_darahLabel)

        self.golongan_darahComboBox = QComboBox(self.formLayoutWidget)
        self.golongan_darahComboBox.setObjectName(u"golongan_darahComboBox")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.golongan_darahComboBox)

        self.tempat_lahirLabel = QLabel(self.formLayoutWidget)
        self.tempat_lahirLabel.setObjectName(u"tempat_lahirLabel")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.tempat_lahirLabel)

        self.tempat_lahirLineEdit = QLineEdit(self.formLayoutWidget)
        self.tempat_lahirLineEdit.setObjectName(u"tempat_lahirLineEdit")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.tempat_lahirLineEdit)

        self.no_teleponLabel = QLabel(self.formLayoutWidget)
        self.no_teleponLabel.setObjectName(u"no_teleponLabel")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.no_teleponLabel)

        self.no_teleponLineEdit = QLineEdit(self.formLayoutWidget)
        self.no_teleponLineEdit.setObjectName(u"no_teleponLineEdit")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.no_teleponLineEdit)

        self.alamatLabel = QLabel(self.formLayoutWidget)
        self.alamatLabel.setObjectName(u"alamatLabel")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.LabelRole, self.alamatLabel)

        self.alamatLineEdit = QLineEdit(self.formLayoutWidget)
        self.alamatLineEdit.setObjectName(u"alamatLineEdit")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.FieldRole, self.alamatLineEdit)

        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 8):
            self.tableWidget.setColumnCount(8)
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
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(50, 260, 256, 81))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(60, 230, 56, 18))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(120, 230, 56, 18))
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(180, 230, 56, 18))
        self.lineCari = QLineEdit(self.centralwidget)
        self.lineCari.setObjectName(u"lineCari")
        self.lineCari.setGeometry(QRect(80, 200, 181, 20))
        self.btnCetak = QPushButton(self.centralwidget)
        self.btnCetak.setObjectName(u"btnCetak")
        self.btnCetak.setGeometry(QRect(240, 230, 56, 18))
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
        self.nomor_rmLabel.setText(QCoreApplication.translate("MainWindow", u"nomor_rm", None))
        self.nama_pasienLabel.setText(QCoreApplication.translate("MainWindow", u"nama_pasien", None))
        self.no_identitasLabel.setText(QCoreApplication.translate("MainWindow", u"no_identitas", None))
        self.jenis_kelaminLabel.setText(QCoreApplication.translate("MainWindow", u"jenis_kelamin", None))
        self.golongan_darahLabel.setText(QCoreApplication.translate("MainWindow", u"golongan_darah", None))
        self.tempat_lahirLabel.setText(QCoreApplication.translate("MainWindow", u"tempat_lahir", None))
        self.no_teleponLabel.setText(QCoreApplication.translate("MainWindow", u"no_telepon", None))
        self.alamatLabel.setText(QCoreApplication.translate("MainWindow", u"alamat", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"nomor_rm", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"nama_pasien", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"no_identitas", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"jenis_kelamin", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"golongan_darah", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"tempat_lahir", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"no_telepon", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"alamat", None));
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Simpan", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Ubah", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Hapus", None))
        self.btnCetak.setText(QCoreApplication.translate("MainWindow", u"Cetak", None))
    # retranslateUi


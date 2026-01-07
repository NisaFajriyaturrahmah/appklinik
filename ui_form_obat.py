# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_obat.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayoutWidget = QWidget(self.centralwidget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(90, 10, 160, 113))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.kd_obatLabel = QLabel(self.formLayoutWidget)
        self.kd_obatLabel.setObjectName(u"kd_obatLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.kd_obatLabel)

        self.kd_obatLineEdit = QLineEdit(self.formLayoutWidget)
        self.kd_obatLineEdit.setObjectName(u"kd_obatLineEdit")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.kd_obatLineEdit)

        self.nama_obatLabel = QLabel(self.formLayoutWidget)
        self.nama_obatLabel.setObjectName(u"nama_obatLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.nama_obatLabel)

        self.nama_obatLineEdit = QLineEdit(self.formLayoutWidget)
        self.nama_obatLineEdit.setObjectName(u"nama_obatLineEdit")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.nama_obatLineEdit)

        self.hargaLabel = QLabel(self.formLayoutWidget)
        self.hargaLabel.setObjectName(u"hargaLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.hargaLabel)

        self.hargaLineEdit = QLineEdit(self.formLayoutWidget)
        self.hargaLineEdit.setObjectName(u"hargaLineEdit")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.hargaLineEdit)

        self.stokLabel = QLabel(self.formLayoutWidget)
        self.stokLabel.setObjectName(u"stokLabel")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.stokLabel)

        self.stokLineEdit = QLineEdit(self.formLayoutWidget)
        self.stokLineEdit.setObjectName(u"stokLineEdit")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.stokLineEdit)

        self.keteranganLabel = QLabel(self.formLayoutWidget)
        self.keteranganLabel.setObjectName(u"keteranganLabel")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.keteranganLabel)

        self.keteranganLineEdit = QLineEdit(self.formLayoutWidget)
        self.keteranganLineEdit.setObjectName(u"keteranganLineEdit")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.keteranganLineEdit)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(50, 160, 56, 18))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(120, 160, 56, 18))
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(190, 160, 56, 18))
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
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
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(50, 180, 256, 192))
        self.btnCetak = QPushButton(self.centralwidget)
        self.btnCetak.setObjectName(u"btnCetak")
        self.btnCetak.setGeometry(QRect(250, 160, 56, 18))
        self.lineCari = QLineEdit(self.centralwidget)
        self.lineCari.setObjectName(u"lineCari")
        self.lineCari.setGeometry(QRect(90, 130, 161, 20))
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
        self.kd_obatLabel.setText(QCoreApplication.translate("MainWindow", u"kd_obat", None))
        self.nama_obatLabel.setText(QCoreApplication.translate("MainWindow", u"nama_obat", None))
        self.hargaLabel.setText(QCoreApplication.translate("MainWindow", u"harga", None))
        self.stokLabel.setText(QCoreApplication.translate("MainWindow", u"stok", None))
        self.keteranganLabel.setText(QCoreApplication.translate("MainWindow", u"keterangan", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Simpan", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Ubah", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Hapus", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"kd_obat", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"nama_obat", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"harga", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"stok", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"keterangan", None));
        self.btnCetak.setText(QCoreApplication.translate("MainWindow", u"Cetak", None))
    # retranslateUi


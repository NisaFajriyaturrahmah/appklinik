# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_petugas.ui'
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
        self.formLayoutWidget.setGeometry(QRect(90, 10, 160, 141))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.kd_petugasLabel = QLabel(self.formLayoutWidget)
        self.kd_petugasLabel.setObjectName(u"kd_petugasLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.kd_petugasLabel)

        self.kd_petugasLineEdit = QLineEdit(self.formLayoutWidget)
        self.kd_petugasLineEdit.setObjectName(u"kd_petugasLineEdit")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.kd_petugasLineEdit)

        self.nama_petugasLabel = QLabel(self.formLayoutWidget)
        self.nama_petugasLabel.setObjectName(u"nama_petugasLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.nama_petugasLabel)

        self.nama_petugasLineEdit = QLineEdit(self.formLayoutWidget)
        self.nama_petugasLineEdit.setObjectName(u"nama_petugasLineEdit")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.nama_petugasLineEdit)

        self.no_teleponLabel = QLabel(self.formLayoutWidget)
        self.no_teleponLabel.setObjectName(u"no_teleponLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.no_teleponLabel)

        self.no_teleponLineEdit = QLineEdit(self.formLayoutWidget)
        self.no_teleponLineEdit.setObjectName(u"no_teleponLineEdit")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.no_teleponLineEdit)

        self.usernameLabel = QLabel(self.formLayoutWidget)
        self.usernameLabel.setObjectName(u"usernameLabel")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.usernameLabel)

        self.usernameLineEdit = QLineEdit(self.formLayoutWidget)
        self.usernameLineEdit.setObjectName(u"usernameLineEdit")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.usernameLineEdit)

        self.passwordLabel = QLabel(self.formLayoutWidget)
        self.passwordLabel.setObjectName(u"passwordLabel")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.passwordLabel)

        self.passwordLineEdit = QLineEdit(self.formLayoutWidget)
        self.passwordLineEdit.setObjectName(u"passwordLineEdit")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.passwordLineEdit)

        self.levelLabel = QLabel(self.formLayoutWidget)
        self.levelLabel.setObjectName(u"levelLabel")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.levelLabel)

        self.levelComboBox = QComboBox(self.formLayoutWidget)
        self.levelComboBox.addItem("")
        self.levelComboBox.addItem("")
        self.levelComboBox.addItem("")
        self.levelComboBox.setObjectName(u"levelComboBox")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.levelComboBox)

        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
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
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(40, 210, 256, 111))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(40, 190, 56, 18))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(110, 190, 56, 18))
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(180, 190, 56, 18))
        self.lineCari = QLineEdit(self.centralwidget)
        self.lineCari.setObjectName(u"lineCari")
        self.lineCari.setGeometry(QRect(90, 160, 161, 20))
        self.btnCetak = QPushButton(self.centralwidget)
        self.btnCetak.setObjectName(u"btnCetak")
        self.btnCetak.setGeometry(QRect(240, 190, 56, 18))
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
        self.kd_petugasLabel.setText(QCoreApplication.translate("MainWindow", u"kd_petugas", None))
        self.nama_petugasLabel.setText(QCoreApplication.translate("MainWindow", u"nama_petugas", None))
        self.no_teleponLabel.setText(QCoreApplication.translate("MainWindow", u"no_telepon", None))
        self.usernameLabel.setText(QCoreApplication.translate("MainWindow", u"username", None))
        self.passwordLabel.setText(QCoreApplication.translate("MainWindow", u"password", None))
        self.levelLabel.setText(QCoreApplication.translate("MainWindow", u"level", None))
        self.levelComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"admin", None))
        self.levelComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"operator", None))
        self.levelComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"dokter", None))

        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"kd_petugas", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"nama_petugas", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"no_telepon", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"username", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"password", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"level", None));
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Simpan", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Ubah", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Hapus", None))
        self.btnCetak.setText(QCoreApplication.translate("MainWindow", u"Cetak", None))
    # retranslateUi


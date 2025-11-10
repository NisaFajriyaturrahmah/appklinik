# -*- coding: utf-8 -*-
import sys
from PySide6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader

from db import DB


class FormDokter(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        ui_file = QFile("form_dokter.ui")
        if not ui_file.open(QFile.ReadOnly):
            print("Gagal membuka form_dokter.ui")
            sys.exit(-1)

        loader = QUiLoader()
        self.ui = loader.load(ui_file)
        ui_file.close()

        if not self.ui:
            print("Gagal memuat UI dokter")
            sys.exit(-1)

        self.setCentralWidget(self.ui.centralwidget)
        self.resize(self.ui.size())
        self.db = DB()
        self.ui.jenis_kelaminComboBox.addItems(["Laki-laki", "Perempuan"])

        self.ui.pushButton.clicked.connect(self.simpan_dokter)
        self.ui.pushButton_2.clicked.connect(self.ubah_dokter)
        self.ui.pushButton_3.clicked.connect(self.hapus_dokter)

        self.load_data()

        self.ui.tableWidget.cellClicked.connect(self.tabel_diklik)

    def load_data(self):
        data = self.db.ambilSemuaDokter()
        self.ui.tableWidget.setRowCount(len(data))
        for row_idx, row_data in enumerate(data):
            for col_idx, value in enumerate(row_data):
                self.ui.tableWidget.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))

    def simpan_dokter(self):
        kd = self.ui.kd_dokterLineEdit.text()
        nama = self.ui.nama_dokterLineEdit.text()
        jk = self.ui.jenis_kelaminComboBox.currentText()
        tempat = self.ui.tempat_lahirLineEdit.text()
        alamat = self.ui.alamatLineEdit.text()
        telp = self.ui.no_teleponLineEdit.text()
        spesialis = self.ui.spesialisasiLineEdit.text()

        try:
            self.db.simpanDokter(kd, nama, jk, tempat, alamat, telp, spesialis)
            QMessageBox.information(self, "Sukses", "Data dokter berhasil disimpan!")
            self.load_data()
            self.clear_form()
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def ubah_dokter(self):
        kd = self.ui.kd_dokterLineEdit.text()
        nama = self.ui.nama_dokterLineEdit.text()
        jk = self.ui.jenis_kelaminComboBox.currentText()
        tempat = self.ui.tempat_lahirLineEdit.text()
        alamat = self.ui.alamatLineEdit.text()
        telp = self.ui.no_teleponLineEdit.text()
        spesialis = self.ui.spesialisasiLineEdit.text()

        try:
            self.db.ubahDokter(kd, nama, jk, tempat, alamat, telp, spesialis)
            QMessageBox.information(self, "Sukses", "Data dokter berhasil diubah!")
            self.load_data()
            self.clear_form()
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def hapus_dokter(self):
        kd = self.ui.kd_dokterLineEdit.text()
        confirm = QMessageBox.question(
            self,
            "Konfirmasi",
            f"Yakin ingin menghapus dokter {kd}?",
            QMessageBox.Yes | QMessageBox.No
        )
        if confirm == QMessageBox.Yes:
            try:
                self.db.hapusDokter(kd)
                QMessageBox.information(self, "Sukses", "Data dokter berhasil dihapus!")
                self.load_data()
                self.clear_form()
            except Exception as e:
                QMessageBox.critical(self, "Error", str(e))

    def tabel_diklik(self, row, column):
        self.ui.kd_dokterLineEdit.setText(self.ui.tableWidget.item(row, 0).text())
        self.ui.nama_dokterLineEdit.setText(self.ui.tableWidget.item(row, 1).text())
        jk = self.ui.tableWidget.item(row, 2).text()
        index = self.ui.jenis_kelaminComboBox.findText(jk)
        if index >= 0:
            self.ui.jenis_kelaminComboBox.setCurrentIndex(index)
        self.ui.tempat_lahirLineEdit.setText(self.ui.tableWidget.item(row, 3).text())
        self.ui.alamatLineEdit.setText(self.ui.tableWidget.item(row, 4).text())
        self.ui.no_teleponLineEdit.setText(self.ui.tableWidget.item(row, 5).text())
        self.ui.spesialisasiLineEdit.setText(self.ui.tableWidget.item(row, 6).text())

    def clear_form(self):
        self.ui.kd_dokterLineEdit.clear()
        self.ui.nama_dokterLineEdit.clear()
        self.ui.jenis_kelaminComboBox.setCurrentIndex(0)
        self.ui.tempat_lahirLineEdit.clear()
        self.ui.alamatLineEdit.clear()
        self.ui.no_teleponLineEdit.clear()
        self.ui.spesialisasiLineEdit.clear()

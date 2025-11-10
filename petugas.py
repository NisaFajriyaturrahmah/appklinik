# -*- coding: utf-8 -*-
import sys
from ui_form_petugas import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem
from db import DB

class FormPetugas(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)

        self.db = DB()

        self.pushButton.clicked.connect(self.simpan_petugas)
        self.pushButton_2.clicked.connect(self.ubah_petugas)
        self.pushButton_3.clicked.connect(self.hapus_petugas)

        self.tableWidget.cellClicked.connect(self.tabel_diklik)

        self.levelComboBox.clear() # Kosongkan dulu (jika ada item bawaan)
        self.levelComboBox.addItems(["admin", "operator", "dokter"])

        self.load_data()

        self.setWindowTitle("Form Data Petugas")


    def load_data(self):
        data_petugas = self.db.ambilSemuaPetugas()

        data_tampil = [data[:4] + data[5:] for data in data_petugas]

        self.tableWidget.setRowCount(len(data_tampil))

        for row, data in enumerate(data_tampil):
            for col, item in enumerate(data):
                self.tableWidget.setItem(row, col, QTableWidgetItem(str(item)))

    def tabel_diklik(self, row, column):
        kd_petugas = self.tableWidget.item(row, 0).text()

        petugas_data = self.db.ambilPetugasById(kd_petugas)

        if petugas_data:
            self.kd_petugasLineEdit.setText(str(petugas_data[0]))
            self.nama_petugasLineEdit.setText(str(petugas_data[1]))
            self.no_teleponLineEdit.setText(str(petugas_data[2]))
            self.usernameLineEdit.setText(str(petugas_data[3]))
            self.passwordLineEdit.setText(str(petugas_data[4]))

            level = str(petugas_data[5])
            index = self.levelComboBox.findText(level)
            if index >= 0:
                self.levelComboBox.setCurrentIndex(index)


    def simpan_petugas(self):
        kd = self.kd_petugasLineEdit.text()
        nama = self.nama_petugasLineEdit.text()
        telp = self.no_teleponLineEdit.text()
        username = self.usernameLineEdit.text()
        password = self.passwordLineEdit.text()
        level = self.levelComboBox.currentText()

        if not kd or not nama or not password:
            QMessageBox.warning(self, "Peringatan", "Kode, Nama, dan Password tidak boleh kosong!")
            return

        try:
            self.db.simpanPetugas(kd, nama, telp, username, password, level)
            QMessageBox.information(self, "Sukses", "Data Petugas berhasil disimpan!")
            self.load_data()
            self.clear_form()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Gagal menyimpan data: {e}")


    def ubah_petugas(self):
        kd = self.kd_petugasLineEdit.text()
        nama = self.nama_petugasLineEdit.text()
        telp = self.no_teleponLineEdit.text()
        username = self.usernameLineEdit.text()
        password = self.passwordLineEdit.text()
        level = self.levelComboBox.currentText()

        if not kd:
            QMessageBox.warning(self, "Peringatan", "Pilih data Petugas yang akan diubah!")
            return

        try:
            self.db.ubahPetugas(kd, nama, telp, username, password, level)
            QMessageBox.information(self, "Sukses", "Data Petugas berhasil diubah!")
            self.load_data()
            self.clear_form()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Gagal mengubah data: {e}")

    def hapus_petugas(self):
        kd = self.kd_petugasLineEdit.text()
        if not kd:
            QMessageBox.warning(self, "Peringatan", "Pilih data Petugas yang akan dihapus!")
            return

        confirm = QMessageBox.question(self, 'Konfirmasi Hapus',
                                          f"Anda yakin ingin menghapus Petugas dengan Kode: {kd}?",
                                          QMessageBox.Yes | QMessageBox.No)

        if confirm == QMessageBox.Yes:
            try:
                self.db.hapusPetugas(kd)
                QMessageBox.information(self, "Sukses", "Data petugas berhasil dihapus!")
                self.load_data()
                self.clear_form()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Gagal menghapus data: {str(e)}")


    def clear_form(self):
        self.kd_petugasLineEdit.clear()
        self.nama_petugasLineEdit.clear()
        self.no_teleponLineEdit.clear()
        self.usernameLineEdit.clear()
        self.passwordLineEdit.clear()
        self.levelComboBox.setCurrentIndex(0) # Kembali ke index pertama

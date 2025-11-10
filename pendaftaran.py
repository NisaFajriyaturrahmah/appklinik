# -*- coding: utf-8 -*-
import sys
from PySide6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem
from PySide6.QtCore import QDate, QTime

from db import DB
from ui_form_pendaftaran import Ui_MainWindow

class FormPendaftaran(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)

        self.db = DB()

        self.pushButton.clicked.connect(self.simpan_pendaftaran)
        self.pushButton_2.clicked.connect(self.ubah_pendaftaran)
        self.pushButton_3.clicked.connect(self.hapus_pendaftaran)

        self.tableWidget.cellClicked.connect(self.tabel_diklik)

        self.load_data()

        self.tanggal_daftarDateEdit.setCalendarPopup(True)
        self.tanggal_janjiDateEdit.setCalendarPopup(True)

    def load_data(self):
        try:
            data = self.db.tampilPendaftaran()
            self.tableWidget.setRowCount(0)
            self.tableWidget.setColumnCount(7)

            for row_num, row_data in enumerate(data):
                self.tableWidget.insertRow(row_num)
                for col_num, col_data in enumerate(row_data):
                    if isinstance(col_data, QDate):
                        display_data = col_data.toString("yyyy-MM-dd")
                    elif isinstance(col_data, QTime):
                        display_data = col_data.toString("HH:mm:ss")
                    else:
                        display_data = str(col_data)

                    self.tableWidget.setItem(row_num, col_num, QTableWidgetItem(display_data))

            self.tableWidget.resizeColumnsToContents()

        except Exception as e:
            QMessageBox.critical(self, "Error Load Data", f"Gagal memuat data pendaftaran: {e}")

    def get_input_data(self):
        no_daftar = self.no_daftarLineEdit.text()
        nomor_rm = self.nomor_rmLineEdit.text()

        tgl_daftar = self.tanggal_daftarDateEdit.date().toString("yyyy-MM-dd")
        tgl_janji = self.tanggal_janjiDateEdit.date().toString("yyyy-MM-dd")

        jam_janji = self.jam_janjiTimeEdit.time().toString("HH:mm:ss")

        keluhan = self.keluhanLineEdit.text()
        kd_petugas = self.kd_petugasLineEdit.text()

        return (no_daftar, nomor_rm, tgl_daftar, tgl_janji, jam_janji, keluhan, kd_petugas)

    def simpan_pendaftaran(self):
        no_daftar, nomor_rm, tgl_daftar, tgl_janji, jam_janji, keluhan, kd_petugas = self.get_input_data()

        if not all([no_daftar, nomor_rm, tgl_daftar, tgl_janji, jam_janji, keluhan, kd_petugas]):
            QMessageBox.warning(self, "Peringatan", "Semua field harus diisi!")
            return

        try:
            self.db.simpanPendaftaran(no_daftar, nomor_rm, tgl_daftar, tgl_janji, jam_janji, keluhan, kd_petugas)
            QMessageBox.information(self, "Sukses", "Data Pendaftaran berhasil disimpan!")
            self.load_data()
            self.clear_form()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Gagal menyimpan data: {e}")

    def ubah_pendaftaran(self):
        no_daftar, nomor_rm, tgl_daftar, tgl_janji, jam_janji, keluhan, kd_petugas = self.get_input_data()

        if not no_daftar:
            QMessageBox.warning(self, "Peringatan", "Pilih data yang akan diubah dari tabel!")
            return

        if not all([no_daftar, nomor_rm, tgl_daftar, tgl_janji, jam_janji, keluhan, kd_petugas]):
            QMessageBox.warning(self, "Peringatan", "Semua field harus diisi!")
            return

        try:
            self.db.ubahPendaftaran(no_daftar, nomor_rm, tgl_daftar, tgl_janji, jam_janji, keluhan, kd_petugas)
            QMessageBox.information(self, "Sukses", "Data Pendaftaran berhasil diubah!")
            self.load_data()
            self.clear_form()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Gagal mengubah data: {e}")

    def hapus_pendaftaran(self):
        no_daftar = self.no_daftarLineEdit.text()

        if not no_daftar:
            QMessageBox.warning(self, "Peringatan", "Pilih data Pendaftaran yang akan dihapus!")
            return

        konfirmasi = QMessageBox.question(self, 'Konfirmasi Hapus',
                                          f"Anda yakin ingin menghapus Pendaftaran dengan No. Daftar: {no_daftar}?",
                                          QMessageBox.Yes | QMessageBox.No)

        if konfirmasi == QMessageBox.Yes:
            try:
                self.db.hapusPendaftaran(no_daftar)
                QMessageBox.information(self, "Sukses", "Data Pendaftaran berhasil dihapus!")
                self.load_data()
                self.clear_form()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Gagal menghapus data: {e}")

    def tabel_diklik(self, row, column):
        try:
            no_daftar = self.tableWidget.item(row, 0).text()
            nomor_rm = self.tableWidget.item(row, 1).text()
            tgl_daftar_str = self.tableWidget.item(row, 2).text()
            tgl_janji_str = self.tableWidget.item(row, 3).text()
            jam_janji_str = self.tableWidget.item(row, 4).text()
            keluhan = self.tableWidget.item(row, 5).text()
            kd_petugas = self.tableWidget.item(row, 6).text()

            self.no_daftarLineEdit.setText(no_daftar)
            self.nomor_rmLineEdit.setText(nomor_rm)
            self.keluhanLineEdit.setText(keluhan)
            self.kd_petugasLineEdit.setText(kd_petugas)

            tgl_daftar = QDate.fromString(tgl_daftar_str, "yyyy-MM-dd")
            self.tanggal_daftarDateEdit.setDate(tgl_daftar)

            tgl_janji = QDate.fromString(tgl_janji_str, "yyyy-MM-dd")
            self.tanggal_janjiDateEdit.setDate(tgl_janji)

            jam_janji = QTime.fromString(jam_janji_str, "HH:mm:ss")
            self.jam_janjiTimeEdit.setTime(jam_janji)

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Gagal mengisi form dari tabel: {e}")


    def clear_form(self):
        self.no_daftarLineEdit.clear()
        self.nomor_rmLineEdit.clear()
        self.keluhanLineEdit.clear()
        self.kd_petugasLineEdit.clear()

        self.tanggal_daftarDateEdit.setDate(QDate.currentDate())
        self.tanggal_janjiDateEdit.setDate(QDate.currentDate())
        self.jam_janjiTimeEdit.setTime(QTime.currentTime())

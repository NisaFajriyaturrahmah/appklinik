# -*- coding: utf-8 -*-
import sys
from PySide6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader

from db import DB # Memastikan impor dari db.py

class FormObat(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        ui_file = QFile("form_obat.ui")
        if not ui_file.open(QFile.ReadOnly):
            print("Gagal membuka form_obat.ui")
            sys.exit(-1)

        loader = QUiLoader()
        self.ui = loader.load(ui_file)
        ui_file.close()

        if not self.ui:
            print("Gagal memuat UI obat")
            sys.exit(-1)

        self.setCentralWidget(self.ui.centralwidget)
        self.resize(self.ui.size())
        self.setWindowTitle("Form Data Obat")

        self.db = DB()

        self.ui.pushButton.clicked.connect(self.simpan)
        self.ui.pushButton_2.clicked.connect(self.ubah)
        self.ui.pushButton_3.clicked.connect(self.hapus)

        self.ui.tableWidget.cellClicked.connect(self.ambil_data_dari_tabel)

        self.load_data()


    def load_data(self):
        data_obat = self.db.ambilSemuaObat()

        self.ui.tableWidget.setRowCount(len(data_obat))

        for row, data in enumerate(data_obat):
            for col, item in enumerate(data):
                # Data urutan: kd_obat, nama_obat, harga, stok, keterangan
                self.ui.tableWidget.setItem(row, col, QTableWidgetItem(str(item)))

    def ambil_data_dari_tabel(self, row, column):
        try:
            kd_obat = self.ui.tableWidget.item(row, 0).text()
            nama_obat = self.ui.tableWidget.item(row, 1).text()
            harga = self.ui.tableWidget.item(row, 2).text()
            stok = self.ui.tableWidget.item(row, 3).text()
            keterangan = self.ui.tableWidget.item(row, 4).text()

            self.ui.kd_obatLineEdit.setText(kd_obat)
            self.ui.nama_obatLineEdit.setText(nama_obat)
            self.ui.hargaLineEdit.setText(harga)
            self.ui.stokLineEdit.setText(stok)
            self.ui.keteranganLineEdit.setText(keterangan)

        except Exception as e:
            print(f"Error saat klik tabel: {e}")

    def simpan(self):
        kd = self.ui.kd_obatLineEdit.text()
        nama = self.ui.nama_obatLineEdit.text()
        harga = self.ui.hargaLineEdit.text()
        stok = self.ui.stokLineEdit.text()
        keterangan = self.ui.keteranganLineEdit.text()

        if not kd or not nama:
            QMessageBox.warning(self.ui, "Peringatan", "Kode dan Nama Obat tidak boleh kosong!")
            return

        try:
            self.db.simpanObat(kd, nama, harga, stok, keterangan)
            QMessageBox.information(self.ui, "Sukses", "Data Obat berhasil disimpan!")
            self.load_data() # Muat ulang data
            self.clear_fields()
        except Exception as e:
            QMessageBox.critical(self.ui, "Error", f"Gagal menyimpan data: {e}")

    def ubah(self):
        kd = self.ui.kd_obatLineEdit.text()
        nama = self.ui.nama_obatLineEdit.text()
        harga = self.ui.hargaLineEdit.text()
        stok = self.ui.stokLineEdit.text()
        keterangan = self.ui.keteranganLineEdit.text()

        if not kd:
            QMessageBox.warning(self.ui, "Peringatan", "Pilih data Obat yang akan diubah!")
            return

        try:
            self.db.ubahObat(kd, nama, harga, stok, keterangan)
            QMessageBox.information(self.ui, "Sukses", "Data Obat berhasil diubah!")
            self.load_data() # Muat ulang data
            self.clear_fields()
        except Exception as e:
            QMessageBox.critical(self.ui, "Error", f"Gagal mengubah data: {e}")

    def hapus(self):
        kd = self.ui.kd_obatLineEdit.text()

        if not kd:
            QMessageBox.warning(self.ui, "Peringatan", "Pilih data Obat yang akan dihapus!")
            return

        konfirmasi = QMessageBox.question(self.ui, 'Konfirmasi Hapus',
                                          f"Anda yakin ingin menghapus Obat dengan Kode: {kd}?",
                                          QMessageBox.Yes | QMessageBox.No)

        if konfirmasi == QMessageBox.Yes:
            try:
                self.db.hapusObat(kd)
                QMessageBox.information(self.ui, "Sukses", "Data Obat berhasil dihapus!")
                self.load_data() # Muat ulang data
                self.clear_fields()
            except Exception as e:
                QMessageBox.critical(self.ui, "Error", f"Gagal menghapus data: {e}")

    def clear_fields(self):
        self.ui.kd_obatLineEdit.clear()
        self.ui.nama_obatLineEdit.clear()
        self.ui.hargaLineEdit.clear()
        self.ui.stokLineEdit.clear()
        self.ui.keteranganLineEdit.clear()

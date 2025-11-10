# -*- coding: utf-8 -*-
import sys
from PySide6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem, QWidget
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader

from db import DB


class FormPasien(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        ui_file = QFile("form_pasien.ui")
        if not ui_file.open(QFile.ReadOnly):
            print("Gagal membuka form_pasien.ui. Pastikan file ini ada.")
            sys.exit(-1)

        loader = QUiLoader()
        temp_ui = loader.load(ui_file)
        ui_file.close()

        if not temp_ui:
            print("Gagal memuat UI pasien")
            sys.exit(-1)

        self.setCentralWidget(temp_ui.centralwidget)
        self.resize(temp_ui.size())

        for widget in temp_ui.centralwidget.findChildren(QWidget):
            if widget.objectName():
                setattr(self, widget.objectName(), widget)

        self.db = DB()

        self.jenis_kelaminComboBox.addItems(["Laki-laki", "Perempuan"])
        self.golongan_darahComboBox.addItems(["A", "B", "O", "AB"])

        self.pushButton.clicked.connect(self.simpan_pasien)
        self.pushButton_2.clicked.connect(self.ubah_pasien)
        self.pushButton_3.clicked.connect(self.hapus_pasien)

        self.load_data()

        self.tableWidget.cellClicked.connect(self.tabel_diklik)


    def load_data(self):
        data = self.db.ambilSemuaPasien()
        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setColumnCount(8)

        headers = ["No RM", "Nama Pasien", "No Identitas", "Jenis Kelamin", "Gol. Darah", "Tempat Lahir", "No. Telepon", "Alamat"]
        self.tableWidget.setHorizontalHeaderLabels(headers)

        for row_idx, row_data in enumerate(data):
            for col_idx, value in enumerate(row_data):
                self.tableWidget.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))

    def simpan_pasien(self):
        rm = self.nomor_rmLineEdit.text()
        nama = self.nama_pasienLineEdit.text()
        identitas = self.no_identitasLineEdit.text()
        jk = self.jenis_kelaminComboBox.currentText()
        gol_darah = self.golongan_darahComboBox.currentText()
        tempat = self.tempat_lahirLineEdit.text()
        telp = self.no_teleponLineEdit.text()
        alamat = self.alamatLineEdit.text()

        if not rm or not nama:
            QMessageBox.warning(self, "Peringatan", "Nomor RM dan Nama Pasien wajib diisi.")
            return

        try:
            self.db.simpanPasien(rm, nama, identitas, jk, gol_darah, tempat, telp, alamat)
            QMessageBox.information(self, "Sukses", "Data pasien berhasil disimpan!")
            self.load_data()
            self.clear_form()
        except Exception as e:
            QMessageBox.critical(self, "Error Simpan", f"Gagal menyimpan data: {str(e)}")

    def ubah_pasien(self):
        rm = self.nomor_rmLineEdit.text()
        nama = self.nama_pasienLineEdit.text()
        identitas = self.no_identitasLineEdit.text()
        jk = self.jenis_kelaminComboBox.currentText()
        gol_darah = self.golongan_darahComboBox.currentText()
        tempat = self.tempat_lahirLineEdit.text()
        telp = self.no_teleponLineEdit.text()
        alamat = self.alamatLineEdit.text()

        if not rm:
            QMessageBox.warning(self, "Peringatan", "Nomor RM harus diisi untuk mengubah data.")
            return

        try:
            self.db.ubahPasien(rm, nama, identitas, jk, gol_darah, tempat, telp, alamat)
            QMessageBox.information(self, "Sukses", "Data pasien berhasil diubah!")
            self.load_data()
            self.clear_form()
        except Exception as e:
            QMessageBox.critical(self, "Error Ubah", f"Gagal mengubah data: {str(e)}")

    def hapus_pasien(self):
        rm = self.nomor_rmLineEdit.text()
        if not rm:
            QMessageBox.warning(self, "Peringatan", "Pilih data yang akan dihapus dari tabel.")
            return

        confirm = QMessageBox.question(
            self,
            "Konfirmasi",
            f"Yakin ingin menghapus pasien dengan RM {rm}?",
            QMessageBox.Yes | QMessageBox.No
        )
        if confirm == QMessageBox.Yes:
            try:
                self.db.hapusPasien(rm)
                QMessageBox.information(self, "Sukses", "Data pasien berhasil dihapus!")
                self.load_data()
                self.clear_form()
            except Exception as e:
                QMessageBox.critical(self, "Error Hapus", f"Gagal menghapus data: {str(e)}")

    def tabel_diklik(self, row, column):
        try:
            self.nomor_rmLineEdit.setText(self.tableWidget.item(row, 0).text())
            self.nama_pasienLineEdit.setText(self.tableWidget.item(row, 1).text())
            self.no_identitasLineEdit.setText(self.tableWidget.item(row, 2).text())

            jk = self.tableWidget.item(row, 3).text()
            index_jk = self.jenis_kelaminComboBox.findText(jk)
            if index_jk >= 0:
                self.jenis_kelaminComboBox.setCurrentIndex(index_jk)

            gol_darah = self.tableWidget.item(row, 4).text()
            index_gd = self.golongan_darahComboBox.findText(gol_darah)
            if index_gd >= 0:
                self.golongan_darahComboBox.setCurrentIndex(index_gd)

            self.tempat_lahirLineEdit.setText(self.tableWidget.item(row, 5).text())
            self.no_teleponLineEdit.setText(self.tableWidget.item(row, 6).text())
            self.alamatLineEdit.setText(self.tableWidget.item(row, 7).text())
        except Exception as e:
            print(f"Error saat mengisi form dari tabel: {e}")

    def clear_form(self):
        self.nomor_rmLineEdit.clear()
        self.nama_pasienLineEdit.clear()
        self.no_identitasLineEdit.clear()
        self.jenis_kelaminComboBox.setCurrentIndex(0)
        self.golongan_darahComboBox.setCurrentIndex(0)
        self.tempat_lahirLineEdit.clear()
        self.no_teleponLineEdit.clear()
        self.alamatLineEdit.clear()

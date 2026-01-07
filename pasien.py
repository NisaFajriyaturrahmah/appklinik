# -*- coding: utf-8 -*-
import sys
from PySide6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem, QWidget, QFileDialog
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from fpdf import FPDF

from db import DB

class FormPasien(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        # 1. Load File UI
        ui_file = QFile("form_pasien.ui")
        if not ui_file.open(QFile.ReadOnly):
            print("Gagal membuka form_pasien.ui")
            sys.exit(-1)

        loader = QUiLoader()
        self.ui = loader.load(ui_file)
        ui_file.close()

        if not self.ui:
            print("Gagal memuat UI pasien")
            sys.exit(-1)

        for widget in self.ui.findChildren(QWidget):
            if widget.objectName():
                setattr(self, widget.objectName(), widget)

        self.setCentralWidget(self.ui.centralwidget)
        self.resize(self.ui.size())
        self.db = DB()

        self.jenis_kelaminComboBox.clear()
        self.jenis_kelaminComboBox.addItems(["Laki-laki", "Perempuan"])
        self.golongan_darahComboBox.clear()
        self.golongan_darahComboBox.addItems(["A", "B", "O", "AB"])

        self.pushButton.clicked.connect(self.simpan_pasien)
        self.pushButton_2.clicked.connect(self.ubah_pasien)
        self.pushButton_3.clicked.connect(self.hapus_pasien)

        if hasattr(self, 'lineCari'):
            self.lineCari.textChanged.connect(self.filter_pasien)
        if hasattr(self, 'btnCetak'):
            self.btnCetak.clicked.connect(self.cetak_pdf)

        self.tableWidget.cellClicked.connect(self.tabel_diklik)

        self.load_data()

    def load_data(self):
        data = self.db.ambilSemuaPasien()
        self.tampilkan_data_ke_tabel(data)

    def tampilkan_data_ke_tabel(self, data):
        self.tableWidget.setRowCount(len(data))
        for row_idx, row_data in enumerate(data):
            for col_idx, value in enumerate(row_data):
                self.tableWidget.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))

    def filter_pasien(self):
        keyword = self.lineCari.text()
        data = self.db.cariPasien(keyword)
        self.tampilkan_data_ke_tabel(data)

    def cetak_pdf(self):
        data = self.db.ambilSemuaPasien()
        if not data:
            QMessageBox.warning(self, "Peringatan", "Tidak ada data untuk dicetak.")
            return

        path, _ = QFileDialog.getSaveFileName(self, "Simpan Laporan", "", "PDF Files (*.pdf)")
        if path:
            try:
                pdf = FPDF(orientation='L', unit='mm', format='A4')
                pdf.add_page()
                pdf.set_font("Arial", "B", 16)
                pdf.cell(0, 10, "LAPORAN DATA PASIEN KLINIK", ln=True, align='C')
                pdf.ln(10)

                pdf.set_font("Arial", "B", 10)
                headers = ["No RM", "Nama Pasien", "Identitas", "L/P", "Gol", "Tpt Lahir", "Telp", "Alamat"]
                col_widths = [20, 45, 30, 20, 10, 30, 30, 80]

                for i, h in enumerate(headers):
                    pdf.cell(col_widths[i], 10, h, border=1, align='C')
                pdf.ln()

                pdf.set_font("Arial", "", 9)
                for row in data:
                    for i, value in enumerate(row):
                        pdf.cell(col_widths[i], 8, str(value), border=1)
                    pdf.ln()

                pdf.output(path)
                QMessageBox.information(self, "Sukses", "Laporan PDF berhasil dibuat!")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Gagal cetak PDF: {str(e)}")

    def simpan_pasien(self):
        try:
            self.db.simpanPasien(
                self.nomor_rmLineEdit.text(),
                self.nama_pasienLineEdit.text(),
                self.no_identitasLineEdit.text(),
                self.jenis_kelaminComboBox.currentText(),
                self.golongan_darahComboBox.currentText(),
                self.tempat_lahirLineEdit.text(),
                self.no_teleponLineEdit.text(),
                self.alamatLineEdit.text()
            )
            QMessageBox.information(self, "Sukses", "Data pasien disimpan!")
            self.load_data()
            self.clear_form()
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def ubah_pasien(self):
        try:
            self.db.ubahPasien(
                self.nomor_rmLineEdit.text(),
                self.nama_pasienLineEdit.text(),
                self.no_identitasLineEdit.text(),
                self.jenis_kelaminComboBox.currentText(),
                self.golongan_darahComboBox.currentText(),
                self.tempat_lahirLineEdit.text(),
                self.no_teleponLineEdit.text(),
                self.alamatLineEdit.text()
            )
            QMessageBox.information(self, "Sukses", "Data pasien diubah!")
            self.load_data()
            self.clear_form()
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def hapus_pasien(self):
        rm = self.nomor_rmLineEdit.text()
        confirm = QMessageBox.question(self, "Konfirmasi", f"Hapus Pasien {rm}?", QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            try:
                self.db.hapusPasien(rm)
                QMessageBox.information(self, "Sukses", "Data dihapus!")
                self.load_data()
                self.clear_form()
            except Exception as e:
                QMessageBox.critical(self, "Error", str(e))

    def tabel_diklik(self, row, column):
        self.nomor_rmLineEdit.setText(self.tableWidget.item(row, 0).text())
        self.nama_pasienLineEdit.setText(self.tableWidget.item(row, 1).text())
        self.no_identitasLineEdit.setText(self.tableWidget.item(row, 2).text())
        self.jenis_kelaminComboBox.setCurrentText(self.tableWidget.item(row, 3).text())
        self.golongan_darahComboBox.setCurrentText(self.tableWidget.item(row, 4).text())
        self.tempat_lahirLineEdit.setText(self.tableWidget.item(row, 5).text())
        self.no_teleponLineEdit.setText(self.tableWidget.item(row, 6).text())
        self.alamatLineEdit.setText(self.tableWidget.item(row, 7).text())

    def clear_form(self):
        self.nomor_rmLineEdit.clear()
        self.nama_pasienLineEdit.clear()
        self.no_identitasLineEdit.clear()
        self.tempat_lahirLineEdit.clear()
        self.no_teleponLineEdit.clear()
        self.alamatLineEdit.clear()

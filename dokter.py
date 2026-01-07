# -*- coding: utf-8 -*-
import sys
from PySide6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem, QWidget, QFileDialog
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from fpdf import FPDF

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

        for widget in self.ui.findChildren(QWidget):
            if widget.objectName():
                setattr(self, widget.objectName(), widget)

        self.setCentralWidget(self.ui.centralwidget)
        self.resize(self.ui.size())
        self.db = DB()

        self.ui.jenis_kelaminComboBox.clear()
        self.ui.jenis_kelaminComboBox.addItems(["Laki-laki", "Perempuan"])

        if hasattr(self, 'lineCari'):
            self.lineCari.textChanged.connect(self.filter_dokter)
        if hasattr(self, 'btnCetak'):
            self.btnCetak.clicked.connect(self.cetak_pdf)

        self.ui.pushButton.clicked.connect(self.simpan_dokter)
        self.ui.pushButton_2.clicked.connect(self.ubah_dokter)
        self.ui.pushButton_3.clicked.connect(self.hapus_dokter)

        self.load_data()
        self.ui.tableWidget.cellClicked.connect(self.tabel_diklik)

    def load_data(self):
        data = self.db.ambilSemuaDokter()
        self.tampilkan_data_ke_tabel(data)

    def tampilkan_data_ke_tabel(self, data):
        self.ui.tableWidget.setRowCount(len(data))
        for row_idx, row_data in enumerate(data):
            for col_idx, value in enumerate(row_data):
                self.ui.tableWidget.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))

    def filter_dokter(self):
        keyword = self.lineCari.text()
        data = self.db.cariDokter(keyword)
        self.tampilkan_data_ke_tabel(data)

    def cetak_pdf(self):
        data = self.db.ambilSemuaDokter()
        if not data:
            QMessageBox.warning(self, "Peringatan", "Tidak ada data untuk dicetak.")
            return

        path, _ = QFileDialog.getSaveFileName(self, "Simpan Laporan", "", "PDF Files (*.pdf)")
        if path:
            try:
                pdf = FPDF(orientation='L', unit='mm', format='A4')
                pdf.add_page()
                pdf.set_font("Arial", "B", 16)
                pdf.cell(0, 10, "LAPORAN DATA DOKTER KLINIK", ln=True, align='C')
                pdf.ln(10)

                # Header Tabel
                pdf.set_font("Arial", "B", 10)
                headers = ["ID", "Nama Dokter", "L/P", "Tempat Lahir", "Alamat", "Telepon", "Spesialis"]
                col_widths = [15, 45, 25, 35, 60, 35, 50]

                for i, h in enumerate(headers):
                    pdf.cell(col_widths[i], 10, h, border=1, align='C')
                pdf.ln()

                # Isi Tabel
                pdf.set_font("Arial", "", 9)
                for row in data:
                    for i, value in enumerate(row):
                        pdf.cell(col_widths[i], 8, str(value), border=1)
                    pdf.ln()

                pdf.output(path)
                QMessageBox.information(self, "Sukses", f"Laporan PDF berhasil disimpan!")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Gagal cetak: {str(e)}")

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
        confirm = QMessageBox.question(self, "Konfirmasi", f"Yakin menghapus {kd}?", QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            try:
                self.db.hapusDokter(kd)
                QMessageBox.information(self, "Sukses", "Data berhasil dihapus!")
                self.load_data()
                self.clear_form()
            except Exception as e:
                QMessageBox.critical(self, "Error", str(e))

    def tabel_diklik(self, row, column):
        self.ui.kd_dokterLineEdit.setText(self.ui.tableWidget.item(row, 0).text())
        self.ui.nama_dokterLineEdit.setText(self.ui.tableWidget.item(row, 1).text())
        jk = self.ui.tableWidget.item(row, 2).text()
        index = self.ui.jenis_kelaminComboBox.findText(jk)
        if index >= 0: self.ui.jenis_kelaminComboBox.setCurrentIndex(index)
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

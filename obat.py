# -*- coding: utf-8 -*-
import sys
from PySide6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem, QWidget, QFileDialog
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from fpdf import FPDF

from db import DB

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

        for widget in self.ui.findChildren(QWidget):
            if widget.objectName():
                setattr(self, widget.objectName(), widget)

        self.setCentralWidget(self.ui.centralwidget)
        self.resize(self.ui.size())
        self.setWindowTitle("Form Data Obat")
        self.db = DB()

        self.pushButton.clicked.connect(self.simpan_obat)
        self.pushButton_2.clicked.connect(self.ubah_obat)
        self.pushButton_3.clicked.connect(self.hapus_obat)

        if hasattr(self, 'lineCari'):
            self.lineCari.textChanged.connect(self.filter_obat)
        if hasattr(self, 'btnCetak'):
            self.btnCetak.clicked.connect(self.cetak_pdf)

        self.tableWidget.cellClicked.connect(self.tabel_diklik)

        self.load_data()

    def load_data(self):
        data = self.db.ambilSemuaObat()
        self.tampilkan_data_ke_tabel(data)

    def tampilkan_data_ke_tabel(self, data):
        self.tableWidget.setRowCount(len(data))
        for row_idx, row_data in enumerate(data):
            for col_idx, value in enumerate(row_data):
                self.tableWidget.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))

    def filter_obat(self):
        keyword = self.lineCari.text()
        data = self.db.cariObat(keyword)
        self.tampilkan_data_ke_tabel(data)

    def cetak_pdf(self):
        data = self.db.ambilSemuaObat()
        if not data:
            QMessageBox.warning(self, "Peringatan", "Tidak ada data untuk dicetak.")
            return

        path, _ = QFileDialog.getSaveFileName(self, "Simpan Laporan", "", "PDF Files (*.pdf)")
        if path:
            try:
                pdf = FPDF(orientation='P', unit='mm', format='A4')
                pdf.add_page()
                pdf.set_font("Arial", "B", 16)
                pdf.cell(0, 10, "LAPORAN DATA OBAT", ln=True, align='C')
                pdf.ln(10)

                pdf.set_font("Arial", "B", 10)
                headers = ["Kode Obat", "Nama Obat", "Harga", "Stok", "Keterangan"]
                col_widths = [30, 50, 30, 20, 60]

                for i, h in enumerate(headers):
                    pdf.cell(col_widths[i], 10, h, border=1, align='C')
                pdf.ln()

                pdf.set_font("Arial", "", 10)
                for row in data:
                    for i, value in enumerate(row):
                        pdf.cell(col_widths[i], 8, str(value), border=1)
                    pdf.ln()

                pdf.output(path)
                QMessageBox.information(self, "Sukses", "Laporan PDF Obat berhasil dibuat!")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Gagal cetak PDF: {str(e)}")

    def simpan_obat(self):
        try:
            self.db.simpanObat(
                self.kd_obatLineEdit.text(),
                self.nama_obatLineEdit.text(),
                self.hargaLineEdit.text(),
                self.stokLineEdit.text(),
                self.keteranganLineEdit.text()
            )
            QMessageBox.information(self, "Sukses", "Data obat berhasil disimpan!")
            self.load_data()
            self.clear_form()
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def ubah_obat(self):
        try:
            self.db.ubahObat(
                self.kd_obatLineEdit.text(),
                self.nama_obatLineEdit.text(),
                self.hargaLineEdit.text(),
                self.stokLineEdit.text(),
                self.keteranganLineEdit.text()
            )
            QMessageBox.information(self, "Sukses", "Data obat berhasil diubah!")
            self.load_data()
            self.clear_form()
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def hapus_obat(self):
        kd = self.kd_obatLineEdit.text()
        confirm = QMessageBox.question(self, "Konfirmasi", f"Hapus Obat {kd}?", QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            try:
                self.db.hapusObat(kd)
                QMessageBox.information(self, "Sukses", "Data berhasil dihapus!")
                self.load_data()
                self.clear_form()
            except Exception as e:
                QMessageBox.critical(self, "Error", str(e))

    def tabel_diklik(self, row, column):
        self.kd_obatLineEdit.setText(self.tableWidget.item(row, 0).text())
        self.nama_obatLineEdit.setText(self.tableWidget.item(row, 1).text())
        self.hargaLineEdit.setText(self.tableWidget.item(row, 2).text())
        self.stokLineEdit.setText(self.tableWidget.item(row, 3).text())
        self.keteranganLineEdit.setText(self.tableWidget.item(row, 4).text())

    def clear_form(self):
        self.kd_obatLineEdit.clear()
        self.nama_obatLineEdit.clear()
        self.hargaLineEdit.clear()
        self.stokLineEdit.clear()
        self.keteranganLineEdit.clear()

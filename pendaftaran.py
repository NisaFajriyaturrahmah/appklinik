# -*- coding: utf-8 -*-
import sys
from PySide6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem, QWidget, QFileDialog
from PySide6.QtCore import QFile, QDate, QTime
from PySide6.QtUiTools import QUiLoader
from fpdf import FPDF

from db import DB

class FormPendaftaran(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        ui_file = QFile("form_pendaftaran.ui")
        if not ui_file.open(QFile.ReadOnly):
            print("Gagal membuka form_pendaftaran.ui")
            sys.exit(-1)

        loader = QUiLoader()
        self.ui = loader.load(ui_file)
        ui_file.close()

        if not self.ui:
            print("Gagal memuat UI pendaftaran")
            sys.exit(-1)

        for widget in self.ui.findChildren(QWidget):
            if widget.objectName():
                setattr(self, widget.objectName(), widget)

        self.setCentralWidget(self.ui.centralwidget)
        self.resize(self.ui.size())
        self.db = DB()

        self.tanggal_daftarDateEdit.setCalendarPopup(True)
        self.tanggal_daftarDateEdit.setDate(QDate.currentDate())
        self.tanggal_janjiDateEdit.setCalendarPopup(True)
        self.tanggal_janjiDateEdit.setDate(QDate.currentDate())
        self.jam_janjiTimeEdit.setTime(QTime.currentTime())

        self.pushButton.clicked.connect(self.simpan_pendaftaran)
        self.pushButton_2.clicked.connect(self.ubah_pendaftaran)
        self.pushButton_3.clicked.connect(self.hapus_pendaftaran)

        if hasattr(self, 'lineCari'):
            self.lineCari.textChanged.connect(self.filter_pendaftaran)
        if hasattr(self, 'btnCetak'):
            self.btnCetak.clicked.connect(self.cetak_pdf)

        self.tableWidget.cellClicked.connect(self.tabel_diklik)

        self.load_data()

    def load_data(self):
        data = self.db.tampilPendaftaran()
        self.tampilkan_data_ke_tabel(data)

    def tampilkan_data_ke_tabel(self, data):
        self.tableWidget.setRowCount(len(data))
        for row_idx, row_data in enumerate(data):
            for col_idx, value in enumerate(row_data):
                display_value = str(value)
                self.tableWidget.setItem(row_idx, col_idx, QTableWidgetItem(display_value))
        self.tableWidget.resizeColumnsToContents()

    def filter_pendaftaran(self):
        keyword = self.lineCari.text()
        data = self.db.cariPendaftaran(keyword)
        self.tampilkan_data_ke_tabel(data)

    def cetak_pdf(self):
        data = self.db.tampilPendaftaran()
        if not data:
            QMessageBox.warning(self, "Peringatan", "Tidak ada data untuk dicetak.")
            return

        path, _ = QFileDialog.getSaveFileName(self, "Simpan Laporan", "", "PDF Files (*.pdf)")
        if path:
            try:
                pdf = FPDF(orientation='L', unit='mm', format='A4')
                pdf.add_page()
                pdf.set_font("Arial", "B", 16)
                pdf.cell(0, 10, "LAPORAN PENDAFTARAN PASIEN", ln=True, align='C')
                pdf.ln(10)

                pdf.set_font("Arial", "B", 10)
                headers = ["No Daftar", "No RM", "Tgl Daftar", "Tgl Janji", "Jam", "Keluhan", "Petugas"]
                col_widths = [25, 25, 30, 30, 20, 110, 35]

                for i, h in enumerate(headers):
                    pdf.cell(col_widths[i], 10, h, border=1, align='C')
                pdf.ln()

                pdf.set_font("Arial", "", 9)
                for row in data:
                    for i, value in enumerate(row):
                        pdf.cell(col_widths[i], 8, str(value), border=1)
                    pdf.ln()

                pdf.output(path)
                QMessageBox.information(self, "Sukses", "Laporan PDF berhasil disimpan!")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Gagal cetak: {str(e)}")

    def get_input_data(self):
        return (
            self.no_daftarLineEdit.text(),
            self.nomor_rmLineEdit.text(),
            self.tanggal_daftarDateEdit.date().toString("yyyy-MM-dd"),
            self.tanggal_janjiDateEdit.date().toString("yyyy-MM-dd"),
            self.jam_janjiTimeEdit.time().toString("HH:mm:ss"),
            self.keluhanLineEdit.text(),
            self.kd_petugasLineEdit.text()
        )

    def simpan_pendaftaran(self):
        vals = self.get_input_data()
        if not vals[0] or not vals[1]:
            QMessageBox.warning(self, "Peringatan", "No Daftar dan Nomor RM wajib diisi!")
            return

        try:
            self.db.simpanPendaftaran(*vals)
            QMessageBox.information(self, "Sukses", "Data berhasil disimpan!")
            self.load_data()
            self.clear_form()
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def ubah_pendaftaran(self):
        vals = self.get_input_data()
        try:
            self.db.ubahPendaftaran(*vals)
            QMessageBox.information(self, "Sukses", "Data berhasil diubah!")
            self.load_data()
            self.clear_form()
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def hapus_pendaftaran(self):
        no = self.no_daftarLineEdit.text()
        if not no: return
        confirm = QMessageBox.question(self, "Konfirmasi", f"Hapus pendaftaran {no}?", QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            try:
                self.db.hapusPendaftaran(no)
                QMessageBox.information(self, "Sukses", "Data dihapus!")
                self.load_data()
                self.clear_form()
            except Exception as e:
                QMessageBox.critical(self, "Error", str(e))

    def tabel_diklik(self, row, column):
        self.no_daftarLineEdit.setText(self.tableWidget.item(row, 0).text())
        self.nomor_rmLineEdit.setText(self.tableWidget.item(row, 1).text())

        tgl_daftar = QDate.fromString(self.tableWidget.item(row, 2).text(), "yyyy-MM-dd")
        self.tanggal_daftarDateEdit.setDate(tgl_daftar)

        tgl_janji = QDate.fromString(self.tableWidget.item(row, 3).text(), "yyyy-MM-dd")
        self.tanggal_janjiDateEdit.setDate(tgl_janji)

        jam = QTime.fromString(self.tableWidget.item(row, 4).text(), "HH:mm:ss")
        self.jam_janjiTimeEdit.setTime(jam)

        self.keluhanLineEdit.setText(self.tableWidget.item(row, 5).text())
        self.kd_petugasLineEdit.setText(self.tableWidget.item(row, 6).text())

    def clear_form(self):
        self.no_daftarLineEdit.clear()
        self.nomor_rmLineEdit.clear()
        self.keluhanLineEdit.clear()
        self.kd_petugasLineEdit.clear()
        self.tanggal_daftarDateEdit.setDate(QDate.currentDate())
        self.tanggal_janjiDateEdit.setDate(QDate.currentDate())
        self.jam_janjiTimeEdit.setTime(QTime.currentTime())

# -*- coding: utf-8 -*-
import sys
from PySide6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem, QWidget, QFileDialog
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from fpdf import FPDF

from db import DB

class FormPetugas(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        ui_file = QFile("form_petugas.ui")
        if not ui_file.open(QFile.ReadOnly):
            print("Gagal membuka form_petugas.ui")
            sys.exit(-1)

        loader = QUiLoader()
        self.ui = loader.load(ui_file)
        ui_file.close()

        if not self.ui:
            print("Gagal memuat UI petugas")
            sys.exit(-1)

        for widget in self.ui.findChildren(QWidget):
            if widget.objectName():
                setattr(self, widget.objectName(), widget)

        self.setCentralWidget(self.ui.centralwidget)
        self.resize(self.ui.size())
        self.db = DB()

        self.levelComboBox.clear()
        self.levelComboBox.addItems(["admin", "operator", "dokter"])

        self.pushButton.clicked.connect(self.simpan_petugas)
        self.pushButton_2.clicked.connect(self.ubah_petugas)
        self.pushButton_3.clicked.connect(self.hapus_petugas)

        if hasattr(self, 'lineCari'):
            self.lineCari.textChanged.connect(self.filter_petugas)
        if hasattr(self, 'btnCetak'):
            self.btnCetak.clicked.connect(self.cetak_pdf)

        self.tableWidget.cellClicked.connect(self.tabel_diklik)

        self.load_data()

    def load_data(self):
        data = self.db.ambilSemuaPetugas()
        self.tampilkan_data_ke_tabel(data)

    def tampilkan_data_ke_tabel(self, data):
        self.tableWidget.setRowCount(len(data))
        for row_idx, row_data in enumerate(data):
            for col_idx, value in enumerate(row_data):
                self.tableWidget.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))

    def filter_petugas(self):
        keyword = self.lineCari.text()
        data = self.db.cariPetugas(keyword)
        self.tampilkan_data_ke_tabel(data)

    def cetak_pdf(self):
        data = self.db.ambilSemuaPetugas()
        if not data:
            QMessageBox.warning(self, "Peringatan", "Tidak ada data untuk dicetak.")
            return

        path, _ = QFileDialog.getSaveFileName(self, "Simpan Laporan", "", "PDF Files (*.pdf)")
        if path:
            try:
                pdf = FPDF(orientation='P', unit='mm', format='A4')
                pdf.add_page()
                pdf.set_font("Arial", "B", 16)
                pdf.cell(0, 10, "LAPORAN DATA PETUGAS KLINIK", ln=True, align='C')
                pdf.ln(10)

                pdf.set_font("Arial", "B", 10)
                headers = ["ID", "Nama Petugas", "Telepon", "Username", "Level"]
                col_widths = [20, 50, 40, 40, 40]

                for i, h in enumerate(headers):
                    pdf.cell(col_widths[i], 10, h, border=1, align='C')
                pdf.ln()

                pdf.set_font("Arial", "", 10)
                for row in data:
                    pdf.cell(col_widths[0], 8, str(row[0]), border=1)
                    pdf.cell(col_widths[1], 8, str(row[1]), border=1)
                    pdf.cell(col_widths[2], 8, str(row[2]), border=1)
                    pdf.cell(col_widths[3], 8, str(row[3]), border=1)
                    pdf.cell(col_widths[4], 8, str(row[5]), border=1)
                    pdf.ln()

                pdf.output(path)
                QMessageBox.information(self, "Sukses", "Laporan Petugas berhasil dicetak!")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Gagal cetak PDF: {str(e)}")

    def simpan_petugas(self):
        try:
            self.db.simpanPetugas(
                self.kd_petugasLineEdit.text(),
                self.nama_petugasLineEdit.text(),
                self.no_teleponLineEdit.text(),
                self.usernameLineEdit.text(),
                self.passwordLineEdit.text(),
                self.levelComboBox.currentText()
            )
            QMessageBox.information(self, "Sukses", "Data petugas berhasil disimpan!")
            self.load_data()
            self.clear_form()
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def ubah_petugas(self):
        try:
            self.db.ubahPetugas(
                self.kd_petugasLineEdit.text(),
                self.nama_petugasLineEdit.text(),
                self.no_teleponLineEdit.text(),
                self.usernameLineEdit.text(),
                self.passwordLineEdit.text(),
                self.levelComboBox.currentText()
            )
            QMessageBox.information(self, "Sukses", "Data petugas berhasil diubah!")
            self.load_data()
            self.clear_form()
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def hapus_petugas(self):
        kd = self.kd_petugasLineEdit.text()
        confirm = QMessageBox.question(self, "Konfirmasi", f"Hapus petugas {kd}?", QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            try:
                self.db.hapusPetugas(kd)
                QMessageBox.information(self, "Sukses", "Data berhasil dihapus!")
                self.load_data()
                self.clear_form()
            except Exception as e:
                QMessageBox.critical(self, "Error", str(e))

    def tabel_diklik(self, row, column):
        self.kd_petugasLineEdit.setText(self.tableWidget.item(row, 0).text())
        self.nama_petugasLineEdit.setText(self.tableWidget.item(row, 1).text())
        self.no_teleponLineEdit.setText(self.tableWidget.item(row, 2).text())
        self.usernameLineEdit.setText(self.tableWidget.item(row, 3).text())
        self.passwordLineEdit.setText(self.tableWidget.item(row, 4).text())
        self.levelComboBox.setCurrentText(self.tableWidget.item(row, 5).text())

    def clear_form(self):
        self.kd_petugasLineEdit.clear()
        self.nama_petugasLineEdit.clear()
        self.no_teleponLineEdit.clear()
        self.usernameLineEdit.clear()
        self.passwordLineEdit.clear()
        self.levelComboBox.setCurrentIndex(0)

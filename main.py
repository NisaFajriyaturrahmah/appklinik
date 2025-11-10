# -*- coding: utf-8 -*-
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader

from dokter import FormDokter
from pasien import FormPasien
from petugas import FormPetugas
from obat import FormObat
from pendaftaran import FormPendaftaran

class Main(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        ui_file = QFile("form.ui")
        if not ui_file.open(QFile.ReadOnly):
            print("Gagal membuka form.ui")
            sys.exit(-1)

        loader = QUiLoader()
        self.formUtama = loader.load(ui_file, self)
        ui_file.close()

        if not self.formUtama:
            print("Gagal memuat UI")
            sys.exit(-1)

        self.setCentralWidget(self.formUtama)
        self.setMenuBar(self.formUtama.menuBar())
        self.resize(self.formUtama.size())

        self.formUtama.actionForm_Dokter.triggered.connect(self.bukaDokter)
        self.formUtama.actionForm_Pasien.triggered.connect(self.bukaPasien)
        self.formUtama.actionForm_Petugas.triggered.connect(self.bukaPetugas)
        self.formUtama.actionForm_Obat.triggered.connect(self.bukaObat)
        self.formUtama.actionFrom_Pendaftaran.triggered.connect(self.bukaPendaftaran)

    def bukaDokter(self):
        self.dokterForm = FormDokter()
        self.dokterForm.show()

    def bukaPasien(self):
        self.pasienForm = FormPasien()
        self.pasienForm.show()

    def bukaPetugas(self):
        self.petugasForm = FormPetugas()
        self.petugasForm.show()

    def bukaObat(self):
        self.obatForm = FormObat()
        self.obatForm.show()

    def bukaPendaftaran(self):
        self.pendaftaranForm = FormPendaftaran()
        self.pendaftaranForm.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec())

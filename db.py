# -*- coding: utf-8 -*-
import mysql.connector

class DB:
    def __init__(self):
        self.koneksi = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='klinik'
        )

    def simpanDokter(self, kd, nama, jk, tempat, alamat, telp, spesialis):
        cursor = self.koneksi.cursor()
        sql = """INSERT INTO dokter
                 (kd_dokter, nama_dokter, jenis_kelamin, tempat_lahir, alamat, no_telepon, spesialisasi)
                 VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        cursor.execute(sql, (kd, nama, jk, tempat, alamat, telp, spesialis))
        self.koneksi.commit()
        cursor.close()

    def ubahDokter(self, kd, nama, jk, tempat, alamat, telp, spesialis):
        cursor = self.koneksi.cursor()
        sql = """UPDATE dokter SET
                    nama_dokter=%s,
                    jenis_kelamin=%s,
                    tempat_lahir=%s,
                    alamat=%s,
                    no_telepon=%s,
                    spesialisasi=%s
                 WHERE kd_dokter=%s"""
        cursor.execute(sql, (nama, jk, tempat, alamat, telp, spesialis, kd))
        self.koneksi.commit()
        cursor.close()

    def hapusDokter(self, kd):
        cursor = self.koneksi.cursor()
        sql = "DELETE FROM dokter WHERE kd_dokter=%s"
        cursor.execute(sql, (kd,))
        self.koneksi.commit()
        cursor.close()

    def ambilSemuaDokter(self):
        cursor = self.koneksi.cursor()
        cursor.execute("SELECT * FROM dokter")
        data = cursor.fetchall()
        cursor.close()
        return data

    def cariDokter(self, keyword):
        cursor = self.koneksi.cursor()
        sql = """SELECT * FROM dokter
                 WHERE kd_dokter LIKE %s OR nama_dokter LIKE %s OR spesialisasi LIKE %s"""
        val = (f"%{keyword}%", f"%{keyword}%", f"%{keyword}%")
        cursor.execute(sql, val)
        data = cursor.fetchall()
        cursor.close()
        return data

    def simpanPasien(self, rm, nama, identitas, jk, gol_darah, tempat, telp, alamat):
        cursor = self.koneksi.cursor()
        sql = """INSERT INTO pasien
                 (nomor_rm, nama_pasien, no_identitas, jenis_kelamin, golongan_darah, tempat_lahir, no_telepon, alamat)
                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
        cursor.execute(sql, (rm, nama, identitas, jk, gol_darah, tempat, telp, alamat))
        self.koneksi.commit()
        cursor.close()

    def ubahPasien(self, rm, nama, identitas, jk, gol_darah, tempat, telp, alamat):
        cursor = self.koneksi.cursor()
        sql = """UPDATE pasien SET
                    nama_pasien=%s,
                    no_identitas=%s,
                    jenis_kelamin=%s,
                    golongan_darah=%s,
                    tempat_lahir=%s,
                    no_telepon=%s,
                    alamat=%s
                 WHERE nomor_rm=%s"""
        cursor.execute(sql, (nama, identitas, jk, gol_darah, tempat, telp, alamat, rm))
        self.koneksi.commit()
        cursor.close()

    def hapusPasien(self, rm):
        cursor = self.koneksi.cursor()
        sql = "DELETE FROM pasien WHERE nomor_rm=%s"
        cursor.execute(sql, (rm,))
        self.koneksi.commit()
        cursor.close()

    def ambilSemuaPasien(self):
        cursor = self.koneksi.cursor()
        sql = "SELECT nomor_rm, nama_pasien, no_identitas, jenis_kelamin, golongan_darah, tempat_lahir, no_telepon, alamat FROM pasien"
        cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close()
        return data

    def cariPasien(self, keyword):
        cursor = self.koneksi.cursor()
        sql = """SELECT * FROM pasien
                 WHERE nomor_rm LIKE %s OR nama_pasien LIKE %s OR alamat LIKE %s"""
        val = (f"%{keyword}%", f"%{keyword}%", f"%{keyword}%")
        cursor.execute(sql, val)
        data = cursor.fetchall()
        cursor.close()
        return data

    def simpanPetugas(self, kd, nama, telp, username, password, level):
        cursor = self.koneksi.cursor()
        sql = """INSERT INTO petugas
                 (kd_petugas, nama_petugas, no_telepon, username, password, level)
                 VALUES (%s, %s, %s, %s, %s, %s)"""
        cursor.execute(sql, (kd, nama, telp, username, password, level))
        self.koneksi.commit()
        cursor.close()

    def ubahPetugas(self, kd, nama, telp, username, password, level):
        cursor = self.koneksi.cursor()
        sql = """UPDATE petugas SET
                    nama_petugas=%s,
                    no_telepon=%s,
                    username=%s,
                    password=%s,
                    level=%s
                 WHERE kd_petugas=%s"""
        cursor.execute(sql, (nama, telp, username, password, level, kd))
        self.koneksi.commit()
        cursor.close()

    def hapusPetugas(self, kd):
        cursor = self.koneksi.cursor()
        sql = "DELETE FROM petugas WHERE kd_petugas=%s"
        cursor.execute(sql, (kd,))
        self.koneksi.commit()
        cursor.close()

    def ambilSemuaPetugas(self):
        cursor = self.koneksi.cursor()
        cursor.execute("SELECT * FROM petugas")
        data = cursor.fetchall()
        cursor.close()
        return data

    def cariPetugas(self, keyword):
        cursor = self.koneksi.cursor()
        sql = """SELECT * FROM petugas
                 WHERE kd_petugas LIKE %s OR nama_petugas LIKE %s OR username LIKE %s"""
        val = (f"%{keyword}%", f"%{keyword}%", f"%{keyword}%")
        cursor.execute(sql, val)
        data = cursor.fetchall()
        cursor.close()
        return data

    def simpanObat(self, kd, nama, harga, stok, keterangan):
        cursor = self.koneksi.cursor()
        sql = """INSERT INTO obat
                 (kd_obat, nama_obat, harga, stok, keterangan)
                 VALUES (%s, %s, %s, %s, %s)"""
        cursor.execute(sql, (kd, nama, harga, stok, keterangan))
        self.koneksi.commit()
        cursor.close()

    def ubahObat(self, kd, nama, harga, stok, keterangan):
        cursor = self.koneksi.cursor()
        sql = """UPDATE obat SET
                    nama_obat=%s,
                    harga=%s,
                    stok=%s,
                    keterangan=%s
                 WHERE kd_obat=%s"""
        cursor.execute(sql, (nama, harga, stok, keterangan, kd))
        self.koneksi.commit()
        cursor.close()

    def hapusObat(self, kd):
        cursor = self.koneksi.cursor()
        sql = "DELETE FROM obat WHERE kd_obat=%s"
        cursor.execute(sql, (kd,))
        self.koneksi.commit()
        cursor.close()

    def ambilSemuaObat(self):
        cursor = self.koneksi.cursor()
        cursor.execute("SELECT * FROM obat")
        data = cursor.fetchall()
        cursor.close()
        return data

    def cariObat(self, keyword):
        cursor = self.koneksi.cursor()
        sql = """SELECT * FROM obat
                 WHERE kd_obat LIKE %s OR nama_obat LIKE %s OR keterangan LIKE %s"""
        val = (f"%{keyword}%", f"%{keyword}%", f"%{keyword}%")
        cursor.execute(sql, val)
        data = cursor.fetchall()
        cursor.close()
        return data

    def simpanPendaftaran(self, no_daftar, nomor_rm, tgl_daftar, tgl_janji, jam_janji, keluhan, kd_petugas):
        cursor = self.koneksi.cursor()
        sql = """INSERT INTO pendaftaran
                 (no_daftar, nomor_rm, tanggal_daftar, tanggal_janji, jam_janji, keluhan, kd_petugas)
                 VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        cursor.execute(sql, (no_daftar, nomor_rm, tgl_daftar, tgl_janji, jam_janji, keluhan, kd_petugas))
        self.koneksi.commit()
        cursor.close()

    def ubahPendaftaran(self, no_daftar, nomor_rm, tgl_daftar, tgl_janji, jam_janji, keluhan, kd_petugas):
        cursor = self.koneksi.cursor()
        sql = """UPDATE pendaftaran SET
                     nomor_rm=%s,
                     tanggal_daftar=%s,
                     tanggal_janji=%s,
                     jam_janji=%s,
                     keluhan=%s,
                     kd_petugas=%s
                 WHERE no_daftar=%s"""
        cursor.execute(sql, (nomor_rm, tgl_daftar, tgl_janji, jam_janji, keluhan, kd_petugas, no_daftar))
        self.koneksi.commit()
        cursor.close()

    def hapusPendaftaran(self, no_daftar):
        cursor = self.koneksi.cursor()
        sql = "DELETE FROM pendaftaran WHERE no_daftar=%s"
        cursor.execute(sql, (no_daftar,))
        self.koneksi.commit()
        cursor.close()

    def ambilSemuaPendaftaran(self):
        cursor = self.koneksi.cursor()
        cursor.execute("SELECT no_daftar, nomor_rm, tanggal_daftar, tanggal_janji, jam_janji, keluhan, kd_petugas FROM pendaftaran")
        data = cursor.fetchall()
        cursor.close()
        return data

    def tampilPendaftaran(self):
        cursor = self.koneksi.cursor()
        cursor.execute("SELECT * FROM pendaftaran")
        data = cursor.fetchall()
        cursor.close()
        return data

    def cariPendaftaran(self, keyword):
        cursor = self.koneksi.cursor()
        sql = """SELECT * FROM pendaftaran
                 WHERE no_daftar LIKE %s OR nomor_rm LIKE %s OR keluhan LIKE %s"""
        val = (f"%{keyword}%", f"%{keyword}%", f"%{keyword}%")
        cursor.execute(sql, val)
        data = cursor.fetchall()
        cursor.close()
        return data

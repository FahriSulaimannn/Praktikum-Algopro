nama = "Fahri Sulaiman Wahab"
tanggal_lahir1 = "07-05-2007" #pada kegiatan 1 format tanggal lahir bisa diubah ke format dd-mm-yyyy
tanggal_lahir2 = "05-07-20027"
nim = "L200250029"
kota = "Bandung" #Pada kegiatan 1 teks ini bisa dihilangkan terlebih dahulu

berkas = open("L200250029", "w")
berkas.write(nim + "\n")
berkas.write(tanggal_lahir1 + "\n") # Pada kegiatan 1 teks [kota + " " + ] bisa dihilangkan terlebih dahulu
berkas.write(nama + "\n")
berkas.close()

# =========================================== Kegiatan 2 ===========================================
# =========================================== Kegiatan 2 Cara 1 ===========================================
berkas = open("L200250029", "w")
berkas.write(nim + "\n")
berkas.write(kota + " " + tanggal_lahir2 + "\n") # Pada kegiatan 1 teks [kota + " " + ] bisa dihilangkan terlebih dahulu
berkas.write(nama + "\n" + nim + "\n" + tanggal_lahir2 + "\n")
berkas.close()

berkas = open("L200250029", "r")
isi_berkas = berkas.read()
print(isi_berkas)
berkas.close()

# =========================================== Kegiatan 2 Cara 2 ===========================================
berkas = open("L200250029", "r")
isi_berkas = berkas.readlines()

nim_berkas = isi_berkas[0].strip()
tanggal_lahir_berkas = isi_berkas[1].strip()
nama_berkas = isi_berkas[2].strip()

dd, mm, yyyy = tanggal_lahir_berkas.split("-")
tanggal_lahir_baru = f"{mm}-{dd}-{yyyy}"
tanggal_lahir_final = f"{kota}, {tanggal_lahir_baru}"

berkas.close()


berkas = open("L200250029", "w")

berkas.write(nama_berkas + "\n")
berkas.write(tanggal_lahir_final + "\n")
berkas.write(nim_berkas + "\n")
berkas.close()

berkas = open("L200250029", "r")
print(berkas.read())
berkas.close()


# Pada kegiatan 3 bisa di uncomment kode di bawah ini

import shelve

# Baca data dari file L200250029
berkas = open("L200250029", "r")
isi_berkas = berkas.read()
berkas.close()

# Simpan ke shelve "fahri"
F = shelve.open("fahri")
F["data"] = isi_berkas
F.close()

# Kegiatan 4

F = shelve.open("fahri")
print(F["data"])
F.close()



# Kegiatan 1 

# Nomor 1
import Modul8 as md

md.nama()
md.nim()
md.alamat()
md.program_studi()
md.fakultas()
md.universitas()
md.tahun_angkatan()

print("=================================================================")

# Nomor 2
def menu():
    print(f"Pilihan yang tersedia: \nb menampilkan bantuan ini \nN menampilkan NIM \na menampikan Nama \nA menampilkan Alamat \nk menampilkan Kode pos \nk keluar \n" )
    while True:
        pilihan = input("Masukkan pilihan anda: ")
        if pilihan == "b":
            print(f"Pilihan yang tersedia: \nb menampilkan bantuan ini \nN menampilkan NIM \na menampikan Nama \nA menampilkan Alamat \nk menampilkan Kode pos \nk keluar \n" )
        elif pilihan == "N":
            md.nim()
        elif pilihan == "a":
            md.nama()
        elif pilihan == "A":
            md.alamat()
        elif pilihan == "k":
            print("Keluar dari program.")
            break
        else:
            print("Perintah tidak dikenal\n")
menu()

print("=================================================================")

# Kegiatan 2
def konversiSuhu(C=None, F=None):
    if C is  None:
        fahrenheit = (C * 9/5) + 32
        print(f"Suhu {C} Celsius setara dengan {fahrenheit} Fahrenheit")
    if F is not None:
        celcius = (F - 32) * 5/9
        print(f"Suhu {F} Fahrenhait setara dengan {celcius} Celsius")

konversiSuhu(36, 42)
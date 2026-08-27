# Kegiatan 1

bangaun_datar = {
    "Segitiga" : "L = 0.5 * a * t",
    "Persegi" : "L = s ** 2",
    "Persegi Panjang" : "L = p * l",
    "Lingkaran" : "L = phi * r ** 2",
    "Jajar Genjang" : "L = a * t",
}

print("No | Bangun Datar      | Rumus Luas")
print("---|-------------------|------------------")

no = 1
for bangun, rumus in bangaun_datar.items():
    print(f"{no:<3}| {bangun:<18}| {rumus}")
    no += 1

print("=================================================================")

# Kegiatan 2

password = "fahri"

for i in range(3):
    user_input = input("Masukkan password: ")
    if user_input == password:
        print("Anda berhasil login")
        break
    elif i == 2 and user_input != password:
        print("Anda telah mencoba 3 kali. Akses anda ditolak")
    else:
        print("Maaf, anda salah memasukkan password")

print("=================================================================")

# Kegiatan 3

waktu = ('pagi', 'siang', 'sore', 'malam')

input_nama = input("Masukkan nama anda : ")
input_waktu = float(input("Masukkan waktu : "))

if 4.00 <= input_waktu <= 10.00:
    print(f"Selamat {waktu[0]} {input_nama}")
elif 10.01 <= input_waktu <= 15.00:
    print(f"Selamat {waktu[1]} {input_nama}")
elif 15.01 <= input_waktu <= 18.00:
    print(f"Selamat {waktu[2]} {input_nama}")
else:
    print(f"Selamat {waktu[3]} {input_nama}")
## Program Identitas diri. Dibuat oleh Fahri L200250029

Nama = "Fahri Sulaiman Wahab"
Alamat = "Jl. Kerinci 07 No.08"
Kecamatan = "Banjarsari"
Kota = "Surakarta"
TTL = "07 Mei 2007"
Umur = "18 Tahun"
Status = "Pelajar"
Hobi = "Berolahraga"
Univ = "Universitas Muhammadiyah Surakarta"
Email = "akunnyaapaya63@gmail.com"

print("Perkenalkan nama saya", Nama, "dan alamat saya di", Alamat, Kecamatan, Kota, "saya lahir pada", TTL,
      "dan sekarang berumur", Umur, "dengan status", Status, "yang sedang berkuliah di", Univ,
      "saya memiliki hobi", Hobi, "Anda bisa menghubungi saya melalui email", Email)

print('=================================================================================')

## Program Akun
## Dibuat oleh Fahri L200250029

Nama = 'Fahri Sulaiman Wahab'
TanggalLahir = '07 Mei 2007'

print("Nama : " + Nama[:6] + Nama[6] + "." + Nama[15] + ".")
print("Username : " + Nama[0] + Nama[6] + Nama[15] + TanggalLahir[0] + TanggalLahir[1] + TanggalLahir[7:])
print("Password : " + Nama[:3] + "536")

print('=================================================================================')

## Kegiatan 3

Nama = 'Fahri Sulaiman Wahab'
NIM = 'L200250029'

x = '1' + NIM[7:]
print(x)
a = int(x)
print(a)
b = len(Nama)
print(b)

print(type(a))
print(type(b))
print(a / b)
print(a // b)
print(10 * (a - 999))
print(b ** 2)
print(a % b)

c = 12.5
print(c)
print(type(c))
print(a / c)
print(a // c)
print(a % c)

print(c > b)
print(type(c > b))
print(a > b and b > c)
print(a > 1100 or b < 10)

print('=================================================================================')

## Kegiatan 4

Nama = 'Fahri Sulaiman Wahab'
NIM = 129
Tinggi = 1.75
Berat = 70
TahunLahir = 2007
Aku = (TahunLahir, Berat, Tinggi, NIM, Nama)
print(Aku)
Data = [TahunLahir, Berat, Tinggi, NIM, Nama]
print(Data)

print(type(Aku))
print(Aku[0])
a = NIM % 4; Aku[a]
print(a, Aku[a])
print(type(Aku[a]))
print(Aku[a:4])
print(type(Aku[4]))
# Aku[0] = 'ok'
# print(Aku)

print(type(Data))
print(type(Data[4]))
print(Data[4][5])
print(Data[4][a:6])
Data[0] = 'ok'; Data
print(Data)
print(Data[-a])
print(range(a))

print('=================================================================================')

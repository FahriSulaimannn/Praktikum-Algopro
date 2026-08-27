# from tkinter import *
# from tkinter import ttk

# my_app = Tk()
# my_app.title("My App")
# frm = ttk.Frame(my_app, padding=20)
# frm.grid()

# # Label untuk menampilkan teks
# ttk.Label(frm, text="Data diri", font=("Arial", 18, "bold")).grid(column=0, row=0, sticky="w", pady=10)

# ttk.Label(frm, text="Nama : ", font=("Arial", 12)).grid(column=0, row=1, pady=10, sticky="w")
# ttk.Label(frm, text="Fahri Sulaiman Wahab", font=("Arial", 12)).grid(column=1, row=1, pady=10, sticky="w")

# ttk.Label(frm, text="NIM : ", font=("Arial", 12)).grid(column=0, row=2, pady=10, sticky="w")
# ttk.Label(frm, text="L20025002", font=("Arial", 12)).grid(column=1, row=2, pady=10, sticky="w")

# ttk.Label(frm, text="Buku favorit : ", font=("Arial", 12)).grid(column=0, row=3, pady=10, sticky="w")
# ttk.Label(frm, text="Belum diketahui", font=("Arial", 12)).grid(column=1, row=3, pady=10, sticky="w")

# ttk.Label(frm, text="Idola : ", font=("Arial", 12)).grid(column=0, row=4, pady=10, sticky="w")
# ttk.Label(frm, text="Lewis Hamilton", font=("Arial", 12)).grid(column=1, row=4, pady=10, sticky="w")

# ttk.Label(frm, text="Motto : ", font=("Arial", 12)).grid(column=0, row=5, pady=10, sticky="w")
# ttk.Label(frm, text="Tetap semangat!", font=("Arial", 12)).grid(column=1, row=5, pady=10, sticky="w")
# # Tombol Tutup
# ttk.Button(frm, text="Tutup", command=my_app.destroy).grid(column=0, row=6, columnspan=2, pady=10)

# my_app.mainloop()

# # =========================================== Kegiatan 2 ===========================================

# from tkinter.simpledialog import askinteger
# from tkinter import *
# from tkinter import ttk

# calculator = Tk()
# calculator.title("Calculator")
# frm = ttk.Frame(calculator, padding=20)
# frm.grid()

# def tambah():
#     a = float(entry1.get())
#     b = float(entry2.get())
#     hasil = a + b
#     ttk.Label(frm, text=f"Hasil: {hasil}", font=("Arial", 12)).grid(column=0, row=5, columnspan=4, pady=10)

# def kurang():
#     a = float(entry1.get())
#     b = float(entry2.get())
#     hasil = a - b
#     ttk.Label(frm, text=f"Hasil: {hasil}", font=("Arial", 12)).grid(column=0, row=5, columnspan=4, pady=10)

# def kali():
#     a = float(entry1.get())
#     b = float(entry2.get())
#     hasil = a * b
#     ttk.Label(frm, text=f"Hasil: {hasil}", font=("Arial", 12)).grid(column=0, row=5, columnspan=4, pady=10)

# def bagi():
#     a = float(entry1.get())
#     b = float(entry2.get())
#     hasil = a / b
#     ttk.Label(frm, text=f"Hasil: {hasil}", font=("Arial", 12)).grid(column=0, row=5, columnspan=4, pady=10)

# ttk.Label(frm, text="Angka 1 : ", font=("Arial", 12)).grid(column=0, row=1, pady=10, sticky="w")
# entry1 = ttk.Entry(frm, width=20)
# entry1.grid(column=1, row=1, columnspan=2, pady=10, sticky="w")

# ttk.Label(frm, text="Angka 2 : ", font=("Arial", 12)).grid(column=0, row=2, pady=10, sticky="w")
# entry2 = ttk.Entry(frm, width=20)
# entry2.grid(column=1, row=2, columnspan=2, pady=10, sticky="w")

# ttk.Button(frm, text="+", command=tambah).grid(column=0, row=3, pady=10)
# ttk.Button(frm, text="-", command=kurang).grid(column=1, row=3, pady=10)
# ttk.Button(frm, text="x", command=kali).grid(column=2, row=3, pady=10)
# ttk.Button(frm, text="/", command=bagi).grid(column=3, row=3, pady=10)


# ttk.Label(frm, text="Hasil: ", font=("Arial", 12)).grid(column=0, row=5, columnspan=4, pady=10)
# calculator.mainloop()

# =========================================== Kegiatan 3 ===========================================

from tkinter.simpledialog import askfloat
from tkinter import *
from tkinter import ttk

calculator = Tk()
calculator.title("Calculator Luas Prisma")
frm = ttk.Frame(calculator, padding=20)
frm.grid()

def hitung():
    a = float(entry1.get())
    b = float(entry2.get())
    c = float(entry3.get())
    hasil = (2 * a) + (b * c)
    ttk.Label(frm, text=f"Hasil: {hasil}", font=("Arial", 12, "bold")).grid(column=0, row=5, pady=10)

ttk.Label(frm, text="Kalkulator penghitung luas prisma", font=("Arial", 18, "bold")).grid(column=0, row=0, pady=10, sticky="w")

ttk.Label(frm, text="Luas Alas : ", font=("Arial", 12)).grid(column=0, row=1, pady=10, sticky="w")
entry1 = ttk.Entry(frm, width=20)
entry1.grid(column=1, row=1, columnspan=2, pady=10, sticky="w")

ttk.Label(frm, text="Keliling Alas : ", font=("Arial", 12)).grid(column=0, row=2, pady=10, sticky="w")
entry2 = ttk.Entry(frm, width=20)
entry2.grid(column=1, row=2, columnspan=2, pady=10, sticky="w")

ttk.Label(frm, text="Tinggi Prisma : ", font=("Arial", 12)).grid(column=0, row=3, pady=10, sticky="w")
entry3 = ttk.Entry(frm, width=20)
entry3.grid(column=1, row=3, columnspan=2, pady=10, sticky="w")

ttk.Button(frm, text="Hitung Luas", command=hitung).grid(column=0, row=4, columnspan=2, pady=10)

ttk.Label(frm, text="Hasil: ", font=("Arial", 12, "bold")).grid(column=0, row=5, pady=10)
calculator.mainloop()

# =========================================== Kegiatan 4 ===========================================
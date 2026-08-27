import socket
import platform

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind(("", 50001))
# s.listen(5)
# print("Server siap")
# data = ""
# kamus = {'nama': 'Fahri Sulaiman Wahab',
#          'nim': 'L20025002',
#          'angkatan': '2025',
#          'keluar': 'Siap!'}

# while data.lower() != 'q':
#     komm, addr = s.accept()
#     while data.lower() != 'q':
#         data = komm.recv(1024).decode()
#         if data.lower() == 'q':
#             s.close()
#             break
#         print("Pertanyaan:", data)
#         if data.lower() == 'keluar':
#             komm.send(kamus['keluar'].encode())
#             s.close()
#             break
#         elif data.lower() in kamus:
#             komm.send(kamus[data.lower()].encode())
#         else:
#             komm.send('Maaf, perintah tidak dimengerti'.encode())

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind(("", 50002))
# s.listen(5)
# print("Server siap")
# perintah = ""

# while perintah.lower() != 'q':
#     komm, addr = s.accept()
#     while perintah.lower() != 'q':
#         perintah = komm.recv(1024).decode()
#         if perintah.lower() == 'q':
#             s.close()
#             break
#         print("Command:", perintah)
#         if perintah.lower() == 'machine':
#             jawab = platform.machine()
#             komm.send(jawab.encode())
#         elif perintah.lower() == 'release':
#             jawab = platform.release()
#             komm.send(jawab.encode())
#         elif perintah.lower() == 'system':
#             jawab = platform.system()
#             komm.send(jawab.encode())
#         elif perintah.lower() == 'version':
#             jawab = platform.version()
#             komm.send(jawab.encode())
#         elif perintah.lower() == 'node':
#             jawab = platform.node()
#             komm.send(jawab.encode())
#         elif perintah.lower() == 'quit':
#             komm.close()
#             break
#         else:
#             komm.send('Maaf, perintah tidak dimengerti'.encode())

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind(("", 50003))
# s.listen(5)
# print("Server siap")

# # Variable untuk menyimpan parameter prisma
# parameter = {
#     'panjang': None,
#     'lebar': None,
#     'tinggi': None
# }

# perintah = ""

# while perintah.lower() != 'q':
#     komm, addr = s.accept()
#     print(f"Client terhubung dari {addr}")
    
#     while perintah.lower() != 'q':
#         perintah = komm.recv(1024).decode().strip()
        
#         if perintah.lower() == 'q':
#             s.close()
#             break
        
#         print("Perintah:", perintah)
        
#         # Cek jika input adalah parameter (format: parameter 1 = 10)
#         if "parameter" in perintah.lower() and "=" in perintah:
#             try:
#                 parts = perintah.split("=")
#                 param_num = int(parts[0].split()[-1])
#                 param_value = float(parts[1].strip())
                
#                 if param_num == 1:
#                     parameter['panjang'] = param_value
#                     komm.send("Disimpan (Parameter 1 - Panjang)".encode())
#                 elif param_num == 2:
#                     parameter['lebar'] = param_value
#                     komm.send("Disimpan (Parameter 2 - Lebar)".encode())
#                 elif param_num == 3:
#                     parameter['tinggi'] = param_value
#                     komm.send("Disimpan (Parameter 3 - Tinggi)".encode())
#                 else:
#                     komm.send("Parameter tidak valid (1-3)".encode())
#             except:
#                 komm.send("Format salah. Gunakan: parameter 1 = 10".encode())
        
#         # Hitung luas prisma
#         elif perintah.lower() == 'hitung':
#             if parameter['panjang'] is not None and parameter['lebar'] is not None and parameter['tinggi'] is not None:
#                 # Luas Prisma = 2 × (panjang × lebar) + 2 × (panjang × tinggi) + 2 × (lebar × tinggi)
#                 luas = 2 * (parameter['panjang'] * parameter['lebar']) + \
#                        2 * (parameter['panjang'] * parameter['tinggi']) + \
#                        2 * (parameter['lebar'] * parameter['tinggi'])
                
#                 hasil = f"Luas Prisma = {luas}\nParameter: Panjang={parameter['panjang']}, Lebar={parameter['lebar']}, Tinggi={parameter['tinggi']}"
#                 komm.send(hasil.encode())
#             else:
#                 komm.send("Parameter belum lengkap. Masukkan 3 parameter terlebih dahulu.".encode())
        
#         # Lihat parameter yang tersimpan
#         elif perintah.lower() == 'lihat':
#             info = f"Parameter Tersimpan:\nPanjang: {parameter['panjang']}\nLebar: {parameter['lebar']}\nTinggi: {parameter['tinggi']}"
#             komm.send(info.encode())
        
#         # Reset parameter
#         elif perintah.lower() == 'reset':
#             parameter = {'panjang': None, 'lebar': None, 'tinggi': None}
#             komm.send("Parameter direset".encode())
        
#         elif perintah.lower() == 'q':
#             komm.close()
#             break
#         else:
#             komm.send('Maaf, perintah tidak dimengerti'.encode())
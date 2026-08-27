import socket

hostname = 'localhost'
pesan = ""

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect((hostname, 50001))
# print("Program komunikasi tentang data diri siap")
# while pesan.lower() != 'q':
#     pesan = input("Pertanyaan : ")
#     s.send(pesan.encode())
#     response = s.recv(1024).decode()
#     print("Jawaban :", response)
#     if pesan.lower() == 'keluar':
#         s.close()
#         break
# s.close()

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect((hostname, 50002))
# print("Program komunikasi tentang server siap")
# while pesan.lower() != 'q':
#     pesan = input("Command : ")
#     s.send(pesan.encode())
#     response = s.recv(1024).decode()
#     if pesan.lower() == 'quit':
#         s.close()
#         break
#     print("Response :", response)
# s.close()

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect((hostname, 50003))
# print("Program komunikasi untuk menghitung luas prisma siap")
# print("Masukkan 3 parameter: parameter 1 = nilai, parameter 2 = nilai, parameter 3 = nilai")
# print("Kemudian ketik 'hitung' untuk menghitung luas prisma")
# print("Ketik 'q' untuk keluar\n")

# while pesan.lower() != 'q':
#     pesan = input("Input : ")
#     s.send(pesan.encode())
#     response = s.recv(1024).decode()
    
#     if pesan.lower() == 'q':
#         s.close()
#         break
    
#     print("Response :", response)
#     print()

# s.close()
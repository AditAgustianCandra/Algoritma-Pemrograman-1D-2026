baris = int(input("Masukkan jumlah baris: "))
jumlah = int(input("Masukkan jumlah lampu: "))

for i in range(1, baris + 1):
    print(f"Baris ke-{i}")
    for j in range(1, jumlah + 1):
        if j % 3 == 0:
            print(f"Lampu {j}: mengalami gangguan")
        else:
            print(f"Lampu {j}: berfungsi normal")

print("Periksa sumber listrik utama taman")
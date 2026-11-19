inventaris = []
jumlah = int(input("Masukkan jumlah PC: "))

for i in range(jumlah):
    nama = input("Nama PC: ")
    status = input("Status (Normal/Rusak): ")
    ram = input("Kapasitas RAM (GB): ")
    inventaris.append([nama, status, ram])

def cek_kelayakan(status, ram):
    ram = int(ram)
    if status == "Normal" and ram >= 8:
        return "Layak"
    else:
        return "Tidak Layak"

print("Hasil evaluasi:")
for i in range(len(inventaris)):
    try:
        hasil = cek_kelayakan(inventaris[i][1], inventaris[i][2])
    except ValueError:
        hasil = "Format RAM Kacau"
    print('{ "PC": "', inventaris[i][0], '", "Status": "', hasil, '" }')
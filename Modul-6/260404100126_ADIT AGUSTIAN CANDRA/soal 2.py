sementara = []
while True:
    nama = input("Masukkan nama asisten: ")
    if nama == "cukup":
        break
    sementara.append(nama)
asisten_awal = tuple(sementara)   

tambahan = input("Masukkan nama asisten tambahan: ")
asisten_akhir = asisten_awal + (tambahan,)

sementara = []
while True:
    hari = input("Masukkan hari tugas: ")
    if hari == "cukup":
        break
    sementara.append(hari)
hari_tugas = tuple(sementara)

asisten_libur = input("Masukkan nama asisten pengecualian: ")
hari_libur = input("Masukkan hari pengecualian: ")

print("Jadwal shift:")
for asisten in asisten_akhir:
    for hari in hari_tugas:
        if asisten == asisten_libur and hari == hari_libur:
            continue
        print(asisten, "-", hari)

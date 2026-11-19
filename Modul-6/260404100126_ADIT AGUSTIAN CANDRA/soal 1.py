anggota = []

while True:
    nama = input("Masukkan nama calon anggota: ")
    if nama == "selesai":
        break
    anggota.append(nama)

print("Hasil pemeriksaan:")
for nama in anggota:
    if nama == "admin" or len(nama) < 4:
        print(nama, ": nama tidak valid")
    else:
        print(nama, ": nama valid")

penyusup = input("Masukkan nama penyusup yang ingin dihapus: ")
if penyusup in anggota:
    anggota.remove(penyusup)
    print(penyusup, "berhasil dihapus")
else:
    print(penyusup, "tidak ada di daftar pendaftaran")

print("Daftar anggota sekarang:", anggota)
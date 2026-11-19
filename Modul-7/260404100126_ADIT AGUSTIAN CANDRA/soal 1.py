tugas = {}

while True:
    print("1. Tambah  2. Tampilkan  3. Selesai  4. Hapus  5. Jumlah  6. Keluar")
    pilih = input("Pilih menu: ")

    if pilih == "1":
        nama_tugas = input("Nama tugas: ")
        tugas[nama_tugas] = "Belum selesai"

    elif pilih == "2":
        for nama_tugas in tugas:
            print(nama_tugas, "-", tugas[nama_tugas])

    elif pilih == "3":
        nama_tugas = input("Nama tugas: ")
        if nama_tugas in tugas:
            tugas[nama_tugas] = "Selesai"
        else:
            print("Tugas tidak ditemukan")

    elif pilih == "4":
        nama_tugas = input("Nama tugas: ")
        try:
            del tugas[nama_tugas]
        except KeyError:
            print("Tugas tidak ditemukan")

    elif pilih == "5":
        selesai = 0
        for nama_tugas in tugas:
            if tugas[nama_tugas] == "Selesai":
                selesai = selesai + 1
        belum = len(tugas) - selesai
        print("Tugas selesai       :", selesai)
        print("Tugas belum selesai :", belum)

    elif pilih == "6":
        break
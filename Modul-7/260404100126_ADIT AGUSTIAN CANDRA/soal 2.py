playlist = {}

while True:
    print("1. Buat playlist  2. Tambah lagu  3. Tampilkan  4. Cari lagu ")
    print("5. Hapus lagu  6. Hapus playlist  7. Keluar")
    pilih = input("Pilih menu: ")

    if pilih == "1":
        nama_playlist = input("Nama playlist: ")
        playlist[nama_playlist] = {}

    elif pilih == "2":
        nama_playlist = input("Nama playlist: ")
        judul_lagu = input("Judul lagu: ")
        penyanyi = input("Penyanyi: ")
        if nama_playlist in playlist:
            playlist[nama_playlist][judul_lagu] = penyanyi
        else:
            print("Playlist tidak ditemukan")

    elif pilih == "3":
        for nama_playlist in playlist:
            print(nama_playlist)
            for judul_lagu in playlist[nama_playlist]:
                print("  ", judul_lagu, "-", playlist[nama_playlist][judul_lagu])

    elif pilih == "4":
        cari = input("Judul lagu: ")
        for nama_playlist in playlist:
            if cari in playlist[nama_playlist]:
                print(cari, "ada di playlist", nama_playlist)

    elif pilih == "5":
        nama_playlist = input("Nama playlist: ")
        judul_lagu = input("Judul lagu: ")
        try:
            del playlist[nama_playlist][judul_lagu]
        except KeyError:
            print("Playlist atau lagu tidak ditemukan")

    elif pilih == "6":
        nama_playlist = input("Nama playlist: ")
        try:
            del playlist[nama_playlist]
        except KeyError:
            print("Playlist tidak ditemukan")

    elif pilih == "7":
        break
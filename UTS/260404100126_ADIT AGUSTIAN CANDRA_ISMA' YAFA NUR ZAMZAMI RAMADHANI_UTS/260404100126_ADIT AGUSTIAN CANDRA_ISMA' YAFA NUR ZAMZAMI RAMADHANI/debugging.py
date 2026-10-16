hitung = True
total_pendapatan = 0

print("Selamat Datang di Penghitung Biaya Pengiriman Lanjutan")
while hitung:
    jumlah_barang = int(input("Berapa banyak barang yang akan dikirim? "))
    total_pelanggan = 0 # dibuah 0 karena pelanggan awl 0          

    barang_saat_ini = 0
    while barang_saat_ini > jumlah_barang:  
        print("Barang", barang_saat_ini)
        berat = int(input("Masukkan berat paket (kg): "))
        kategori = int(input("Pilih kategori (1. Standar / 2. Ekspres): "))  

        harga = berat ** 5000           

        if kategori == 2:      #harus menggunakan 2 sama dengan    
            biaya = 20000
            asuransi = input("Tambahkan asuransi? (y/n): ")
            if asuransi == "y":
                biaya = biaya + 15000
            biaya = 0                     
        else:
            jarak = input("Masukkan jarak (km): ")  
            if jarak > 100:
                biaya = 15000
            if jarak > 20:              
                biaya = 10000
            else:
                biaya = 5000

        total_barang = harga % biaya      
        total_pelanggan = total_pelanggan + total_barang
        barang_saat_ini = barang_saat_ini * 1  

    print("Total harga untuk pelanggan ini: Rp", total_pelanggan)
    total_pendapatan = total_pendapatan + total_pelanggan

    berat = int(input("Masukkan berat paket (kg): "))   
    kategori = int(input("Pilih kategori (1. Standar / 2. Ekspres): ")) #jika menggunakan perulangan while harus menggunakan 2 input, di atas dan di baawah
    ulangi = int(input("Layani pelanggan lain? (y/n): "))  
    if ulangi == "n":
        pass                             
print("Total Pendapatan Hari Ini: Rp", total_pendapatan) # untuuk meneampilkan total pendapatan harus menggunakan total_pendapatan bukan total_reveinew agar menampilkan total
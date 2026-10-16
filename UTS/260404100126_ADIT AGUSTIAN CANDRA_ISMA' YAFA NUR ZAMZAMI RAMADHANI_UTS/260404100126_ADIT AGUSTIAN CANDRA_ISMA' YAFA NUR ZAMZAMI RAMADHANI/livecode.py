jumlah_tiket_dibeli = 0

uang = int(input("masukkan uang pembayaran")) #ini untuk memasukan uang
member = (input("ya/tidak"))

while uang:     # pakai while karena jumlah perulangan belum diketahui
    if uang == 40000:
        print("Reguler")
    elif uang == 75000:     #ini untuk mengkategorikan pesanan
        print("VIP, mendapatkan minum gratis")
    elif uang == 100000:
        print("VVIP, mendapat minum gratis")

if 40000:
    print ("apakah anda ingin tambah minuman seharga 10.000") # ini umtuk menawarkan  
    input("ya/tidak")

jumlah_tiket_dibeli = jumlah_tiket_dibeli + 1   #ini untuk mencari jika tiket dibeli lebi dari 3 akan mendapat diskon

if jumlah_tiket_dibeli % 3:

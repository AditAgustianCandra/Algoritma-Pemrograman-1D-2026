total = int(input("Masukkan total belanja: "))

if total % 100000 == 0:
    bayar = 0
    print("Selamat, belanjaan gratis!")
elif total % 50000 == 0:
    bayar = total - total * 0.50
    print("Diskon 50%")
elif total % 10000 == 0:
    bayar = total - total * 0.20
    print("Diskon 20%")
elif total >= 200000:
    bayar = total - total * 0.10
    print("Diskon 10%")
else:
    bayar = total
    print("Tidak ada diskon")
print("Total belanja awal =", total)
print("Total yang harus dibayar =", bayar)


poin = "Poin Bertambah" if bayar > 0 else "Tidak Ada Poin"
print("Status poin:", poin)
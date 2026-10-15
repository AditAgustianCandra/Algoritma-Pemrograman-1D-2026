jumlah = 0
total_pendapatan = 0
total_jarak = 0
jarak_terjauh = 0

jarak = int(input("Masukkan jarak : "))

while jarak != 0:
    if jarak < 0:
        print("Jarak negatif tidak valid")
    else:
        jumlah = jumlah + 1
        total_jarak = total_jarak + jarak

        if jarak > jarak_terjauh:
            jarak_terjauh = jarak

        if jarak <= 5:
            tarif = 3000
        elif jarak <= 15:
            tarif = 3000 + (jarak - 5) * 1000
        else:
            tarif = 13000 + (jarak - 15) * 500

        if jumlah % 5 == 0:
            tarif = tarif / 2
            print("Penumpang ke-", jumlah, "dapat diskon 50%")

        print("Tarif: Rp", tarif)
        total_pendapatan = total_pendapatan + tarif

    jarak = int(input("Masukkan jarak:"))

if jumlah > 0:
    rata_rata = total_jarak / jumlah
else:
    rata_rata = 0

print("Jumlah penumpang :", jumlah)
print("Total pendapatan : Rp", total_pendapatan)
print("Jarak terjauh    :", jarak_terjauh, "km")
print("Rata-rata jarak  :", rata_rata, "km")
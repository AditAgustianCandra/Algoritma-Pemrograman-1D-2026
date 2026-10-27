total_gaji = 0

for hari in range(1, 8):
    print(f"Hari ke-{hari}")
    gaji_harian = 100000

    lembur = int(input("Jam lembur: "))

    while lembur > 8 or lembur < 1:
        print("Jumlah lembur tidak sesuai, upah tidak dihitung. Input ulang.")
        lembur = int(input("Jam lembur: "))

    if 1 <= lembur <= 3:
        gaji_harian = gaji_harian + lembur * 25000
    elif lembur <= 4:
        gaji_harian = gaji_harian + 100000
    elif lembur <= 6:
        gaji_harian = gaji_harian + 200000
    elif lembur <= 8:
        gaji_harian = gaji_harian + 300000

    shift = input("Shift malam? (y/t): ")
    while True:
        if shift == "y":
            gaji_harian = gaji_harian + 50000
            print(gaji_harian)
            break
        elif shift == "t":
            continue
        else:
            shift = input("Shift malam? (y/t): ")
    

    print(f"Gaji hari ke-{hari}: Rp{gaji_harian:,}")
    total_gaji = total_gaji + gaji_harian

print(f"Total gaji seminggu: Rp{total_gaji:,}")
nama = input("Masukkan nama mahasiswa : ")
tugas = float(input("Masukkan nilai tugas   : "))
uts = float(input("Masukkan nilai UTS     : "))
uas = float(input("Masukkan nilai UAS     : "))

def hitung_nilai(tugas, uts, uas):
    akhir = (tugas * 0.3) + (uts * 0.3) + (uas * 0.4)

    if akhir >= 85:
        grade = "A"
    elif akhir >= 70:
        grade = "B"
    elif akhir >= 55:
        grade = "C"
    else:
        grade = "D"

    if grade == "D":
        ket = "Tidak Lulus"
    else:
        ket = "Lulus"

    print("Nama        :", nama)
    print("Nilai Tugas :", tugas)
    print("Nilai UTS   :", uts)
    print("Nilai UAS   :", uas)
    print("Nilai Akhir :", akhir)
    print("Grade       :", grade)
    print("Keterangan  :", ket)

hitung_nilai(tugas, uts, uas)
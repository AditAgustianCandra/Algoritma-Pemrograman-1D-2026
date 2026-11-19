undangan = set()
webinar_a = set()
webinar_b = set()

print("Isi daftar undangan (ketik selesai jika sudah)")
while True:
    nama = input("Nama: ")
    if nama == "selesai":
        break
    undangan.add(nama)

print("Isi peserta Webinar A (ketik selesai jika sudah)")
while True:
    nama = input("Nama: ")
    if nama == "selesai":
        break
    webinar_a.add(nama)

print("Isi peserta Webinar B (ketik selesai jika sudah)")
while True:
    nama = input("Nama: ")
    if nama == "selesai":
        break
    webinar_b.add(nama)

print("Semua peserta       :", webinar_a.union(webinar_b))
print("Hadir di keduanya   :", webinar_a.intersection(webinar_b))
print("Hanya salah satu    :", webinar_a.symmetric_difference(webinar_b))
print("Undangan tidak hadir:", undangan.difference(webinar_a.union(webinar_b)))
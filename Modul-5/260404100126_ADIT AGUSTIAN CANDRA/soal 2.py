kata = input("Masukkan kata : ")

def palindrom(kata):
    terbalik = ""
    for huruf in kata:
        terbalik = huruf + terbalik
    return kata == terbalik

if palindrom(kata):
    print(f"Kata {kata} adalah palindrom")
else:
    print(f"Kata {kata} bukan palindrom")
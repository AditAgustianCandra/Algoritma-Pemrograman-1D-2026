n = int(input("Masukkan tinggi (2-15): "))

while n < 2 or n > 15:
    print("Tinggi harus 2 sampai 15, ulangi")
    n = int(input("Masukkan tinggi (2-15): "))

for i in range(1, 2 * n):
    if i <= n:
        baris = i
    else:
        baris = 2 * n - i

    print(" " * (n - baris), end="")

    for j in range(1, baris + 1):
        print(j % 10, end= "")

    for j in range(baris - 1, 0, -1):
        print(j % 10,end = "")

    print()
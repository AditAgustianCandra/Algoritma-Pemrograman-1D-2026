n = int(input("Masukkan hari ke-N : "))

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

if n < 1:
    print("N harus bilangan bulat positif")
else:
    print(f"Jumlah pelanggan hari ke-{n} = {fibonacci(n)} orang")
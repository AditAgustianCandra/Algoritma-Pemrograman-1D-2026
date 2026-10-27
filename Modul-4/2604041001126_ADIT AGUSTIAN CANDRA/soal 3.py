n = int(input("Masukkan bilangan bulat: "))

for i in range(1, n + 1):
    for j in range(n - i):
        print(' ', end=' ')

    for k in range(1, i + 1):
        print(k, end=' ')

    for s in range(1):
        print(' ', end=' ')

    for k in range(i, 0, -1):
        print(k, end=' ')

    print()
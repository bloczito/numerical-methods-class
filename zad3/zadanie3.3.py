import numpy


def findFirst(arr):
    # pierwsze y1, potem y2,3, itd.
    prev_y = numpy.array([1, 0, 0, 0, 0, 0])

    while True:
        zk = product(arr, prev_y)

        norm = numpy.linalg.norm(zk)
        next_y = [zk[i] / norm for i in range(0, len(zk))]

        # warunek zakonczenia
        if abs(abs(prev_y[0]) - abs(next_y[0])) < 1e-8:
            print(f"Znaleziony wektor wlasny: {next_y}")
            print(f"Znaleziona wartosc wlasna: {norm}")
            return next_y
        prev_y = next_y


def findSecond(arr, e1):
    # pierwsze y1, potem y2,3, itd.
    prev_y = numpy.array([1, 0, 0, 0, 0, 0])

    while True:
        zk = product(arr, prev_y)
        # ortogonalizacja
        zk = ortho(zk, e1)
        norm = numpy.linalg.norm(zk)
        next_y = [zk[i] / norm for i in range(0, len(zk))]
        # warunek zakonczenia
        if abs(abs(prev_y[0]) - abs(next_y[0])) < 1e-13:
            print(f"Znaleziony wektor wlasny: {next_y}")
            print(f"Znaleziona wartosc wlasna: {norm}")
            return next_y
        prev_y = next_y


# mnozy macierz a razy wektor x i zwraca wektor wynikowy y
def product(a, x):
    y = []
    for i in range(0, 6):
        summ = 0
        for j in range(0, 6):
            summ = summ + a[i][j] * x[j]
        y.append(summ)
    return y


# dokonuje ortogonalizacji wektora zk
def ortho(zk, e):
    prod = 0
    for i in range(0, len(zk)):
        prod = prod + zk[i] * e[i]

    for i in range(0, len(zk)):
        zk[i] = zk[i] - e[i] * prod
    return zk


if __name__ == "__main__":
    print("Szukanie dwoch najwiekszych na modul wartosci wlasnych macierzy")
    arr = numpy.array([
        [19 / 12, 13 / 12, 5 / 6, 5 / 6, 13 / 12, -17 / 12],
        [13 / 12, 13 / 12, 5 / 6, 5 / 6, -11 / 12, 13 / 12],
        [5 / 6, 5 / 6, 5 / 6, -1 / 6, 5 / 6, 5 / 6],
        [5 / 6, 5 / 6, -1 / 6, 5 / 6, 5 / 6, 5 / 6],
        [13 / 12, -11 / 12, 5 / 6, 5 / 6, 13 / 12, 13 / 12],
        [-17 / 12, 13 / 12, 5 / 6, 5 / 6, 13 / 12, 19 / 12]
    ])

    # szuka pierwszej wartosci wlasnej
    e1 = findFirst(arr)
    print()

    # szuka drugiej wartosci wlasnej
    e2 = findSecond(arr, e1)

    print()
    print("Sprawdzenie wyników z wartosciami wlasnymi znalezionymi przez funkcję z biblioteki numpy")
    yee = numpy.linalg.eig(arr)
    print(f"Znalezione wartosci wlasne z funkcji numpy.linalg.eig(): {yee[0]}")

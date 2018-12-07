A = input("Podaj dzielną:")
A = int(A)
B = input("Podaj dzielnik:")
B = int(B)
while B == 0:
    print("Nie dziel przez 0")
    B = input("Podaj dzielnik jeszcze raz:")
    B = int(B)
if B != 0:
    print("Wynik:")
    print(int(A/B))
    print("Reszta:")
    print(A%B)

#Program dzielacy dwie liczby przez siebie w wyniku podaje ilosc, i reszte z dzielenia
a= float(input("a:"))
b= float(input("b:"))
while b==0:
    print("!!!bug!!!")
    b= float(input("b:"))
if b!=0:
    reszta=a%b
    wynik=(a-reszta)/b
    print("zniwo to:",wynik, "i",reszta, "odpadek to:",reszta)

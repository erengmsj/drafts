print("""*********************************

Faktöriyel Bulma Programı

Çıkmak İçin 'q' ya Basın.

*********************************
""")

while True:
    sayı = input("Sayı:")
    if (sayı == "q"):
        print("Program Sonlandırılıyor..")
        break

    else:
        sayı = int(sayı)

        factorial = 1

        for i in range(2,sayı+1):
            factorial *= i
        print("Faktöriyel",factorial)
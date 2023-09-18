print("""************************************************* 
ATM Machine 

İşlemler;

1. Bakiye Sorgulama 

2. Para Yatırma

3. Para Çekme

Programdan Çıkmak İçin 'q' ya Basın.
************************************************* 
    
""")

bakiye = 1000

while True:
    işlem = input("İşlemi seçiniz:")

    if (işlem == "q"):
        print("Yine Bekleriz..")
        break

    elif (işlem == "1"):
        print("Bakiyeniz {} tl dir.".format(bakiye))

    elif (işlem == "2"):
        miktar = int(input("Yatıracağınız Miktarı Giriniz:"))
        bakiye += miktar

    elif (işlem == "3"):
        miktar = int(input("Çekmek İstediğiniz Miktarı Giriniz:"))

        if (bakiye - miktar < 0 ):
            print("Böyle Bir Miktar Çekemezsiniz..")
            continue
        bakiye -= miktar



    else:
        print("Geçirsiz İşlem..")



























sayı1=int(input("başlangıc giriniz"))
sayı2=int(input("bitişi giriniz"))


num=range(sayı1,sayı2)
toplam=0
for numm in num :
    toplam += numm
    print(toplam)
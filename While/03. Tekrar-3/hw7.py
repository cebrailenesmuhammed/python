sayı1 = int(input("Birinci sayıyı girin: "))
sayı2 = int(input("İkinci sayıyı girin: "))

toplam=0
sayac=0
sayı =sayı1
while sayı <= sayı2:
  
 toplam += sayı

 sayac += 1

sayı += 1

ortalama = toplam / sayac

print(f"{sayı1} ile {sayı2} arasındaki sayıların ortalaması: {ortalama}")
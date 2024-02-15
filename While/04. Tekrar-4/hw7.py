sayi1 = int(input("Birinci sayıyı girin: "))
sayi2 = int(input("İkinci sayıyı girin: "))


toplam = 0
sayac = 0
sayi = sayi1
while sayi <= sayi2:
  
 toplam += sayi

 sayac += 1

sayi += 1

ortalama = toplam / sayac

print(f"{sayi1} ile {sayi2} arasındaki sayıların ortalaması: {ortalama}")





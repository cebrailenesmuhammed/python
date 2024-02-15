sayı1=int(input("Başlangıç Değerini Girin : "))
sayı2=int(input("bitiş değerin girin"))



toplam=0
sayı= (sayı1,sayı2+1)
toplam+=sayı


ortalama = toplam / (sayı2-sayı1 + 1)
print("Sayıların Ortalaması: {}"+ortalama)
toplam= 0
sayac= 0
sayı =  int (input("bir sayı girin lütfen"))
while sayi != 1:
    toplam += sayi
    sayac += 1
    sayi = int(input("Bir sayı daha girin (1 girerseniz durur): "))
ortalama = toplam / sayac if sayac != 0 else 0
print("Ortalama: ", ortalama)
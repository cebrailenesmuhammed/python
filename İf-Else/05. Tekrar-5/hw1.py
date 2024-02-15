import math

sınav1 =  float(input("1. notunuzu girin\n : "))
sınav2 =  float(input("2. notunuzu girin\n : "))
perfonmas =  float(input("perfonmas notunuzu girin\n : "))

toplam = (int(sınav1) +   int(sınav2) +  int(perfonmas))

Ortalama= ( toplam / 3)

if (Ortalama > 50) :
    print("Başarılı")
elif (Ortalama < 50) :   
    print("Başarısız")

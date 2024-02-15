import math

birinci_sınav_notu=("lütfen sınav notunuzun 1 olan")
ikinci_sınav_notu=("lütfen sınav notunuzu 2 olan")
perfonmas_notu   = ("perfonmas noatu")

toplam = (int(birinci_sınav_notu) +  int(ikinci_sınav_notu) +   int(perfonmas_notu))
ortalama= (toplam/3)


if (ortalama > 50) :
    print("Başarılı")
elif (ortalama < 50) :   
    print("Başarısız")
  
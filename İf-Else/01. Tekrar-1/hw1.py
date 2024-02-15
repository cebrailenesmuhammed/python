import math

birinci_sınav_notu= float(input("birinci sınav notu giriniz"))
ikinci_sınav_notu=float (input("ikinci sınav notu giriniz"))
performans_notu=float (input("ikinci sınav notu giriniz"))

toplam = (int(birinci_sınav_notu) + int(ikinci_sınav_notu) +  int(performans_notu)) 
Ortalama =( toplam / 3)

if (Ortalama > 50) :
    print("Başarılı")
elif (Ortalama < 50) :   
    print("Başarısız")  



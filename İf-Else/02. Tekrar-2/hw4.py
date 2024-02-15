ürün1_fiyatı= int(input("ürün1 fiyat gir"))
ürün2_fiyatı= int(input("ürün2 fiyat gir"))


toplam= ürün1_fiyatı + ürün2_fiyatı

if toplam <= 200 :
    print ("ücret:",toplam)

elif toplam > 200:
     print ("ücret:", toplam/4)    

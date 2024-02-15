ürün1=int(input("1ürün fiyat"))
ürün2=int(input("2ürün fiyat"))

toplam = ürün1+ürün2

if toplam<=200:
   print("Ücret: ",toplam)

elif toplam > 200:
    print("Ücret: ",toplam/4)

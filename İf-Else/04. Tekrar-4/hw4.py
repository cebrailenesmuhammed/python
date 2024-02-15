ürün1 = int (input("1 ürün fiyatınızı girin \n"))
ürün2 = int (input("2 ürün fiyatınızı girin \n"))

toplam = ürün1 +  ürün2


if toplam <= 200:
    print("Ücret: ",toplam)

elif toplam > 200:
  print ("ücret:",toplam/4)
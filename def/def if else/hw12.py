
size  = float(input("boyunuz\n : "))
weight = float(input("kilonuz\n : "))
vki = weight / (size * size)
   


def weak (vki):
    if vki < 18:
        print ("zayıf")
    elif vki < 25 :
      print("normal") 
    elif vki < 30:
        print("Kilolu")
    elif vki < 35:
        print("Obez")
    else:
        print("Ciddi obez")



weak (vki)
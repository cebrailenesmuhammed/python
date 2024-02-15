boy  = float(input("boyunuz\n : "))
ağırlık = float(input("kilonuz\n : "))
vki = ağırlık / (boy * boy)


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

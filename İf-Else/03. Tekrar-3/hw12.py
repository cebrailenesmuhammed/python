boy= float(input("boyunuz\n : "))
agarlık= float(input("kilonuz\n : "))
vki= agarlık /  (boy*boy)


if vki < 18:
    print("Zayıf")
elif vki < 25:
    print("normal")
elif vki < 30:
    print("kilolu")    
if vki < 35:
    print("obez") 
else:
     print("ciddi obez")          

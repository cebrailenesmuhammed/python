k1=float (input("1kenarı girin"))
k2=float (input("2kenarı girin"))
k3=float (input("3kenarı girin"))

if k1==k2==k3:
    print("eşkenar")  

elif k1==k2 or k1==k3 or k2==k3 :
    print("ikizkenar")    
else :
    ("çeşitkenar")
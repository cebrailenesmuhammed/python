kenar1= float (input ( "1kenar" ))
kenar2= float (input ( "2kenar" ))
kenar3= float (input ( "3kenar" ))

if kenar1 == kenar2 == kenar3:
    print("Eşkenar")
elif kenar1 == kenar2 or kenar1 == kenar3 or kenar2 == kenar3:
    print("İkizkenar")
else:
    print("Çeşitkenar")
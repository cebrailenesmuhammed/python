bagaj=float (input("bagajın ağırlınızı girin"))
if bagaj <= 20:
     print("Herhangi bir ücret ödemeniz gerekmiyor.")
 

else:
     ek_üçret= int (bagaj-20) * 10
     print("Fazla bagaj için {ek_ucret} TL ödemelisiniz.")
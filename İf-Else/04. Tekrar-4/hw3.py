bagaj=float (input("bagajın ağırlınız girin"))

if bagaj <= 20 :
    print ("herhangi bi ğçret ödeme")
else:
     ücret = int (bagaj -20)  *   10
     print ("fazla bagaj icin {ücret}tl ödememesiniz")

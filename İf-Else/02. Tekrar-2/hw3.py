bagaj=float (input("bağaj girin:"))
if bagaj <= 20:
    print ("üçret ödeme")
else: 
    ek_ücret = int(bagaj-20)  * 10
    print ("fazla bagaj icin {ek_ücret} ödemelisiniz")  
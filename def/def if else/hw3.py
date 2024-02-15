def getbaggage():
    baggage = float(input("Bagaj ağırlığını giriniz: "))
    return int(baggage)

def baggage_calculation(baggage):
    if baggage <= 20:
        return 0
    return baggage - 20

def baggage_crash (additional_baggage):
    return additional_baggage * 10

baggage = getbaggage()


additional_baggage =  baggage_calculation (baggage) 
if additional_baggage > 0:
    payment = baggage_crash(additional_baggage)
    print("fazla bagaj için ", payment, "TL kadar ödeme yapmanız gerekiyor")
else:
    print("Herhangi bir ücret ödemeniz gerekmiyor")


bagggg = getbaggage()
baggage_calculation(bagggg)
baggage_crash()
    
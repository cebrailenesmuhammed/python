ad = "enes"  
maas = 3000000000  
calisma_yili = 10 

if calisma_yili <= 5:
    zamli_maas = maas * 1.10
elif calisma_yili <= 10:
    zamli_maas = maas * 1.15
else:
    zamli_maas = maas * 1.25

print(f"Sayın {ad}, zamlı maaşınız {zamli_maas} TL")


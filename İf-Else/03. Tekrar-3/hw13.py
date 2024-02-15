ad="yavuz"
maaş= 1 
çalış= 6

if çalış <= 5:
    zamlı=maaş * 1.10
elif çalış <= 10:   
     zamli_maas = maaş * 1.15
else:
    zamli_maas = maaş * 1.25

print(f"Sayın {ad}, zamlı maaşınız {zamli_maas} TL")
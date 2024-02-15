ad = "ali"
maas=3000
yılı=6


if yılı <= 5:
    zamlı_maaş = maas * 1.10
elif yılı <= 10:
        zamli_maas = maas * 1.15
else:
    zamli_maas = maas * 1.25

print(f"Sayın {ad}, zamlı maaşınız {zamli_maas} TL")    
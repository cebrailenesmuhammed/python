sayilar = [35, 26, 81, 64]


sayilar.sort(reverse=True)
print(sayilar)


sayilar.reverse()
print(sayilar)


print(sayilar.count(26))


sayilar.remove(81)
print(sayilar)


sayilar.clear()
print(sayilar)

print(sayilar.index(64))


ondalikli_sayilar = [1.4, 6.8]
birlesik_liste = sayilar + ondalikli_sayilar
print(birlesik_liste)

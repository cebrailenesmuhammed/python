sayılar= [35,26,81,64]


sayılar.sort(reverse=True)
print(sayılar) 


sayılar.reverse()
print(sayılar)


sayı = sayılar.count(26)
print(sayı) 

sayılar.remove(81)
print(sayılar) 


sayılar.clear()
print(sayılar) 


indeks = sayılar.index(64)
print(indeks) 


ondalıklı_sayılar = [1.4, 6.8]
sayılar.extend(ondalıklı_sayılar)
print(sayılar) 

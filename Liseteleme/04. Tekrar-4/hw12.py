onemli_telefonlar = {"Acil Çağrı Merkezi":"112", "Polis İmdat":"155", "Milli Eğitim Bakanlığı İletişim Merkezi":"444 0 632"}
deger = onemli_telefonlar.pop("Acil Çağrı Merkezi")
print(deger) 
print(onemli_telefonlar)
onemli_telefonlar = {"Acil Çağrı Merkezi":"112", "Polis İmdat":"155", "Milli Eğitim Bakanlığı İletişim Merkezi":"444 0 632"}
anahtar_deger = onemli_telefonlar.popitem()
print(anahtar_deger) 
print(onemli_telefonlar) 



onemli_telefonlar = {"Acil Çağrı Merkezi":"112", "Polis İmdat":"155", "Milli Eğitim Bakanlığı İletişim Merkezi":"444 0 632"}
onemli_telefonlar.clear()
print(onemli_telefonlar)


sozluk = {"Bilim insanı": "Aziz Sancar", "Şair": "Mehmet Akif Ersoy", "Astronom": "Ali Kuşçu"}

meslekler = sozluk.copy()
print(meslekler)


print(sozluk.values())


sozluk.clear()
print(sozluk)


sozluk["Matematikçi"] = "Cahit Arf"
print(sozluk)


if "Sanatçı" in sozluk:
    print("Sanatçı anahtarı var.")
else:
    print("Sanatçı anahtarı yok.")


sozluk["Bilim insanı"] = "Canan Dağdeviren"
print(sozluk)


print(sozluk["Şair"])


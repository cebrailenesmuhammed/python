işlemci = "i7"
ram = "8"

mesaj = "Kurulum uygun" if işlemci == 'i7' or ram >= 8 else "Kurulum uygun değil"
print(mesaj)
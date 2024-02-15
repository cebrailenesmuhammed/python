islemci = 'i5'
ram = 8


def steam (processor,ram,message):
    message = "Kurulum uygun" if processor == 'i7' or ram >= 8 else "Kurulum uygun değil"
    print(message)


steam(islemci,ram)    
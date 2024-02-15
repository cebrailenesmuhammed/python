import random
sayı = random.randint(0,20)

print("0 ile 20 arasında bir sayı tahmin ediniz.")


while True :
    tahmin =  int(input("Tahmininiz: "))


    if tahmin == sayı :
       print("Tebrikler, doğru tahmin ettiniz!")
    break
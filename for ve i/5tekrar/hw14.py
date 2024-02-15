
import random


sayi = random.randint(0, 20)


print("0 ile 20 arasında bir sayı tahmin ediniz.")


while True:
   
    tahmin = int(input("Tahmininiz: "))

    
    if tahmin == sayi:
        print("Tebrikler, doğru tahmin ettiniz!")
        break
 
    elif tahmin > sayi:
        print("Tahmininiz çok büyük, azaltın.")
 
    else:
        print("Tahmininiz çok küçük, arttırın.")
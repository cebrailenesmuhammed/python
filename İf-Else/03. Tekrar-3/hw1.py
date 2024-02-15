import math 
s1= float  (input ("s1 giriniz"))
s2= float  (input ("s2 giriniz"))
p= float  (input ("p giriniz"))

t= ( int(s1) + int(s2) + int(p))
o=( t / 3)
if (o > 50) :
    print("Başarılı")
elif (o < 50) :   
    print("Başarısız")
  
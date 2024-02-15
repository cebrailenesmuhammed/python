getuser = input ("kullanıncı adınızı giriniz")
getpassword= input   ("şifrenizi girebilirmisiniz")

def save (user, password):
    if user == "türkiye" and password == 1923 :
        print("Giriş başarılı")
    else:
        print("Kullanıcı adı ya da şifre yanlış")
          

save(getuser,getpassword )


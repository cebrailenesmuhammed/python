def heat0 (): 
    heat=float(input("sıcaklık \n : "))
    return heat







def heta_get (heat1):
    if heat1 <= 5 :
        print ("soğuk")
    elif 6  <= heat1 <= 14 :
        print("Ilık")
    else:
        print("Sıcak")    



heat = heat0 ()
heta_get(heat)        
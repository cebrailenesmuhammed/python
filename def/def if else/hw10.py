def time0 ():
    time =float(input("saat\n : "))
    return time

def time1 (fee,time2):
    if time2 <= 1:
     fee = 5
    elif 1 < time2 <= 5:
        fee = time2 * 4
    else:
        fee = time2 * 3
    print(f"Ödenecek miktar: {fee} TL")
    return fee ,time2
      
fee = 0
time = time0 ()
time1(fee, time)   
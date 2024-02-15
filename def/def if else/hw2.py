def angle (a):
    angle = float(input(a + ". açı girin\n : "))
    return angle

angle01 = angle("1")
angle02 = angle("2")
angle03 = angle ("3")
 

def average_angle (angle1, angle2, angle3):
 total = ( int(angle1) + int(angle2) + int(angle3) )
 if (total == 180) :
    print(" üçgen")
 else:
    print("bu bir üçgen değildir")







average_angle (angle01, angle02, angle03)


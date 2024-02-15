def get_notes_performance():
    return float(input("Pefromans Notu Girin \n"))

def get_notes_exam1():
    return float(input("Birinci Sınav Notu Girin \n"))

def get_notes_exam2():
    return float(input("İkinci Sınav Notu Girin \n"))

def calculate_average(Pefromance, Exam1, Exam2):
    Average = Pefromance + Exam1 + Exam2 / 3
    return Average

def check_success(Average):
    if Average >= 50:
        return "Başarılı"
    return "Başarısız"


performance = get_notes_performance()
exam1 = get_notes_exam1()
exam2 = get_notes_exam2()
average = calculate_average(performance, exam1, exam2)
success = check_success(average)
print(success)







































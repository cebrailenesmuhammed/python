ders = ["B", "İ", "L", "İ", "Ş", "İ", "M"]


ders.sort()
print(ders)


ders.reverse()
print(ders)


print(ders.count("İ"))


ders.remove("Ş")
ders.remove("İ")
ders.remove("İ")
print(ders)


alan = ders.copy()
print(alan)

ders.clear()
print(ders)


print(alan.index("L"))

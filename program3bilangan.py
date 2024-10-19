a = int(input("Masukan Nilai a : "))
b = int(input("Masukan Nilai b : "))
c = int(input("Masukan Nilai c : "))

print("a = ", a)
print("b = ", b)
print("c = ", c)

if a > b and a > c:
    maks = a
    print("Bilangan terbesar adalah a = ", maks)
elif b > a and b > c:
    maks = b
    print("Bilangan terbesar adalah b = ", maks)
else:
    maks = c
    print("Bilangan terbesar adalah c = ", maks)

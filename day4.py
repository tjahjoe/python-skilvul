# 1
def fpb (x, y) :
    if y == 0:
        return x
    else :
        return fpb (y, x%y); 


print(fpb(28, 14))

# 2
angka = [2,3,10,12]
angka = list(filter(lambda x : x % 2 == 0, angka))
print(angka)

# 3
def mir(a):
    kondisi = True
    for i in range(len(x)//2):
        if a[i] != a[i-1]:
            kondisi = False
            break
    return kondisi

print(mir("adaa"))
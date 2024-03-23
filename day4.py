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
mirror =list(filter(lambda x : str(x) == str(x)[::-1], [9, 9]))

def mi(a):
    for i in range(len(a)//2):
        if a[i] != a[i-1]:
            return False
        else :
            return True

print(mi(["a", "d", "a"]))
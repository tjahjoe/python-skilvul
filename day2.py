# a = [2, 4, 5, 5]
# print(a[0])

# b = 5
# b = 6
# print(b)

# ran = range(1,5,1)

# print(ran[3])


# 1
# angka = [1, 2, 3, 4, 5]

l = [1,2,3,4,5]

# l = [x ** 2 for x in l]
# print(l)

# for x in l:
#     print(x**2)

l = list(map(lambda x : x ** 2, l))
print(l)




# 2
o = [1,2,3,4,5]

# 
# for u in o:
#     if u % 2 == 0:
#         print("genap")
#     else:
#         print("ganjil")
def k(x):
    if x % 2 == 0:
        x = "genap"
    else:
        x = "ganjil"
    return x


o = list(map(k, o))
print(o)


# 3
angka = [[1,2,3],[2,3,4],[3,4,5]]
def perkalian(x, y, z):
    return x + y + z

angka = list(map(perkalian, angka[0], angka[1], angka[2]))
print(angka)

# 4
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print(i, " fizzBuzz")
    elif i % 3 == 0:
        print(i, " Fizz")
    elif i % 5 == 0:
        print(i, " Buzz")
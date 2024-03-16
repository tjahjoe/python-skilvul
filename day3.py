
# 1
inpu = [800, 600,400, 200]
Compare_input = [500, 200, 400]

for i in range(len(inpu)):
    if inpu[i] in Compare_input:
        inpu[i] = 1
    else:
        inpu[i] = 0
print(inpu)


# 2
inpu = [100, 200, 300, 400, 500]
Compare_input =[500, 200, 400]
for i in range(len(inpu)):
    if inpu[i] in Compare_input:
        inpu[i] = 1
    else:
        inpu[i] = 0
print(inpu)

# 3
inpu = ["A", "B", 'C']
for indeks, i in enumerate(inpu):
    print(f"{indeks} {i}")

# 4
inpu = [{"nama" : "Budi", "nilai" : 90}, {"nama" : "Dwi", "nilai" : 85}, {"nama" : "Tri", "nilai" : 75}]
tertinggi = inpu[0]
terrendah = inpu[0]
for i in range(len(inpu)):
    if tertinggi["nilai"] < inpu[i]["nilai"]:
        tertinggi = inpu[i]
    elif terrendah["nilai"] > inpu[i]["nilai"]:
        terrendah = inpu[i]
print(f"{tertinggi} \n {terrendah}")

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

# 5
inpu = [{"nama" : "Budi", "gaji" : 5000}, {"nama" : "Dwi", "gaji" : 8000}, {"nama" : "joko", "gaji" : 6000}]
ma = sorted(inpu,key = lambda x : x["gaji"], reverse=True)
total = 0
for i in range(len(inpu)):
    total = total + inpu[i]["gaji"]
    
output = {"highest_salary" : ma[0]["nama"], "total_salary" : total }
print(output)

# 6
data_toko = {
    "indomaret" : {
        "ayam" : 30000,
        "sayur" : 15000,
        "buah" : 20000,
        "ikan" : 22000
    }
}

items_to_buy = {
    "ayam" : 2,
    "sayur" : 1,
    "ikan" : 1
}

jumlah = []
total = 0
for i in data_toko["indomaret"]:
    if i in items_to_buy:
        jumlah.append({i : data_toko["indomaret"][i] * items_to_buy[i] })
        total += data_toko["indomaret"][i] * items_to_buy[i]

print(jumlah)
print(total)

# 6
inpu = {
    "indomaret" : {
        "ayam" : 30000,
        "sayur" : 15000,
        "buah" : 20000,
        "ikan" : 22000,
    },
    "alfamart" : {
        "ayam" : 25000,
        "sayur" : 12000,
        "buah" : 30000,
        "ikan" : 25000
    }
}
temp = []
for i in inpu["indomaret"]:
    if i in inpu["alfamart"]:
        if inpu["indomaret"][i] < inpu["alfamart"][i]:
            temp.append({ i : inpu["indomaret"][i]})
        else :
            temp.append({ i : inpu["alfamart"][i]})

jumlah = []
total = 0;

for indeks, i in enumerate(inpu["indomaret"]) :
    if i in items_to_buy:
        jumlah.append({i : temp[indeks][i] * items_to_buy[i] })
        total += temp[indeks][i] * items_to_buy[i]

print(jumlah)
print(total)

# membandingkan harga yang paling murah
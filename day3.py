
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


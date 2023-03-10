towns = ["Tartu", "Narva", "Tallinn", "Rakvere"]

#for cycle to go through an array
for town in towns:
    print(town)

print("-------------")
#same with while cycle
i = 0
while i < len(towns):
    print(towns[i])
    i += 1

#for cycle to read from file
f = open('data.txt')
for line in f:
    print(line.strip())

f.close()
input()
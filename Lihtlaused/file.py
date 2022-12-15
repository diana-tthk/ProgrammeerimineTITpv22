f = open("andmed.txt")
#Read name and age from file. Each on the separate line
nimi = f.readline().strip()
perekonnanimi = f.readline().strip()
vanus = f.readline().strip()

print("Nimi: ", nimi)
print("Perekonnanimi: ", perekonnanimi)
print ("Vanus: ", vanus)

f.close()

nimi = input("Palun sisesta oma nimi: ")
perekonnanimi = input("Palun sisesta oma perekonnanimi: ")
vanus = input("Palun sisesta oma vanus: ")

f = open("andmed.txt", "a")
f.write(nimi + "\n")
f.write(perekonnanimi + "\n")
f.write(vanus + "\n")
f.close
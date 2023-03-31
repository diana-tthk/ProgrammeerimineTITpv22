#Kirjutada programm, mis loeb andmed failist 
#"andmed.txt" ja tagastab kõik unikaalsed numbrid, mis 
#saab sealt leida

numbers = set(open("andmed.txt").read().split())
#f = open("andmed.txt")
#for l in f:
#    numbers.add(int(l.strip()))
#f.close()

print(numbers)

input()
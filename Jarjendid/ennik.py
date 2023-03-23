#ennik/ tuple - list that cannot be changed
punkt = (3, 8)
print(punkt[0])
#tuple requires less memory than list
a = (1,2,3,4,5,6,7,8)
b = [1,2,3,4,5,6]

print(a.__sizeof__())
print(b.__sizeof__())

#Tuple can hold multiple datatypes 
#(list can too, but it is not a good practice)
andmed = ("Peeter", "Paun", 1967)
print("Eesnimi:", andmed[0])
print("Perenimi:", andmed[1])
print("Sünniaasta:", andmed[2])

input()


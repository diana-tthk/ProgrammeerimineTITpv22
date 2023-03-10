line = "Tere!"
#python can represent string type objects as an array
for letter in line:
    print(letter)

print(line[3])

#split() method
line = "Tere päevast!"
print(line.split())
line = "10.10.14.209"
octets = line.split('.')
print("My fourth octet is: " + octets[3])


input()
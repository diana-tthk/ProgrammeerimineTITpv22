f = open("names.txt")

while True:
    name = f.readline()
    if name == "":
        break

    print("Hello " + name.strip() + "!")

f.close()
input()
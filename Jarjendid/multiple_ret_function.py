def read_data(filename):
    names = []
    brthddates = []

    f = open(filename)
    for line in f:
        data = line.strip().split()
        names.append(data[0])
        brthddates.append(data[1])

    f.close()
    return (names, brthddates)


(names, birthdates) = read_data("f.txt")
print(names)
print(birthdates)
input()

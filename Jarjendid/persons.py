def read_data(filename):
    persons = []
    f = open(filename)
    #for every line in file
    for l in f:
        data = l.strip().split()
        person = (data[0], data[1], int(data[2]))
        #person = tuple(l.strip().split())
        persons.append(person)
    f.close()
    return persons


persons = read_data("../Problems/persons.txt")

max_year = 0
for p in persons:
    if p[2] > max_year:
        max_year = p[2]

#def ret_3d_ele(tuple_1):
#    return tuple_1[2]
#print(max(persons, key=ret_3d_ele)[2])

print("The youngest person's year of birth is: " + str(max_year))
input()
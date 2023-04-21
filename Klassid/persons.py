import datetime

class Person:
    name = ""
    surname = ""
    birthyear = 1900

    def __init__(self, name, surname, birthyear):
        self.name = name
        self.surname = surname
        self.birthyear = birthyear

    def __str__(self):
        return self.name + " " + self.surname + " " + str(self.birthyear)
    def __repr__(self):
        return self.name + " " + self.surname + " " + str(self.birthyear)

    def age(self):
        year = datetime.date.today().year
        return year - self.birthyear

#person = Person("Mari", "Mets", 1993)
#print(person.name, person.surname, person.birthyear)
def read_data(filename):
    persons = []
    with open(filename, 'r') as f:
        #for every line in file
        for l in f:
            data = l.strip().split()
            person = Person(data[0], data[1], int(data[2]))
            persons.append(person)
    
    return persons

persons = read_data("Y:/programmeerimine/skriptid/Problems/persons.txt")
print(persons[0], persons[0].age())

oldest = persons[0]
youngest = persons[0]
for person in persons:
    if person.birthyear < oldest.birthyear:
        oldest = person
    if person.birthyear > youngest.birthyear:
        youngest = person

print("Oldest person is: ", oldest.name, oldest.surname,
oldest.age())
print("Youngest person is: ", youngest.name, youngest.surname,
youngest.age())

#print names and age of those younger than 18

input()
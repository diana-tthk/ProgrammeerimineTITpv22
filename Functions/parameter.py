def hello(name, time = "many"):
    print("Hello " + name)
    print("I haven't seen you for " + str(time) + " days!")

hello("Tiit", 2)
hello("James")

nimi = input("What is your name? ")
hello(nimi, 3)
# hello(input("What is your name? "))

input()
people = int(input("How many peole travel?"))
seats = int(input("How many seats in one bus?"))

buses = people // seats
last_bus = people % seats

if last_bus == 0:
    last_bus = seats
else:
    buses += 1

print("You will need ", str(buses), " buses.")
print("There will be ", str(last_bus), " people in the last bus")
input()

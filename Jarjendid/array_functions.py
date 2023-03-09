numbers = [1, 2, 5, 1]
numbers2 = [5, 4, 2, 7]

#min element
print(min(numbers))
print(min(numbers2))
print("-----------------")
#max element
print(max(numbers))
print(max(numbers2))
print("-----------------")

#sum of the elements
print(sum(numbers))
print(sum(numbers2))
print("-----------------")

#sort elements in the array
print(sorted(numbers))
print(sorted(numbers2))
print("-----------------")
print(numbers)
print(numbers2)
print("-----------------")

#sum the arrays
num3 = numbers + numbers2
print(num3)
print("-----------------")
#count occurences of the specific element
print("I have " + str(num3.count(5)) + " numbers 5 in my array")
input()
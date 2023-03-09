#create array
long_months = [1, 3, 5, 7, 8, 10, 12]

print(long_months)
print("--------------")
#print array element by index
print(long_months[0])
print(long_months[6])
print("--------------")
#assign value of an element to a variable
january = long_months[0]
print(january)
print("--------------")
#change value of an element in the array
long_months[6] = 13
print(long_months)
print("--------------")
#remove element form the array by index
long_months.pop(6)
print(long_months)
print("--------------")
#remove element from the array by value
long_months.remove(10)
print(long_months)
print("--------------")
#add element to the array (to the end)
long_months.append(10)
long_months.append(12)
print(long_months)
print("--------------")
#get length of the array (len)
print("My array length is " + str(len(long_months)))
#get index of the specific element (index)
print("My element 10 index is " + str(long_months.index(10)))

input()
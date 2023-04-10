#Given a list of integers. 
#Determine how many distinct numbers there are.

num = [1, 2, 4, 5, 2, 4, 2, 6, 35, 24]
print(len(set(num)))

#Given two lists of numbers. 
# Count how many unique numbers occur in both of them.

num = [1, 2, 6, 4, 5, 7]
num2 = [10, 2, 3, 4, 8]

print(len(set(num).intersection(set(num2))))

#Given two lists of numbers. 
# Find all the numbers that occur in both 
# the first and the second list 
# and print them in ascending order.

num = [82, 54, 91, 100, 70, 33, 88, 
14, 52, 48, 56, 20, 63, 16, 22, 23, 30, 
8, 84, 75, 45]

num2 = [10, 44, 77, 90, 43, 75, 25, 24, 
5, 21, 71, 70, 83, 68, 18, 92, 81, 57, 
27, 67, 48, 6]

print(sorted(set(num).intersection(set(num2))))

#Given a sequence of numbers, 
# determine if the next number 
# has already been encountered. 
# For each number, print the word YES 
# (in a separate line) 
# if this number has already been encountered, 
# and print NO, if it has not already been encountered.

num = [1, 2, 3, 2, 3, 4]

unique = set()
length = len(unique)
for number in num:
    unique.add(number)
    if (len(unique) > length):
        print("NO")
        length = len(unique)
    else:
        print("YES")
        
input()

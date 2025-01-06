# In[]:
# MIT course: Introduction to CS and Programming using Python
# 6.100L | Fall 2022 | Undergraduate
# Lecture 3





# In[]:
# directory

import os
directory = r'C:\Users\panah\OneDrive\Desktop\Work\1 - MIT - Courses'
os.chdir(directory)
del directory





# In[]:
# Exercise 1

# Expand this code to show a sad face when the user entered 
# the while loop more than 2 times. Hint: use a counter
###################
# where = input("Go left or right? ")
# while where == "right":
#     where = input("Go left or right? ")
# print("You got out!")

where = input("Go left or right? ")
n = 1

while where == "right":
    if n > 2:
        print(":(")
    where = input("Go left or right? ")
    n += 1
    
print("You got out!")





# In[]:
# Exercise 2

# Fix this code to use variables start and end in the 
# range, to get the total sum between and including those values. 

# mysum = 0
# start = 3
# end = 5
# for i in range(start, end):
#     mysum += i
# print(mysum)

mysum = 0
start = 3
end = 5

for i in range(start, end+1):
    mysum += i

print(mysum)





# In[]:
# Exercise 3

# Write a program that:
# Practice 1: 
# Declare a variable x that stores an int > 0. Print all ints, one on each
# line, between 1 (inclusive) and x (inclusive) that are divisible by 5.
# For ex. if x = 15, it prints 5, 10, and 15. 
# For ex. if x = 14, it prints 5 and 10.

x = int(input("Enter a positive integer: "))

for i in range(1,x+1):
    if i%5==0:
        print(i)





# In[]
# Exercise 4

# Practice 2:
# Declare a variable n that stores an int. Print the sum of all digits 
# in n. Hint: you can get a digit at a time looking at the remainder 
# when you divide n by 10.
# For ex. If x = 1234, print 10

# version 1
n = input("Enter an integer: ")
mysum = 0

for i in n:
    digit = int(i)
    mysum += digit

print(mysum)



# version 2
n = int(input("Enter an integer: "))
mysum = 0

while True:
    remainder = n % 10
    mysum += remainder
    n = n // 10
    
    if n == 0:
        break

print(mysum)





# In[]
# Finger exercise

# Assume you are given a positive integer variaböe named N.
# Write a piece of Python code that prints hello world on separate lines, N times. 
# You can use either a while loop or a for loop.

n = int(input("Enger a positive integer: "))

for i in range(n):
    print("hello world")



# In[]:
# MIT course: Introduction to CS and Programming using Python
# 6.100L | Fall 2022 | Undergraduate
# Lecture 4





# In[]:
# directory

import os
directory = r'C:\Users\panah\OneDrive\Desktop\Work\1 - MIT - Courses'
os.chdir(directory)
del directory





# In[]:
# Exercise 1

# Write code that loops a for loop over some range 
# and prints how many even numbers are in that range. Try it with:
# range(5)
# range(10)
# range(2,9,3)
# range(-4,6,2)
# range(5,6)

#for i in range(5):
    # your code here

range_list = [range(5), range(10), range(2,9,3), range(-4,6,2), range(5,6)]
even = []

for i in range_list:
    total_num = 0
   
    for j in i:
        if j%2 == 0:
            total_num += 1
    
    even.append(total_num)





# In[]:
# Exercise 2

# Assume you are given a string of lowercase letters in variable s. 
# Count how many unique letters there are in s. For example, if 
# s = "abca" Then your code prints 3. 

# your code here
s = 'abca'

new_word = ''
for i in s:
    if i not in new_word:
        new_word = new_word + i
print(len(new_word))





# In[]:
# Exercise 3

# Hardcode a number as a secret number. Write a program that 
# checks through all the numbers between 1 to 10 and prints the 
# secret value. If it's not found, it doesn't print anything. 

# your code here
# secret = 4

import random

random.seed() # input seed number for a consistent output
secret = random.randint(1,20)
condition = True

for i in range(1,10):
    if i == secret:
        print("Secret number is: ", i)
        condition = False

if condition:
    print("secret number is not between 1 and 10")




# In[]
# Exercise 4 --- AT HOME

# Write code that counts how many unique common characters there are between 
# two strings. For example below, the common characters count is 8: 
# text1 = "may the fourth be with you"
# text2 = "revenge of the sixth"
# Hint, start to write your code with a smaller example, then test it on the above text.

# text1 = "abc"
# text2 = "cde"
# your code here

# text
text1 =  "may the fourth be with you"
text2 = "revenge of the sixth"

# set variables
common = ""
unique = ""

# loop
for char in text1:
    if char in text2:
        common = common + char
        if char not in unique:
            unique = unique + char
      
# lenght
print(len(unique))





# In[]
# Finger exercise

# Assume you are given a positive integer variable named N.
# Write a piece of Python code that finds the cube root of N. 
# The code prints the cube root if N is a perfect cube or it prints error if N is not a perfect cube. 
# Hint: use a öoop that increments a counter --you decidewhen the counter shouöd stop.

# inputs
n = random.randint(-1000,1000)
print(n)

guess = int(input("What is your initial guess? "))
check = [] # collects all guesses


# set common sing
if n * guess < 0:
    guess = -guess


# loop
condition = True

while condition: 
    check.append(guess)
    
    # check if guess is spot on
    if guess ** 3 == n:
        print("Cube root of", n, "is", guess)
        condition = False
        break 
     
    # adjust the guess up or down             
    if guess ** 3 > n: 
        guess = guess - 1
    else:
        guess = guess + 1
     
    # check for repetitions
    if guess in check:
        break
  
# if cubic root is not found
if condition:
    print("Cube root of ", n, "is between", check[-2], "and", check[-1])







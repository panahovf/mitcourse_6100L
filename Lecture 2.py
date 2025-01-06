# In[]:
# MIT course: Introduction to CS and Programming using Python
# 6.100L | Fall 2022 | Undergraduate
# Lecture 2





# In[]:
# directory

import os
directory = r'C:\Users\panah\OneDrive\Desktop\Work\1 - MIT - Courses'
os.chdir(directory)
del directory





# In[]:
# Exercise 1

# Write a program that: 
# * Asks the user for a verb.
# * Prints "I can _ better than you" where you replace _ with the verb.
# * Then prints the verb 5 times in a row separated by spaces.
# For example, if the user enters run, you print:
#     I can run better than you!
#     run run run run run

# Solution
x = input("Enter a verb: ")
y = "I can " + x + " better than you"
z = 5* (x + " ")
print(y)
print(z)

del (x,y,z)





# In[]:
# Exercise 2

# Write a program that:
# * Saves a secret number. 
# * Asks the user for a number guess.
# * Prints a bool depending on whether the guess matches the secret.

# Solution
secret_num = 17
guess_num = input("Enter your number: ")
check = secret_num == guess_num
print("You gues was:", check)

del(secret_num, guess_num, check)





# In[]:
# Exercise 2

# Write a program that:
# * Saves a secret number. 
# * Asks the user for a number guess.
# * Prints whether the guess is too low, too high, or the same as the secret. 

# Solution
secret_num = 17
guess_num = int(input("Enter your guess: "))

if guess_num < secret_num:
    print("Your guess is low")
elif guess_num > secret_num:
    print("Your guess it high")
else:
    print("Your guess is correct!")

del(secret_num, guess_num)





# In[]
# Finger exercise

# Assume you are given a variable named number (has a numerical value). 
# Write a piece of Python code that prints out one of the following strings: 
# positive if the variable number is positive
# negative if the variable number is negative
# zero if the variable number is equal to zero

number = np.random.randint(-100,100)

if number > 0:
    print("positive")
elif number < 0:
    print("negative")
else:
    print("zero")







# In[]:
# MIT course: Introduction to CS and Programming using Python
# 6.100L | Fall 2022 | Undergraduate
# Lecture 1





# In[]:
# directory

import os
directory = r'C:\Users\panah\OneDrive\Desktop\Work\1 - MIT - Courses'
os.chdir(directory)
del directory





# In[]:
# Finger exercise 1

# Assume 3 variables are already defined for you: a, b, and c. 
# Create a variable called total that adds a and b then multiplies the result by c. 
# Include a last line in your code to print the value: print(total)


# Solution
a = 3
b = 4
c = 5

total = (a+b)*c

print(total)
del (a,b,c,total)




# In[]:
# Problem Set 0

# Problem 1
# Write a program that does the following in order:
# 1. At the top of your file and type: import numpy
# 2. Now write a line that sets a variable named x to 5.
# 3. Now write a line that sets a variable named y to 8.
# 4. Add variables x and y, and save the result to a variable named z .
# 5. Now save the result of this command: numpy.log2(z) to a variable named a .

# Solution
import numpy as np

x = 5
y = 8
z = x+y
a = np.log2(z)
print(a)
del(x,y,z,a)



# Problem 2
# Write a program that does the following in order:
# 1. Asks the user to enter a number “x”
# 2. Asks the user to enter a number “y”
# 3. Prints out number “x”, raised to the power “y”.
# 4. Prints out the log (base 2) of “x”.

# Solution
x = float(input("Enter number x: "))
y = float(input("Enter number y: "))
print(x**y)
print(np.log2(x))
del(x,y)


















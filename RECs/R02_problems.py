####################################################################################
# Practice Problem 1
# Write a program that takes your name as an Input and Outputs the length of your name minus 5.

# Insert code below
name = input("Enter your full name: ")
name_len = len(name) - 1 # removes the space between first and last names
print(name_len - 5)
      
  

####################################################################################
# Practice Problem 2
# Write a program to remove the nth character from a non empty string.
# Print the old string and the new string.

test_string = "We want to remove the nth character from this string"
n = 8

# Insert code below
updated_string = test_string[:n-1] + test_string[n:]
print(test_string)
print(updated_string)
print("n'th character is: ", "'", test_string[n-1], "'")



####################################################################################
# Practice Problem 3
# Write a program which answers the following:
# Does a given string have length greater than 10 or less than 5? If True, output True. If False, output False.

my_string = "This is my string"  # example string - modify to test

# Insert code below
string_len = len(my_string)
if string_len > 10 or string_len < 5:
    print("True")
else:
    print(False)


####################################################################################
# Practice Problem 4
# Write a program which answers the following using a for loop:
# Count the number of e's in the following string

my_string = "How many times is the letter e in this string?"

# Insert code below
n = 0
for i in my_string:
    if i == "e":
        n += 1
    
print(n)




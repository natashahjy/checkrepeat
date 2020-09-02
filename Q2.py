# Assignment 2 Question 2
# Done By: Natasha Heng Jeng Yee
# UOW ID Number: 6959684

import collections
# Check repeating characters (a-z) and (A-Z) in String
# Check for errors

# Function to check for repeat characters in string
def check_repeat(user_input_test):
    repeat = False
    repeat_frequency = collections.Counter(user_input_test)
    for key, value in repeat_frequency.items():
        if value > 1:
            repeat = True
       
    return repeat

# Prompt user to enter string
while True:
    user_input = input("Enter a String:")
    
    # Check if user entered string is alphabets
    # If not show error message and prompt for input again
    if (not user_input.isalpha()):
        print("Please enter (a-z) or (A-Z)\n")
        continue
    
    # if repeat is true, print repeat found
    # else print no repeat found and stop loop
    if (check_repeat(user_input)):
        print("Repeat found\n")
    else:
        print("No repeat found",end="")
        break
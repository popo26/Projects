#https://github.com/CodingNomads/python_miniprojects/tree/master/sentence_analysis

# Write a script that takes a sentence from the user and returns:

# the number of lower case letters
# the number of uppercase letters
# the number of punctuations characters
# the total number of characters
# Use a dictionary to store the count of each of the above.

# Note: ignore all spaces.

# Example input:

# I love to work with dictionaries!
# Example output:

# Upper case: 1
# Lower case: 26
# Punctuation: 1
# Total chars: 28


import string
print(string.punctuation)

user_input = input("Enter a sentence: ")

lower_count = 0
upper_count = 0
punctuation_count = 0
total_char = 0
result = {}

for char in user_input:
    if char.islower():
        lower_count += 1
        total_char += 1
    elif char.isupper():
        upper_count += 1
        total_char += 1
    elif char in string.punctuation:
        punctuation_count += 1
        total_char+= 1

result = {"Upper Case": upper_count, "Lower Case": lower_count, "Punctuation": punctuation_count, "Total Chars": total_char}
print(result)




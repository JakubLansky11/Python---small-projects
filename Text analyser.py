# Project - text analyser
# Author - Jakub Lánský
# Email - kubik.langos@seznam.cz

import sys
indent = "-" * 130

# Entering name

name = input("Hello. Please, write your name: ")
print(indent)
print("Welcome to the ap, ", name)
print("You can write your own text to be analysed!")
print(indent)

# Selecting a text
while True:
    text = input("Write your text: ")

# Adjusting of the text
    adjusted_text = []
    items = text.split()
    for item in items:
        adjusted_item = str(item.strip(".,"))
        adjusted_text.append(adjusted_item)

# Number of words

    words_count = len(adjusted_text)
    print("There are", words_count, "words in the selected text.")


# Number of tittlecase, uppercase, lowercase words and numeric strings and their sum

    tittlecase_count = 0
    uppercase_count = 0
    lowercase_count = 0
    numerics_count = 0
    numerics_sum = 0
    numbers = []
    for letter in adjusted_text:
        if letter.istitle():
            tittlecase_count = tittlecase_count + 1
        elif letter.isupper() and letter.isalpha():
            uppercase_count = uppercase_count + 1
        elif letter.islower():
            lowercase_count = lowercase_count + 1
        elif letter.isnumeric():
            numerics_count = numerics_count + 1
            numbers.append(int(letter))
            numerics_sum = sum(numbers)

    print("There are", tittlecase_count, "titlecase words.")
    print("There are", uppercase_count, "uppercase words.")
    print("There are", lowercase_count, "lowercase words.")
    print("There are", numerics_count, "numeric strings.")
    print("The sum of all the numbers", numerics_sum)

# Graph    print(item, "|", word_lengths.count(item) * "*", "|", word_lengths.count(item))

    print(indent)     
    print(f"Len| OCCURENCES:              |NR.")
    print(indent) 
    words = adjusted_text
    word_lengths = [len(word) for word in words]
    range_max = max(word_lengths) + 1
    for item in range(1, range_max):
        x_counts = word_lengths.count(item) * "*"
        print(f" {item :^2}| {x_counts :^25}| {word_lengths.count(item)}")
    continue

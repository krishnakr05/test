"""Reverses the given string."""
def reverse_string(s):
    return s[::-1]

"""Counts the number of vowels in a string."""
def count_vowels(s):
    count = 0
    for char in s.lower():
        if char in "aeiou":
            count += 1
    return count

"""
Complete the count_vowels function. It takes a string and returns:

The total number of vowels in the string (count every occurrence, not just unique)
A set of the unique vowels found in the string
We are only interested in the 5 vowels: a, e, i, o, u, and their capitalized versions. Treat uppercase and lowercase vowels as separate. For example, "A" and "a" are not the same.
"""
def count_vowels(text):
    strlist = list(text)
    vowels_count = 0
    unique_vowels = set()
    vowels = {"a", "A", "e", "E", "i", "I", "o", "O", "u", "U"}

    for letter in strlist:
        if letter in vowels:
            vowels_count += 1
            if letter not in unique_vowels:
                unique_vowels.add(letter)
    return vowels_count, unique_vowels
        
        
            
        
      

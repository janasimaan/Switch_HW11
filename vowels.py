def letters(str):
    vowels = "aeiouAEIOU"
    counting_vowels = sum(1 for char in str if char in vowels)
    counting_consonant = sum(1 for char in str if char.isalpha() and char not in vowels)
    return counting_vowels, counting_consonant

input_string = "Hello World!"
vowels, consonants = letters(input_string)
print(f"Vowels: {vowels}, Consonants: {consonants}")
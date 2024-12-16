def word_score(str):

    def get_word_score(word):
        return sum(ord(char) - ord('a') + 1 for char in word)

    words = str.split()
    highest_Score = 0
    highest_Word = ""

    for word in words:
        score = get_word_score(word)
        if score > highest_Score:
            highest_Score = score
            highest_Word = word
    return highest_Word

input_string = "apple banana cherry"
result = word_score(input_string)
print(f"Highest scoring word: {result}")
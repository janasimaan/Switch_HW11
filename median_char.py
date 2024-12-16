def median_ch(str):
    sorted_chars = sorted(str)
    median_index = len(sorted_chars)//2
    return sorted_chars[median_index]

input_string = "abcde"
result = median_ch(input_string)
print(f"Median character: {result}")

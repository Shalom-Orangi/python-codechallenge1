def consonant_value(s):
    vowels = "aeiou"
    max_value = 0
    current_value = 0

    for char in s:
        if char not in vowels:
            # ord is a command that calculates the numeric values in every lowercase letter
            value = ord(char) - ord('a') + 1
            current_value += value
        else:
            # If a vowel is encountered, update max_value and reset current_value
            max_value = max(max_value, current_value)
            current_value = 0

    max_value = max(max_value, current_value)

    return max_value

input_string = "strength"
result = consonant_value(input_string)
print(result)




def calculate_control_digit(reference):
    first_part = reference[:7] + reference[14:]
    second_part = reference[7:14] + reference[14:]

    # Step 2: Convert letters to numbers according to the mapping
    conversion_table = {
        'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9,
        'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'Ñ': 15, 'O': 16, 'P': 17,
        'Q': 18, 'R': 19, 'S': 20, 'T': 21, 'U': 22, 'V': 23, 'W': 24, 'X': 25,
        'Y': 26, 'Z': 27
    }
    first_part_numbers = [conversion_table[letter] if letter in conversion_table else int(letter) for letter in
                          first_part]
    second_part_numbers = [conversion_table[letter] if letter in conversion_table else int(letter) for letter in
                           second_part]

    # Step 3: Multiply each number by the values according to their position
    multiplication_values = [13, 15, 12, 5, 4, 17, 9, 21, 3, 7, 1]
    first_part_multiplied = [num * multiplication_values[i] for i, num in enumerate(first_part_numbers)]
    second_part_multiplied = [num * multiplication_values[i] for i, num in enumerate(second_part_numbers)]

    # Step 4: Sum all the values obtained in each list
    sum_first_part = sum(first_part_multiplied)
    sum_second_part = sum(second_part_multiplied)

    # Step 5: Get the remainder when divided by 23
    remainder_first_part = sum_first_part % 23
    remainder_second_part = sum_second_part % 23

    # Step 6: Convert the remainders to letters according to the conversion table
    letter_table = {
        0: 'M', 1: 'Q', 2: 'W', 3: 'E', 4: 'R', 5: 'T', 6: 'Y', 7: 'U', 8: 'I',
        9: 'O', 10: 'P', 11: 'A', 12: 'S', 13: 'D', 14: 'F', 15: 'G', 16: 'H',
        17: 'J', 18: 'K', 19: 'L', 20: 'B', 21: 'Z', 22: 'X'
    }
    first_control_digit = letter_table[remainder_first_part]
    second_control_digit = letter_table[remainder_second_part]
    return first_control_digit, second_control_digit


# example use
example = '9872023VH5797S0001'
cd = calculate_control_digit(example)
print(cd)

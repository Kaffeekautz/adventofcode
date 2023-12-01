def replace_words_with_digits(line):
    # Define a lookup for numbers written out as words
    number_words = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

    # Replace written-out numbers with digits
    for word, digit in number_words.items():
        line = line.replace(word, digit)

    return line

def find_first_and_last_digits(line):
    # Find the first and last digits in the string
    first_digit = next((int(char) for char in line if char.isdigit()), None)
    last_digit = next((int(char) for char in reversed(line) if char.isdigit()), None)

    return first_digit, last_digit

def process_file(file_path):
    concatenated_numbers = ""
    total_sum = 0

    with open(file_path, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            line = line.strip()
            if line:
                modified_line = replace_words_with_digits(line)
                first_digit, last_digit = find_first_and_last_digits(modified_line)
                concatenated_row = str(first_digit) + str(last_digit)
                concatenated_numbers += concatenated_row
                total_sum += int(concatenated_row)

                print(f"Row {line_number}: Original: {line}, Modified: {modified_line}, Concatenated: {concatenated_row}")

    print(f"\nConcatenated Numbers: {concatenated_numbers}")
    print(f"Total Sum: {total_sum}")

if __name__ == "__main__":
    file_path = '01-12-23\input.txt'  # Replace 'your_file.txt' with the actual file path
    process_file(file_path)

def findandaddnumbers(file_path):
    total_sum = 0
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()  # Remove leading and trailing whitespaces
                if line:  # Check if the line is not empty
                    first_digit = next((char for char in line if char.isdigit()), '')
                    last_digit = next((char for char in reversed(line) if char.isdigit()), '')
                    combined_number = first_digit + last_digit
                    if combined_number:
                        total_sum += int(combined_number)
                        print(f"Line: {line}, Full Number: {combined_number}")
        print(f"Total Sum of Full Numbers: {total_sum}")

    except Exception as e:
        print(f"An error occurred: {e}")


file_path = '01-12-23\input.txt'
findandaddnumbers(file_path)

def calculate_points(winning_numbers, your_numbers):
    # Find the numbers that are both in winning_numbers and your_numbers
    matches = [num for num in your_numbers if num in winning_numbers]
    matches_count = len(matches)

    return matches, matches_count

def main():
    # Read lines from the input file
    with open("04-12-23/input.txt", "r") as file:
        lines = file.readlines()

    total_points = 0

    card_info = []

    for line in lines:
        line = line.strip()

        # Extract card number and numbers from the line
        parts = line.split(":")
        if len(parts) != 2:
            continue

        card_number = parts[0].strip()
        numbers_str = parts[1].strip()

        try:
            # Split the numbers into winning_numbers and your_numbers
            your_numbers_str, winning_numbers_str = numbers_str.split("|")
            winning_numbers = sorted(list(map(int, winning_numbers_str.split())))
            your_numbers = sorted(list(map(int, your_numbers_str.split())))

            # Calculate points and get matches for the current card
            matches, matches_count = calculate_points(winning_numbers, your_numbers)
            card_points = matches_count * 2
            total_points += card_points

            # Store card information for later sorting and display
            card_info.append((int(card_number.split()[1]), f"Card {card_number}", card_points, your_numbers, winning_numbers, matches))
        except ValueError:
            print(f"Skipping invalid line: {line}")

    # Sort the card_info list by card number
    card_info.sort(key=lambda x: x[0])

    # Display information for each card in sorted order
    for _, card_number, points, your_numbers, winning_numbers, matches in card_info:
        print(f"{card_number}: {points} Points")
        print("Left side: ", winning_numbers)
        print("Right side: ", your_numbers)
        print(f"Matches: {matches}")
        print("=" * 40)  # Separator line

    print("Total points:", total_points)

if __name__ == "__main__":
    main()

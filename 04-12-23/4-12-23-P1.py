def calculate_points(winning_numbers, your_numbers):
    matches = [num for num in your_numbers if num in winning_numbers]
    matches_count = len(matches)

    if matches_count == 1:
        print(f"Matches: [{matches[0]}]")
        return 1
    elif matches_count > 1:
        print(f"Matches: {matches}")
        return matches_count * 2
    else:
        print("No Matches")
        return 0

def main():
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
            your_numbers_str, winning_numbers_str = numbers_str.split("|")
            winning_numbers = sorted(list(map(int, winning_numbers_str.split())))
            your_numbers = sorted(list(map(int, your_numbers_str.split())))

            card_points = calculate_points(winning_numbers, your_numbers)
            total_points += card_points

            card_info.append((int(card_number.split()[1]), f"Card {card_number}", card_points, your_numbers, winning_numbers))
        except ValueError:
            print(f"Skipping invalid line: {line}")

    # Sort the card_info list by card number
    card_info.sort(key=lambda x: x[0])

    for _, card_number, points, your_numbers, winning_numbers in card_info:
        print(f"{card_number}: {points} Points")
        print("Left side: ", your_numbers)
        print("Right side: ", winning_numbers)
        print("=" * 40)  # Separator line

    print("Total points:", total_points)

if __name__ == "__main__":
    main()

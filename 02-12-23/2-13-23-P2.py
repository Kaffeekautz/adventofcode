def find_min_cubes(game):
    min_cubes = {}

    for subset in game:
        set_cubes = {}

        for cube in subset.split(', '):
            count, color = cube.split()
            set_cubes[color] = set_cubes.get(color, 0) + int(count)

        for color, count in set_cubes.items():
            if color not in min_cubes or count > min_cubes[color]:
                min_cubes[color] = count

    return min_cubes

def sum_of_power_of_min_sets(game_records):
    total_power = 0

    for game_record in game_records:
        game_info = game_record.split(': ')[1]
        game = game_info.split('; ')
        min_cubes = find_min_cubes(game)

        # Calculate the power of the minimum set for the game
        power = min_cubes['red'] * min_cubes['green'] * min_cubes['blue']
        total_power += power

    return total_power

def read_game_records_from_file(file_path):
    with open(file_path, 'r') as file:
        game_records = file.readlines()
    return game_records


file_path = '02-12-23\input.txt'
game_records = read_game_records_from_file(file_path)

# Calculate and print the sum of the power of the minimum sets for all games
result = sum_of_power_of_min_sets(game_records)
print(f"Total Sum of Power of Minimum Sets: {result}")

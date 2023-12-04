def is_possible(game, cube_counts):
    for subset in game:
        for cube in subset.split(', '):
            count, color = cube.split()
            if int(count) > cube_counts[color]:
                return False
    return True

def print_game_details(game_record, cube_counts):
    game_info = game_record.split(': ')
    game_id = int(game_info[0][5:])
    revealed_sets = game_info[1].split('; ')
    
    print(f"Game {game_id}:")
    
    for idx, revealed_set in enumerate(revealed_sets, 1):
        print(f"  Set {idx}: {revealed_set}")
    
    possible = is_possible(revealed_sets, cube_counts)
    print(f"  Possible: {'Yes' if possible else 'No'}")
    
    return game_id, possible

def sum_of_possible_games(game_records, cube_counts):
    possible_games = []
    for game_record in game_records:
        game_id, possible = print_game_details(game_record, cube_counts)
        possible_games.append((game_id, possible))
        print()

    return possible_games

def read_game_records_from_file(file_path):
    with open(file_path, 'r') as file:
        game_records = file.readlines()
    return game_records


file_path = '02-12-23\input.txt'
cube_counts = {'red': 12, 'green': 13, 'blue': 14}

game_records = read_game_records_from_file(file_path)
result = sum_of_possible_games(game_records, cube_counts)

# Print the total sum of possible games
total_sum = sum(game_id for game_id, possible in result if possible)
print(f"Total Sum of Possible Games: {total_sum}")

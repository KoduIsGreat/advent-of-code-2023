from typing import Dict


sample_input = """
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""


def parse_game(input: str) -> tuple[int, Dict[int, Dict[str, int]]]:
    split = input.split(':')
    if len(split) != 2:
        print(f'Skipping non size 2 split: {split}')
    game, rounds = split
    game_id = int(game.split(' ')[1])
    rounds = rounds.split(';')
    round_num = 1
    round_sets = {}
    for r in rounds:
        sets = {}
        color_count = r.split(',')
        for cc in color_count:
            count, color = cc.strip().split(' ')
            sets[color] = int(count)
        round_sets[round_num] = sets
        round_num += 1
    return game_id, round_sets


def get_max_colors():
    return {
        'red': 12,
        'green': 13,
        'blue': 14
    }


def find_answer(input: str):
    games = {}
    possible_game_ids = {}
    for line in input.split('\n'):
        if line == '':
            continue
        if line:
            game_id, sets = parse_game(line)
            games[game_id] = sets

    for game_id, rounds in games.items():
        print(f'Game {game_id}: {rounds}')
        invalid_round = False
        for round_id, sets in rounds.items():
            max_colors = get_max_colors()
            for color, count in sets.items():
                max_colors[color] -= count
            print(f'Game {game_id}-{round_id} colors: {max_colors}')
            if any(v < 0 for v in max_colors.values()):
                invalid_round = True
                break
        if not invalid_round:
            possible_game_ids[game_id] = 1

    return sum(possible_game_ids.keys())


ans = find_answer(sample_input)
print("Sample Answer: ", ans)
with open("2/input.txt") as file:
    input = file.read()
    print("Answer: ", find_answer(input))

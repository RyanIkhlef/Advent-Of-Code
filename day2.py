import re

input = "./inputs/day2/step_1"


def game_is_possible(color: str):
    max_red_cubes = 12
    max_green_cubes = 13
    max_blue_cubes = 14

    number = int(re.search(r"[0-9]*", color).group())
    if "red" in color and number > max_red_cubes:
        return False
    elif "green" in color and number > max_green_cubes:
        return False
    elif "blue" in color and number > max_blue_cubes:
        return False

    return True


def parse_line(line: str):
    game_metadata_end_index = line.find(":")
    game_id = int(line[len("game") + 1:game_metadata_end_index])
    game_set = line[game_metadata_end_index + 2:].split(";")

    return game_id, game_set


def step1():
    with (open(input, "r", encoding="utf-8") as file):
        result = 0
        for line in file:
            line = line[:-1]
            game_id, game_set = parse_line(line)

            game_possible = True
            for subset in game_set:
                sublist = subset.split(",")
                for color in sublist:
                    if not game_is_possible(color.strip()):
                        game_possible = False
                        break
                if not game_possible:
                    break

            if game_possible:
                result += game_id

    print("La réponse de l'étape 1 est :", result)


step1()


def step2():
    with (open(input, "r", encoding="utf-8") as file):
        result = 0

        for line in file:
            line = line[:-1]
            game_id, game_set = parse_line(line)
            max_should_red = 0
            max_should_green = 0
            max_should_blue = 0

            for subset in game_set:
                sublist = subset.split(",")
                for color in sublist:
                    color = color.strip()
                    number = int(re.search(r"[0-9]*", color).group())
                    cube_color = re.search(r"red|green|blue", color).group()
                    if cube_color == "red" and number > max_should_red:
                        max_should_red = number
                    elif cube_color == "green" and number > max_should_green:
                        max_should_green = number
                    elif cube_color == "blue" and number > max_should_blue:
                        max_should_blue = number

            result += max_should_red * max_should_green * max_should_blue

    print("La réponse de l'étape 2 est :", result)


step2()

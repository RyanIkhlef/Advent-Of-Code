import re

input = "./inputs/day4/test"


def step1():
    result = 0
    with open(input, "r", encoding="utf-8") as file:
        for line in file:
            line = line[:-1]
            start_line_index = re.search(r"^Card\s+[0-9]+:", line).span()[1]
            line = line[start_line_index:].strip()
            split = line.split("|")
            winning_number = re.findall(r"[0-9]+", split[0])
            picked_number = re.findall(r"[0-9]+", split[1])

            intersection = [value for value in picked_number if value in winning_number]
            size_intersection = len(intersection)
            if size_intersection > 0:
                result += pow(2, size_intersection - 1)

    print("La réponse de l'étape 1 est :", result)


step1()


def compute_next(data: list, start_index: int, end_index: int):
    result = 0
    cpt_card = start_index
    while cpt_card < end_index:
        card = data[cpt_card]
        winning_numbers = card[0]
        picked_numbers = card[1]
        intersection = [value for value in picked_numbers if value in winning_numbers]
        size_intersection = len(intersection)
        if size_intersection > 0:
            result += pow(2, size_intersection - 1)
            for cpt in range(1, size_intersection + 1):
                result += compute_next(data, cpt_card + cpt, cpt_card + cpt + size_intersection)
        cpt_card += 1
    return result

def compute(data: list):
    card_numbers = len(data)
    card_cpt = 0
    result = 0

    while card_cpt < card_numbers:
        card = data[card_cpt]
        winning_numbers = card[0]
        picked_numbers = card[1]
        intersection = [value for value in picked_numbers if value in winning_numbers]
        size_intersection = len(intersection)
        if size_intersection > 0:
            result += pow(2, size_intersection - 1) + compute_next(data, card_cpt + 1, size_intersection + 1)
        card_cpt += 1
    return result



def step2():
    game = []
    with open(input, "r", encoding="utf-8") as file:
        for line in file:
            line = line[:-1]
            start_line_index = re.search(r"^Card\s+[0-9]+:", line).span()[1]
            line = line[start_line_index:].strip()
            split = line.split("|")
            winning_number = re.findall(r"[0-9]+", split[0])
            picked_number = re.findall(r"[0-9]+", split[1])
            game.append((winning_number, picked_number))

    result = compute(game)

    print("La réponse de l'étape 2 est :", result)


step2()

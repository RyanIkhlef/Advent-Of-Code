import re

input = "./inputs/day3/step_1"


def get_sum(data: list):
    result = 0
    pattern = r"[0-9]+"
    line_cpt = 0
    while line_cpt < len(data):
        current_line = 0
        line = data[line_cpt]
        numbers = re.finditer(pattern, line)

        print("ligne :", line_cpt + 1)
        for itr in numbers:
            start_index = itr.start()
            end_index = itr.end() - 1
            number = itr.group()
            found = False

            # Regarde à gauche (-1, 0)
            if start_index > 0 and not line[start_index - 1].isdigit() and line[start_index - 1] != ".":
                current_line += int(number)
                result += int(number)
                print("\tnumber :", number, "trouver à gauche.")
                found = True

            # Regarde à droite (1, 0)
            elif end_index + 1 < len(line) and not line[end_index + 1].isdigit() and line[end_index + 1] != ".":
                current_line += int(number)
                result += int(number)
                print("\tnumber :", number, "trouver à droite.")
                found = True

            elif line_cpt > 0:
                line_before = data[line_cpt - 1]

                if start_index > 0:
                    special_char = re.search(r"[^0-9.]+", line_before[start_index - 1:end_index + 2])
                else:
                    special_char = re.search(r"[^0-9.]+", line_before[start_index: end_index + 2])

                # Regarde au dessus (-1,1), (1,0), (1,1)
                if not special_char is None:
                    current_line += int(number)
                    result += int(number)
                    print("\tnumber :", number, "trouver au dessus.")
                    found = True

            if not found and line_cpt + 1 < len(data):
                line_after = data[line_cpt + 1]
                if start_index > 0:
                    special_char = re.search(r"[^0-9.]+", line_after[start_index - 1:end_index + 2])
                else:
                    special_char = re.search(r"[^0-9.]+", line_after[start_index:end_index + 2])

                # Regarde en dessous (-1,-1), (0, -1), (1, -1)
                if not special_char is None:
                    current_line += int(number)
                    result += int(number)
                    print("\tnumber :", number, "trouver en dessous.")

        print(line, "=>", result, ":", current_line)
        line_cpt += 1

    return result


def step1():
    with open(input, "r", encoding="utf-8") as file:
        data = []
        for line in file:
            line = line[:-1]
            data.append(line)

        resultat = get_sum(data)

    print("La réponse de l'étape 1 est :", resultat)


step1()


def step2():
    with open(input, "r", encoding="utf-8") as file:
        for line in file:
            line = line[:-1]
            break

    print("La réponse de l'étape 2 est :", "niy")


step2()

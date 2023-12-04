import re

input = "./inputs/day3/test"


def get_sum_by_digit(data: list):
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

    resultat = get_sum_by_digit(data)

    print("La réponse de l'étape 1 est :", resultat)


step1()


def get_sum_by_char(data: list):
    result = 0
    pattern = r"[^0-9.]+"
    line_cpt = 0
    while line_cpt < len(data):
        line = data[line_cpt]
        characters = re.finditer(pattern, line)
        print("ligne :", line_cpt + 1)
        for itr in characters:
            start_index = itr.start()
            end_index = itr.end() - 1
            char = itr.group()

            if char != "*":
                print("char est :", char)
                matchItr = re.finditer(r"[0-9]+", line)
                if not matchItr is None:
                    for it in matchItr:
                        match_start_index = it.start()
                        match_end_index = it.end()
                        if match_end_index == start_index:
                            print("trouver à gauche :", it.group())
                            result += int(it.group())
                            break
                        elif match_start_index == end_index + 1:
                            print("trouver à droite :", it.group())
                            result += int(it.group())
                            break

                    # if line_cpt > 0:
                    #     line_after = data[line_cpt - 1]
                    #     special_char = re.finditer(r"[0-9]+", line_after)
                    #     for it in special_char:
                    #         match_start_index = it.start()
                    #         match_end_index = it.end()
                    #         if match_end_index >= start_index and match_start_index <= end_index + 1:
                    #             result += int(it.group())
                    #             print("trouver au dessus :", it.group())

                    if line_cpt + 1 < len(data):
                        line_after = data[line_cpt + 1]
                        special_char = re.finditer(r"[0-9]+", line_after)
                        for it in special_char:
                            match_start_index = it.start()
                            match_end_index = it.end()
                            if match_end_index >= start_index and match_start_index <= end_index + 1:
                                result += int(it.group())
                                print("trouver en bas : ", it.group())
            else:
                print("char est :", char)
                number_adj = []
                matchItr = re.finditer(r"[0-9]+", line)
                if not matchItr is None:
                    for it in matchItr:
                        match_start_index = it.start()
                        match_end_index = it.end()
                        if match_end_index == start_index:
                            print("trouver à gauche :", it.group())
                            number_adj.append(int(it.group()))
                        elif match_start_index == end_index + 1:
                            print("trouver à droite :", it.group())
                            number_adj.append(int(it.group()))

                # if line_cpt > 0:
                #     line_after = data[line_cpt - 1]
                #     special_char = re.finditer(r"[0-9]+", line_after)
                #     for it in special_char:
                #         match_start_index = it.start()
                #         match_end_index = it.end()
                #         if match_end_index >= start_index and match_start_index <= end_index + 1:
                #             number_adj.append(int(it.group()))
                #             print("trouver au dessus :", it.group())

                if line_cpt + 1 < len(data):
                    line_after = data[line_cpt + 1]
                    special_char = re.finditer(r"[0-9]+", line_after)
                    for it in special_char:
                        match_start_index = it.start()
                        match_end_index = it.end()
                        if match_end_index >= start_index and match_start_index <= end_index + 1:
                            number_adj.append(int(it.group()))
                            print("trouver en bas : ", it.group())

                res = 1
                for number in number_adj:
                    res *= number
                    print("res =", res)
                result += res

        print(line, "=>", result)
        line_cpt += 1

    return result

# todo initialiser le dictionnaire pour prendre des listes de nombre
# todo multiplier les nombres entre eux à la fin et les ajouter au résultat.
def get_sum_by_digit2(data: list):
    result = 0
    pattern = r"[0-9]+"
    line_cpt = 0
    while line_cpt < len(data):
        current_line = 0
        line = data[line_cpt]
        numbers = re.finditer(pattern, line)
        mul = {}
        print("ligne :", line_cpt + 1)
        for itr in numbers:
            start_index = itr.start()
            end_index = itr.end() - 1
            number = itr.group()
            found = False

            # Regarde à gauche (-1, 0)
            if start_index > 0 and not line[start_index - 1].isdigit() and line[start_index - 1] != ".":
                if line[start_index + 1] == "*":
                    mul[str(line_cpt) + "_" + str(start_index - 1)] = int(number)
                else:
                    current_line += int(number)
                    result += int(number)
                    print("\tnumber :", number, "trouver à gauche.")
                    found = True

            # Regarde à droite (1, 0)
            elif end_index + 1 < len(line) and not line[end_index + 1].isdigit() and line[end_index + 1] != ".":
                if line[end_index + 1] == "*":
                    mul[str(line_cpt) + "_" + str(end_index + 1)] = int(number)
                else:
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
                    if special_char.group() == "*":
                        mul[str(line_cpt - 1) + "_" + str(special_char.span()[0])] = int(number)
                    else:
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
                    if special_char.group() == "*":
                        mul[str(line_cpt + 1) + "_" + str(special_char.span()[0])] = int(number)
                    else:
                        current_line += int(number)
                        result += int(number)
                        print("\tnumber :", number, "trouver en dessous.")

        print(line, "=>", result, ":", current_line)
        line_cpt += 1

    return result



def step2():
    with open(input, "r", encoding="utf-8") as file:
        data = []
        for line in file:
            line = line[:-1]
            data.append(line)

    resultat = get_sum_by_digit2(data)
    print("La réponse de l'étape 2 est :", resultat)


step2()

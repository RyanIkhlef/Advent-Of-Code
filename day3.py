input = "./inputs/day3/step_1"

# To have a = 1, z = 26, A = 27, Z=52 we need to subtract these numbers.
lowercaseConverter = 96
uppercaseConverter = 38


def assign_priority(badge: str):
    if badge.isupper():
        return ord(badge) - uppercaseConverter
    else:
        return ord(badge) - lowercaseConverter


def step1():
    priorities = 0
    with open(input, "r", encoding="utf-8") as file:
        for line in file:
            line_size = len(line)
            first_compartment = line[:line_size // 2]
            second_compartment = line[line_size // 2:line_size - 1]
            already_found = []

            for badge in first_compartment:
                if badge in second_compartment:
                    if badge in already_found:
                        continue
                    priorities += assign_priority(badge)
                    already_found.append(badge)

    print("La réponse de l'étape 1 est :", priorities)


step1()


def step2():
    first = ""
    second = ""
    group = 1
    priorities = 0
    with open(input, "r", encoding="utf-8") as file:
        for line in file:
            line = line[:len(line) - 1]
            if group % 3 == 0:
                for badge in line:
                    if badge in first and badge in second:
                        priorities += assign_priority(badge)
                        break
            elif group % 3 == 1:
                first = line
            else:
                second = line

            group += 1

    print("La réponse de l'étape 2 est :", priorities)


step2()

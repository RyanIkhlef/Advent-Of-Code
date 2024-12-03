import re

input = "./inputs/day1/day1_input"

def read_input():
    with open(input, "r", encoding="utf-8") as file:
        left = []
        right = []
        for line in file:
            line = line[:-1]
            tmp = re.split(" {3}", line)
            left.append(int(tmp[0]))
            right.append(int(tmp[1]))

    return left, right

def step1():
    left, right = read_input()

    distance = 0
    left.sort()
    right.sort()

    for index in range(len(left)):
        distance += abs(right[index] - left[index])

    print("La réponse de l'étape 1 est :", distance)


step1()


def step2():
    read_input()
    left, right = read_input()

    distance = 0

    for index in range(len(left)):
        distance +=  left[index] * right.count(left[index])

    print("La réponse de l'étape 2 est :", distance)


step2()

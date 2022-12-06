input = "./inputs/day1/day1_input"

def step1():
    maxCarry = 0
    currentCarry = 0
    with open(input, "r", encoding="utf-8") as file:
        for line in file:
            if line == "\n":
                if maxCarry < currentCarry:
                    maxCarry = currentCarry
                currentCarry = 0
            else:
                currentCarry += int(line)

    print("La réponse de l'étape 1 est :", maxCarry)

def step2():
    maxCarry = [0, 0, 0]
    currentCarry = 0
    with open(input, "r", encoding="utf-8") as file:
        for line in file:
            if line == "\n":
                if maxCarry[0] < currentCarry:
                    maxCarry[0], maxCarry[1], maxCarry[2] = currentCarry, maxCarry[0], maxCarry[1]
                elif maxCarry[1] < currentCarry:
                    maxCarry[1], maxCarry[2] = currentCarry, maxCarry[1]
                elif maxCarry[2] < currentCarry:
                    maxCarry[2] = currentCarry
                currentCarry = 0
            else:
                currentCarry += int(line)

    print("La réponse de l'étape 2 : \n\tLe top 3 est :", maxCarry,
          "\n\tLa somme du top 3 est :", sum(maxCarry))

step2()
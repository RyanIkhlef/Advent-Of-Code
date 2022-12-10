input = "./inputs/day4/step_1"
def step1():
    total = 0
    with open(input, "r", encoding="utf-8") as file:
        for line in file:
            line = line[:len(line)-1]
            line = line.replace(",", "-")
            bounds = [int(x) for x in line.split("-")]
            if (bounds[0] <= bounds[2] and bounds[1] >= bounds[3]) or (bounds[0] >= bounds[2] and bounds[1] <= bounds[3]):
                total += 1

    print("La réponse de l'étape 1 est :", total)

step1()

def step2():
    total = 0
    with open(input, "r", encoding="utf-8") as file:
        for line in file:
            line = line[:len(line)-1]
            line = line.replace(",", "-")
            bounds = [int(x) for x in line.split("-")]
            firstSeg = range(bounds[0], bounds[1] + 1)
            secondSeg = range(bounds[2], bounds[3] + 1)

            if bounds[0] in secondSeg or bounds[1] in secondSeg \
                    or bounds[2] in firstSeg or bounds[3] in firstSeg:
                total += 1


    print("La réponse de l'étape 2 est :", total)

step2()

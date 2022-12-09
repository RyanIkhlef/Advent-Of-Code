input = "./inputs/day2/step_1"

opponentShapes = {"rock": "A", "paper": "B", "scissors": "C"}
playerShapes = {"rock": "X", "paper": "Y", "scissors": "Z"}


def isDraw(opponent, player):
    return (opponent == opponentShapes["rock"] and player == playerShapes["rock"]) or \
        (opponent == opponentShapes["paper"] and player == playerShapes["paper"]) or \
        (opponent == opponentShapes["scissors"] and player == playerShapes["scissors"])


def iaIsWinner(opponent, player):
    return (opponent == opponentShapes["rock"] and player == playerShapes["scissors"]) or \
        (opponent == opponentShapes["paper"] and player == playerShapes["rock"]) or \
        (opponent == opponentShapes["scissors"] and player == playerShapes["paper"])


def computePoint(opponent, player):
    if player == playerShapes["rock"]:
        point = 1
    elif player == playerShapes["paper"]:
        point = 2
    else:
        point = 3

    if isDraw(opponent, player):
        return 3 + point
    elif iaIsWinner(opponent, player):
        return 0 + point
    return 6 + point


def step1():
    total = 0
    with open(input, "r", encoding="utf-8") as file:
        for line in file:
            line = line.replace("\n", "")
            shapes = line.split(" ")
            total += computePoint(shapes[0], shapes[1])

    print("La réponse de l'étape 1 est :", total)

step1()

def computeShape(opponentShape, strategy):
    if (strategy == "X"):
        if (opponentShape == opponentShapes["rock"]):
            return playerShapes["scissors"]
        elif (opponentShape == opponentShapes["paper"]):
            return playerShapes["rock"]
        else:
            return playerShapes["paper"]
    elif strategy == "Y":
        if (opponentShape == opponentShapes["rock"]):
            return playerShapes["rock"]
        elif (opponentShape == opponentShapes["paper"]):
            return playerShapes["paper"]
        else:
            return playerShapes["scissors"]
    else:
        if (opponentShape == opponentShapes["rock"]):
            return playerShapes["paper"]
        elif (opponentShape == opponentShapes["paper"]):
            return playerShapes["scissors"]
        else:
            return playerShapes["rock"]

def step2():
    total = 0
    with open(input, "r", encoding="utf-8") as file:
        for line in file:
            line = line.replace("\n", "")
            shapes = line.split(" ")
            playerShape = computeShape(shapes[0], shapes[1])
            total += computePoint(shapes[0], playerShape)

    print("La réponse de l'étape 2 est :", total)

step2()
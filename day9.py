input = "./inputs/day9/step_1"

positions = [[0, 0]]


def move_tail(head_tracker: list, tail_tracker: list):
    head_x = head_tracker[0]
    head_y = head_tracker[1]
    tail_x = tail_tracker[0]
    tail_y = tail_tracker[1]
    # Tail is too far on the left
    if head_x - tail_x > 1 and head_y == tail_y:
        tail_tracker[0] += 1
    # Tail is too far on the right
    elif tail_x - head_x > 1 and head_y == tail_y:
        tail_tracker[0] -= 1
    # Tail is too far on the bot
    elif tail_x == head_x and head_y - tail_y > 1:
        tail_tracker[1] += 1
    # Tail is too far on the top
    elif tail_x == head_x and tail_y - head_y > 1:
        tail_tracker[1] -= 1
    # Tail is too far on the diagonal top right
    elif tail_x - head_x == 1 and tail_y - head_y > 1:
        tail_tracker[0] -= 1
        tail_tracker[1] -= 1
    # Tail is too far on the diagonal top left
    elif head_x - tail_x == 1 and tail_y - head_y > 1:
        tail_tracker[0] += 1
        tail_tracker[1] -= 1
    # Tail is too far on the diagonal left top
    elif head_x - tail_x > 1 and tail_y - head_y == 1:
        tail_tracker[0] += 1
        tail_tracker[1] -= 1
    # Tail is too far on the diagonal left bot
    elif head_x - tail_x > 1 and head_y - tail_y == 1:
        tail_tracker[0] += 1
        tail_tracker[1] += 1
    # Tail is too far on the diagonal bot left
    elif head_x - tail_x == 1 and head_y - tail_y > 1:
        tail_tracker[0] += 1
        tail_tracker[1] += 1
    # Tail is too far on the diagonal bot right
    elif tail_x - head_x == 1 and head_y - tail_y > 1:
        tail_tracker[0] -= 1
        tail_tracker[1] += 1
    # Tail is too far on the diagonal right bot
    elif tail_x - head_x > 1 and head_y - tail_y == 1:
        tail_tracker[0] -= 1
        tail_tracker[1] += 1
    # Tail is too far on the diagonal right top
    elif tail_x - head_x > 1 and tail_y - head_y == 1:
        tail_tracker[0] -= 1
        tail_tracker[1] -= 1

    if tail_tracker not in positions:
        positions.append(tail_tracker.copy())

    return tail_tracker


def move_right(head_tracker: list, tail_tracker: list, steps: int):
    for step in range(steps):
        head_tracker[0] += 1
        move_tail(head_tracker, tail_tracker)


def move_left(head_tracker: list, tail_tracker: list, steps: int):
    for step in range(steps):
        head_tracker[0] -= 1
        move_tail(head_tracker, tail_tracker)


def move_up(head_tracker: list, tail_tracker: list, steps: int):
    for step in range(steps):
        head_tracker[1] += 1
        move_tail(head_tracker, tail_tracker)


def move_down(head_tracker: list, tail_tracker: list, steps: int):
    for step in range(steps):
        head_tracker[1] -= 1
        move_tail(head_tracker, tail_tracker)


def step1():
    head_tracker = [0, 0]
    tail_tracker = [0, 0]
    with open(input, "r", encoding="utf-8") as file:
        for line in file:
            line = line[:-1]
            line = line.split(" ")
            direction = line[0]
            steps = int(line[1])

            match direction:
                case "R":
                    move_right(head_tracker, tail_tracker, steps)
                case "L":
                    move_left(head_tracker, tail_tracker, steps)
                case "U":
                    move_up(head_tracker, tail_tracker, steps)
                case "D":
                    move_down(head_tracker, tail_tracker, steps)

    print("La réponse de l'étape 1 est :", len(positions))


step1()


def step2():
    with open(input, "r", encoding="utf-8") as file:
        for line in file:
            line = line[:-1]
            break

    print("La réponse de l'étape 2 est :", "niy")


step2()

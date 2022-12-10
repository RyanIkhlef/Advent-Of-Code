input = "./inputs/day5/step_1"
ship_size = 9


def print_stacks(stacks: list):
    index = 1
    str_stack = ""
    for stack in stacks:
        str_stack += str(index) + " " + str(stack) + "\n"
        index += 1

    return str_stack[:-1]


def move(number: int, from_: int, to: int, stacks: list):
    moved = 0
    while moved < number:
        stacks[to].append(stacks[from_].pop())
        moved += 1


def step1():
    with open(input, "r", encoding="utf-8") as file:
        is_instruction = False
        stacks = [[] for _ in range(ship_size)]

        for line in file:
            line = line[:len(line) - 1]
            try:
                int(line.replace(" ", ""))
                is_instruction = True
            except ValueError:
                if is_instruction:
                    if line == "":
                        for stack in stacks:
                            stack.reverse()
                            while "-" in stack:
                                stack.remove("-")
                        continue

                    line = line.replace("move ", "").replace(" from", "").replace(" to", "")
                    instruction = line.split(" ")
                    instruction = [int(value) for value in instruction]
                    move(instruction[0], instruction[1] - 1, instruction[2] - 1, stacks)

                else:
                    line = line.replace("[", "")
                    line = line.replace("]", "")
                    line = line.replace(" " * 4, "-")
                    line = line.replace(" ", "")

                    for index in range(ship_size):
                        if index >= len(line):
                            stacks[index].append("-")
                        else:
                            stacks[index].append(line[index])
    print("Stack finale :")
    print(print_stacks(stacks))

    top_crates = ""
    for stack in stacks:
        top_crates += str(stack[-1])

    print("La réponse de l'étape 1 est :", top_crates, end="\n\n")


step1()


def move9001(number: int, from_: int, to: int, stacks: list):
    crates_to_move = []
    moved = 0
    while moved < number:
        crates_to_move.append(stacks[from_].pop())
        moved += 1

    crates_to_move.reverse()
    [stacks[to].append(crate) for crate in crates_to_move]


def step2():
    with open(input, "r", encoding="utf-8") as file:
        is_instruction = False
        stacks = [[] for _ in range(ship_size)]

        for line in file:
            line = line[:len(line) - 1]
            try:
                int(line.replace(" ", ""))
                is_instruction = True
            except ValueError:
                if is_instruction:
                    if line == "":
                        for stack in stacks:
                            stack.reverse()
                            while "-" in stack:
                                stack.remove("-")
                        continue

                    line = line.replace("move ", "").replace(" from", "").replace(" to", "")
                    instruction = line.split(" ")
                    instruction = [int(value) for value in instruction]
                    move9001(instruction[0], instruction[1] - 1, instruction[2] - 1, stacks)

                else:
                    line = line.replace("[", "")
                    line = line.replace("]", "")
                    line = line.replace(" " * 4, "-")
                    line = line.replace(" ", "")

                    for index in range(ship_size):
                        if index >= len(line):
                            stacks[index].append("-")
                        else:
                            stacks[index].append(line[index])
    print("Stack finale :")
    print(print_stacks(stacks))

    top_crates = ""
    for stack in stacks:
        top_crates += str(stack[-1])
    print("La réponse de l'étape 2 est :", top_crates)


step2()

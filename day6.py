input = "./inputs/day6/step_1"
def step1():
    start_of_packet = 4
    is_found = False
    with open(input, "r", encoding="utf-8") as file:
        for line in file:
            line = line[:-1]
            line_size = len(line)
            index = 0
            while index < line_size:
                marker = line[index:index+start_of_packet]
                for letter in marker:
                    if marker.count(letter) > 1:
                        index += 1
                        is_found = False
                        break
                    is_found = True
                if is_found:
                    start_of_packet += index
                    break


    print("La réponse de l'étape 1 est :", start_of_packet)

step1()

def step2():
    start_of_message = 14
    is_found = False
    with open(input, "r", encoding="utf-8") as file:
        for line in file:
            line = line[:-1]
            line_size = len(line)
            index = 0
            while index < line_size:
                marker = line[index:index+start_of_message]
                for letter in marker:
                    if marker.count(letter) > 1:
                        index += 1
                        is_found = False
                        break
                    is_found = True
                if is_found:
                    start_of_message += index
                    break

    print("La réponse de l'étape 2 est :", start_of_message)

step2()

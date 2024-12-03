input = "./inputs/day2/step_1"


def step1():
    reports = []
    with open(input, "r", encoding="utf-8") as file:
        for line in file:
            line = line[:-1]
            reports.append(line.split())

    number_safe_reports = 0
    for report in reports:
        is_safe = True
        old_distance = None

        for index in range(1, len(report)):
            distance = int(report[index - 1]) - int(report[index])

            if old_distance is not None:
                if (old_distance < 0 < distance) or (old_distance > 0 > distance):
                    is_safe = False
                    break

            old_distance = distance
            if distance == 0 or abs(distance) > 3:
                is_safe = False
                break

        if is_safe:
            number_safe_reports += 1


    print("La réponse de l'étape 1 est :", number_safe_reports)


step1()

def is_valid(report, suppress_allowed = True):
    old_distance = None

    for index in range(1, len(report)):
        distance = int(report[index - 1]) - int(report[index])

        if old_distance is not None:
            if (old_distance < 0 < distance) or (old_distance > 0 > distance):
                if suppress_allowed:
                    return any(is_valid(report[:i] + report[i+1:], False) for i in range(len(report)))
                return False

        old_distance = distance
        if distance == 0 or abs(distance) > 3:
            if suppress_allowed:
                return any(is_valid(report[:i] + report[i+1:], False) for i in range(len(report)))
            return False

    return True


def step2():
    reports = []
    with open(input, "r", encoding="utf-8") as file:
        for line in file:
            line = line[:-1]
            reports.append(line.split())

    number_safe_reports = 0
    for report in reports:
        if is_valid(report):
            number_safe_reports += 1

    print("La réponse de l'étape 2 est :", number_safe_reports)


step2()

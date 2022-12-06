# import re
input = "./inputs/day1/day1_input"


def read_line(line: str):
    first_digit_pos = 0
    first_digit = None
    for char in line:
        if char.isdigit():
            first_digit = int(char)
            first_digit_pos = line.index(char)
            break
        continue

    for char in line[:first_digit_pos:-1]:
        if char.isdigit():
            return first_digit * 10 + int(char)
        continue

    return first_digit * 10 + first_digit


def step1():
    with open(input, "r", encoding="utf-8") as file:
        result = 0
        for line in file:
            line = line[:-1]
            digit = read_line(line)
            result += digit

    print("La réponse de l'étape 1 est :", result)


# step1()


def get_digit(digit: str):
    if digit.isdigit():
        return int(digit)

    match digit:
        case "one":
            return 1
        case "two":
            return 2
        case "three":
            return 3
        case "four":
            return 4
        case "five":
            return 5
        case "six":
            return 6
        case "seven":
            return 7
        case "eight":
            return 8
        case "nine":
            return 9
    return None


# def step2():
#     pattern = r'[0-9]|one|two|three|four|five|six|seven|eight|nine'
#     result = 0
#     with open(input, "r", encoding="utf-8") as file:
#         for line in file:
#             line = line[:-1]
#             print("line =", line)
#             digits = re.findall(pattern, line)
#             print("digits =", digits)
#             first_digit = get_digit(digits[0]) * 10
#             print("first  =", first_digit)
#             last_digit = get_digit(digits[-1])
#             print("last digit =", last_digit)
#
#             result += first_digit + last_digit
#
#     print("La réponse de l'étape 2 est :", result)


def step2():
    listChar = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
                "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    result = 0
    with open(input, "r", encoding="utf-8") as file:
        for line in file:
            line = line[:-1]
            first_digit_index = len(line)
            last_digit_index = 0
            first_digit = None
            last_digit = None
            for number in listChar:
                index = line.find(number)
                if index >= 0 and index <= first_digit_index:
                    first_digit_index = index
                    first_digit = get_digit(number) * 10
                index = line.rfind(number)
                if index >= 0 and index >= last_digit_index:
                    last_digit_index = index
                    last_digit = get_digit(number)

            if last_digit is None:
                last_digit = first_digit

            result += first_digit + last_digit

    print("La réponse de l'étape 2 est :", result)


step2()

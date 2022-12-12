input = "./inputs/day8/step_1"


# 1 2 3 4
# 5 6 7 8
# 9 a b c
# d e f g

def compute_visible(grid: list):
    row_size = len(grid)
    column_size = len(grid[0])
    visible = ((row_size + column_size) * 2) - 4  # Trees in the bord row + column * 2 - 4 corners counted 2 times

    for index_row in range(1, row_size - 1):
        for index_column in range(1, column_size - 1):
            tree = grid[index_row][index_column]
            trees_left = grid[index_row][:index_column]
            trees_right = grid[index_row][index_column + 1:]

            trees_top = []
            row_top = grid[:index_row]
            row_top_size = len(row_top)
            for index in range(row_top_size):
                trees_top.append(row_top[index][index_column])

            trees_bot = []
            row_bot = grid[index_row + 1:]
            row_bot_size = len(row_bot)
            for index in range(row_bot_size):
                trees_bot.append(row_bot[index][index_column])

            # print("(" + str(index_row) + "," + str(index_column) + ")", tree, end=" | ")

            if tree > max(trees_left) or tree > max(trees_right) or tree > max(trees_top) or tree > max(trees_bot):
                # print(max(trees_left), max(trees_right), max(trees_top), max(trees_bot), "| visible")
                visible += 1
                continue

            # print(max(trees_left), max(trees_right), max(trees_top), max(trees_bot), "| invisible")

    return visible


def step1():
    grid = []
    with open(input, "r", encoding="utf-8") as file:
        for line in file:
            line = line[:-1]
            row = []
            for tree in line:
                row.append(int(tree))

            grid.append(row)

    print("La réponse de l'étape 1 est :", compute_visible(grid))


step1()


def compute_scenic_of_direction(grid: list, tall: int):
    scenic = 0

    for tree in grid:
        scenic += 1
        if tree >= tall:
            break

    return scenic


def compute_scenic(grid: list):
    row_size = len(grid)
    column_size = len(grid[0])
    highest_scenic = 0

    for index_row in range(1, row_size - 1):
        for index_column in range(1, column_size - 1):
            tree = grid[index_row][index_column]
            trees_left = grid[index_row][:index_column]
            trees_left.reverse()
            trees_right = grid[index_row][index_column + 1:]

            trees_top = []
            row_top = grid[:index_row]
            row_top_size = len(row_top)
            for index in range(row_top_size):
                trees_top.append(row_top[index][index_column])

            trees_top.reverse()

            trees_bot = []
            row_bot = grid[index_row + 1:]
            row_bot_size = len(row_bot)
            for index in range(row_bot_size):
                trees_bot.append(row_bot[index][index_column])

            current_scenic = compute_scenic_of_direction(trees_left, tree) \
                             * compute_scenic_of_direction(trees_right, tree) \
                             * compute_scenic_of_direction(trees_top, tree) \
                             * compute_scenic_of_direction(trees_bot, tree)

            if current_scenic > highest_scenic:
                highest_scenic = current_scenic

    return highest_scenic


def step2():
    grid = []
    with open(input, "r", encoding="utf-8") as file:
        for line in file:
            line = line[:-1]
            row = []
            for tree in line:
                row.append(int(tree))

            grid.append(row)

    print("La réponse de l'étape 2 est :", compute_scenic(grid))


step2()

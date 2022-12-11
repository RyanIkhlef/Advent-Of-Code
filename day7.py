input = "./inputs/day7/step_1"

# {
#   "/": {parent : none, size: 0 },
#   "/a": {parent: "/", size: 0},
#   "/a/e": {parent: "/a", size: 0}
# }
file_system = dict()


def compute_parent_dir(current_dir: str):
    current_dir = current_dir.split("/")
    current_dir.pop(-2)
    current_dir = "/".join(current_dir)

    if current_dir == "":
        current_dir = "/"

    return current_dir


def cd(args: str, current_dir: str):
    if args == "..":
        current_dir = compute_parent_dir(current_dir)
    elif args == "/":
        file_system[args] = {"parent": None, "children": [], "size": 0}
    else:
        if not current_dir.endswith("/"):
            current_dir += "/"
        current_dir += args + "/"
        if current_dir not in file_system:
            parent_dir = compute_parent_dir(current_dir)
            file_system[current_dir] = {"parent": parent_dir, "children": [], "size": 0}

    return current_dir


def read_command(command: str, current_dir: str):
    args = command[3:]

    if command.startswith("cd"):
        return cd(args, current_dir)

    return current_dir


def compute_file_size(path: str):
    file = file_system[path]
    children = file["children"]

    for child in children:
        file["size"] += compute_file_size(path + child)

    return file["size"]


def step1():
    current_dir = "/"
    with open(input, "r", encoding="utf-8") as file:
        for line in file:
            line = line[:-1]
            if line.startswith("$"):
                current_dir = read_command(line[2:], current_dir)
            elif line.startswith("dir"):
                file_system[current_dir]["children"].append(line[4:] + "/")
            else:
                line = line.split(" ")
                file_system[current_dir]["size"] += int(line[0])

    compute_file_size("/")

    print("File system :")
    print(file_system)

    total = 0
    for _, file in file_system.items():
        size = file["size"]
        if size < 100000:
            total += size

    print("La réponse de l'étape 1 est :", total)


step1()


def step2():
    total_size = file_system["/"]["size"]
    amount_to_delete = 30000000 - (70000000 - total_size)

    file_to_delete = file_system["/"]
    for _, file in file_system.items():
        if amount_to_delete <= file["size"] < file_to_delete["size"]:
            file_to_delete = file

    print("La réponse de l'étape 2 est :", file_to_delete["size"])


step2()

def print_maze(maze):
    s = ""
    for row in maze:
        for col in row:
            s += str(col)
        s += "\n"
    return s


def has_corners(pos, length):
    y, x = pos

    if x == 0:
        return "Left"
    if x == length[1] - 1:
        return "Right"
    if y == 0:
        return "Up"
    if y == length[0] - 1:
        return "Down"

    return False


def lookup(pos, maze, left=True, up=True, right=True, down=True):
    y, x = pos
    points = []

    if left:
        coords = (y, x - 1)
        if maze[coords[0]][coords[1]] == 0:
            points.append(coords)

    if up:
        coords = (y - 1, x)
        if maze[coords[0]][coords[1]] == 0:
            points.append(coords)

    if right:
        coords = (y, x + 1)
        if maze[coords[0]][coords[1]] == 0:
            points.append(coords)

    if down:
        coords = (y + 1, x)
        if maze[coords[0]][coords[1]] == 0:
            points.append(coords)

    return points


def check_around(pos, maze):
    y, x = pos

    corner = has_corners((y, x), (7, 7))

    points = []

    if corner == "Left":
        points = lookup((y, x), maze, left=False)
    elif corner == "Up":
        points = lookup((y, x), maze, up=False)
    elif corner == "Right":
        points = lookup((y, x), maze, right=False)
    elif corner == "Down":
        points = lookup((y, x), maze, down=False)
    else:
        points = lookup((y, x), maze)

    return points


maze = [
    [0, 0, 0, 0, 1, 1, 1],
    [0, 1, 1, 0, 1, 0, 0],
    [0, 1, 1, 0, 1, 0, 1],
    [0, 1, 1, 0, 1, 0, 1],
    [0, 1, 1, 0, 0, 0, 1],
    [0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
]

initial_pos = (4, 4)
final_pos = (1, 6)


print(check_around(initial_pos, maze))

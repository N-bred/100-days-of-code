import time
import sys
import os


def split_interval(string, interval, rep):
    res = []
    i = 0
    while i <= len(string):
        res.append(string[i : interval + i])
        i += interval
    return rep.join(res)


def print_maze(maze):
    return split_interval(
        "".join([str(c) for r in maze for c in r]), len(maze[0]), "\n"
    )


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
        if maze[y][x - 1] == 0:
            points.append((y, x - 1))

    if up:
        if maze[y - 1][x] == 0:
            points.append((y - 1, x))

    if right:
        if maze[y][x + 1] == 0:
            points.append((y, x + 1))

    if down:

        if maze[y + 1][x] == 0:
            points.append((y + 1, x))

    return points


def check_around(pos, maze):
    corner = has_corners(pos, (len(maze), len(maze[0])))
    points = []

    if corner == "Left":
        points = lookup(pos, maze, left=False)
    elif corner == "Up":
        points = lookup(pos, maze, up=False)
    elif corner == "Right":
        points = lookup(pos, maze, right=False)
    elif corner == "Down":
        points = lookup(pos, maze, down=False)
    else:
        points = lookup(pos, maze)

    return points


def replace_in_line(string, rep, pos, row_length):
    y, x = pos
    index = y * row_length + x + y
    l = list(string)
    l[index] = rep
    return "".join(l)


maze = [
    [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
    [0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1],
    [0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1],
    [0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1],
    [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1],
    [0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1],
]


def main():
    if __name__ == "__main__":
        initial_pos = (5, 0)
        final_pos = (5, 12)
        rep = "-"
        old_pos = initial_pos
        middle_pos = 0
        current_pos = initial_pos

        maze_str = print_maze(maze)
        maze_str = replace_in_line(maze_str, rep, initial_pos, len(maze[0]))

        while current_pos != final_pos:

            print(maze_str)
            time.sleep(0.1)
            os.system("cls")

            middle_pos = current_pos
            current_pos = check_around(current_pos, maze)

            if old_pos in current_pos:
                current_pos.remove(old_pos)
                old_pos = middle_pos

            if len(current_pos) == 1:
                current_pos = current_pos[0]

            maze_str = replace_in_line(maze_str, rep, current_pos, len(maze[0]))

        print(maze_str)


main()

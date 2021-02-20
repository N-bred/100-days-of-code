import random


def generate_random_rgba():
    color = [str(random.randint(0, 255)) for i in range(0, 3)]
    return f"rgba({', '.join(color)}, 1)", color


def convert_rgba_to_hex(color_array):
    hex_color = [hex(int(color))[2:] for color in color_array]
    return "#" + "".join(hex_color)


def generate_random_color(rgba=True, hex_c=True):
    colors = []
    random_rgba = generate_random_rgba()
    colors.append(random_rgba[0])

    if hex_c:
        random_hex = convert_rgba_to_hex(random_rgba[1])
        colors.append(random_hex)

    if rgba is False:
        colors.remove(random_rgba[0])

    return colors


def print_list(l):
    for s in l:
        print(s)


def main():
    if __name__ == "__main__":
        print("Welcome to the Random Color Generator")

        answer = input(
            "Type rgba for only rgba color, hex for only hex color or both for both versions: "
        )

        if answer == "rgba":
            return print_list(generate_random_color(hex_c=False))
        elif answer == "hex":
            return print_list(generate_random_color(rgba=False))
        elif answer == "both":
            return print_list(generate_random_color())
        else:
            return print("Wrong option")


main()
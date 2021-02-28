from pathlib import Path

FILE = "letter.txt"
NAMES = "names.txt"
LETTER_FOLDER = "letters"


def main():
    if __name__ == "__main__":

        with open(NAMES) as names_file:
            names = names_file.readlines()
            names_file.close()

        with open(FILE) as file:
            lines = file.readlines()
            file.close()

        for name in names:
            replaced = "".join(lines).replace("[name]", name)
            output = Path(LETTER_FOLDER, name.strip() + ".txt")
            with open(str(output), "w") as file:
                file.write(replaced)
                file.close()


main()

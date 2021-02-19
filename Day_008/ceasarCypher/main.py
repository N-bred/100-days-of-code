def cypher_encode(string, shift):
    list_str = list(string)
    encoded = []

    for char in list_str:
        if char.isupper():
            encoded.append(chr(((ord(char) + shift - 65) % 26 + 65)))
        else:
            encoded.append(chr(((ord(char) + shift - 97) % 26 + 97)))

    return "".join(encoded)


def cypher_decode(string, shift):
    list_str = list(string)
    decoded = []
    for char in list_str:
        if char.isupper():
            decoded.append(chr(((ord(char) - shift - 65) % 26 + 65)))
        else:
            decoded.append(chr(((ord(char) - shift - 97) % 26 + 97)))

    return "".join(decoded)


def main():
    if __name__ == "__main__":
        print("Welcome to the Caesar's Cypher")
        mode = input(
            "Type 'encode' to encode something, type 'decode' to decode something: "
        )

        if mode == "":
            return

        text = input("Please enter the text to process: ")
        shift = int(input("Please enter the shift number: "))

        if mode == "encode":
            result = cypher_encode(text, shift)
        else:
            result = cypher_decode(text, shift)

        print("Result " + result)

        repeat = input("Do you want to try again? Yes or No: ")

        if repeat.lower() == "yes":
            return main()
        return


main()
def cypher_encode(string, shift):
    list_str = list(string)
    encoded = []

    for char in list_str:
        code = ord(char)
        if 97 <= code <= 122:
            if code + shift > 122:
                code = 96 + shift
            else:
                code += shift
        elif 65 <= code <= 90:
            if code + shift > 90:
                code = 64 + shift
            else:
                code += shift

        encoded.append(chr(code))

    return "".join(encoded)


def cypher_decode(string, shift):
    list_str = list(string)
    decoded = []
    for char in list_str:
        code = ord(char)
        if 97 <= code <= 122:
            if code - shift < 97:
                code = 123 - shift
            else:
                code -= shift
        elif 65 <= code <= 90:
            if code - shift < 65:
                code = 91 - shift
            else:
                code -= shift
        decoded.append(chr(code))
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

        if repeat == "Yes":
            return main()
        return


main()
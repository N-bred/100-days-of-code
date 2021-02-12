
def main():
    if __name__ == "__main__":
        print("Welcome to the Caesar's Cypher")
        mode = input("Type 'encode' to encode something, type 'decode' to decode something: ")

        if mode != "encode" or mode != "decode":
            return print("Bad option")

        text = input("Please enter the text to process: ")
        shift = int(input("Please enter the shift number: "))
        # Call to function

        if mode == "encode":
            print("Encode")
            reult = ""
        else:
            print("Decode")
            result = " "


        print("Result " + result)

main()
def get_input():
    name = input("Type the name of the bidder: ")
    amount = float(input("Enter the amount to bid: $"))
    return name, amount


def get_highest_bid(bids):
    sorted_bids = sorted(bids.items(), key=lambda k: k[1], reverse=True)
    return sorted_bids[0]


def main():
    if __name__ == "__main__":
        print("Welcome to the Hidden Bid Auction")
        bids = {}
        bidding = True
        while bidding:
            name, amount = get_input()
            bids[name] = amount
            again = input("Are there any other bidders? yes or no: ")

            if again == "no":
                bidding = False

        winner_name, bid = get_highest_bid(bids)
        print(f"The winner is: {winner_name} with a bid of ${bid}")


main()
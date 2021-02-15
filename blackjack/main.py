import random

GLOBAL_CARDS = {"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"j":10, "k": 10, "q": 10, "a":1}

def calculate_result(players_cards, cards):
    result = 0
    for n in players_cards:
        if n != "a":
            result += cards[str(n)]
        
        if n == "a":
            if result <= 10:
                result += 11
            elif result <= 20:
                result += 1

    return result


def compute_victory(player_cards, computer_cards, cards, is_skipped=False):
    player_result = calculate_result(player_cards, cards)
    computer_result = calculate_result(computer_cards, cards)

    print(f"Player: {player_cards} - {player_result} | CPU: {computer_cards} - {computer_result}")

    if player_result == 21 and computer_result == 21:
        return "Draw"
    elif player_result == 21 and computer_result != 21:
        return"You win"
    elif computer_result == 21 and player_result != 21:
        return"Computer wins"
    elif player_result > 21 and computer_result < 21:
        return"Computer wins"
    elif computer_result > 21 and player_result < 21:
        return"You win"


    if player_result < 21 and computer_result < 21:
        if is_skipped:
            if player_result > computer_result:
                return "You win"
            else:
                return "Computer wins"

    return False



def pick_a_card(cards):
    picked_card = random.choice(list(cards.keys()))
    cards.pop(picked_card, None)
    return picked_card


def main():
    if __name__ == "__main__":
        print("Welcome to Blackjack, a python game.")
        cards = GLOBAL_CARDS.copy()
        player_cards = []
        computer_cards = []
        is_running = True
        skipped = False

        for n in range(0,2):
            player_cards.append(pick_a_card(cards))
            computer_cards.append(pick_a_card(cards))
        
        while is_running:
            print(f"Your cards: {player_cards}")

            confirmation = input("Type y to get another cards, or n to pass: ")

            if confirmation == 'y':
                player_cards.append(pick_a_card(cards))


            if calculate_result(computer_cards, GLOBAL_CARDS) <= 10:
                computer_cards.append(pick_a_card(cards))

            result = compute_victory(player_cards, computer_cards, GLOBAL_CARDS, skipped)

            


            if confirmation == 'n':
                skipped = True

            if result is not False :
                is_running = False
                return print(result)
            
                


            


main()
import random
import art


def player_deck(player_cards):
    print(f"    current hand : {player_cards}, current score : {sum(player_cards)}")


def dealer_deck(dealer_cards):
    print(f"    Dealers hand : {dealer_cards}, score : {sum(dealer_cards)}")


def result_deck(player_cards, dealer_cards):

    player_total = sum(player_cards)
    dealer_total = sum(dealer_cards)
    if player_total > 21 and 11 in player_cards:
        position = player_cards.index(11)
        player_cards[position] = 1

    if player_total == 21:
        print(f"    You got 21 You win, your cards = {player_cards}")
        dealer_deck(dealer_cards)

    elif dealer_total == 21:
        print(f"    Dealer got 21 dealer wins, dealers cards = {dealer_cards}")
        player_deck(player_cards)

    elif player_total > 21 > dealer_total:
        player_deck(player_cards)
        dealer_deck(dealer_cards)
        print("You crossed 21, DEALER WINS")

    elif player_total < 21 < dealer_total:
        player_deck(player_cards)
        dealer_deck(dealer_cards)
        print("dealer crossed 21, YOU WIN")

    elif player_total > dealer_total:
        player_deck(player_cards)
        dealer_deck(dealer_cards)
        print("YOU WIN")

    else:
        player_deck(player_cards)
        dealer_deck(dealer_cards)
        print("DEALER WINS")


def blackjack():
    print(art.logo)

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    playercards = random.choices(cards, k=2)
    dealercards = random.choices(cards, k=2)

    max_dealer_card = get_max_dealer_card(dealercards)

    print(f"    Your cards : {playercards}, current score : {sum(playercards)}")
    print(f"    Dealers first card: {max_dealer_card}")

    handle_immediate_win(dealercards, playercards)

    handle_draw(dealercards, playercards)

    dealer_draw_till17(cards, dealercards)

    player_play(cards, dealercards, playercards)

    check_play_again()


def player_play(cards, dealercards, playercards):
    should_continue = True
    while should_continue:
        hit = input("Type 'y' to get another card and 'n' to pass : ").lower()

        if hit == 'y':
            playercards.append(random.choice(cards))
            if sum(playercards) >= 21:
                result_deck(playercards, dealercards)
                should_continue = False
            else:
                player_deck(playercards)

        elif hit == 'n':
            result_deck(playercards, dealercards)
            should_continue = False

        else:
            print("invalid input")
            should_continue = False


def dealer_draw_till17(cards, dealercards):
    while sum(dealercards) < 17:
        if sum(dealercards) > 21 and 11 in dealercards:
            position = dealercards.index(11)
            dealercards[position] = 1
        dealercards.append(random.choice(cards))


def handle_draw(dealercards, playercards):
    if sum(dealercards) == 21 and sum(playercards) == 21:
        print(f"    Your final hand : {playercards}, final score : {sum(playercards)}")
        print(f"    Dealers final hand : {dealercards}, final score : {sum(dealercards)}")
        print("DRAW")
        check_play_again()


def handle_immediate_win(dealercards, playercards):
    if sum(playercards) == 21:
        print('    YOU WIN')
        print(f"dealers cards{dealercards}")
        check_play_again()
    elif sum(dealercards) == 21:
        print(f'    DEALER WINS , dealers cards ={dealercards}')
        check_play_again()



def check_play_again():
    yes_no = input("would you like to play blackjack? type 'y' for yes and 'n' for no : ")
    if yes_no == 'y':
        blackjack()
    else:
        print("GOOD GAME, GOOD BYE")


def get_max_dealer_card(dealercards):
    max_dealer_card = 0
    for card in dealercards:
        if card > max_dealer_card:
            max_dealer_card = card
    return max_dealer_card


blackjack()
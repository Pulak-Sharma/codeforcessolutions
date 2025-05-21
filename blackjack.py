import random

def deal_card(num):
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.sample(cards, num)

def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)    
    return sum(cards)

def compare(user, computer):
    if user==computer:
        return "Draw 🙃"
    elif computer==0:
        return "You Lose. Opponent has Blackjack 😢"
    elif user==0:
        return "BLACKJACK! You Win 🥳"
    elif user>21:
        return "You went over. You Lose 😭"
    elif computer>21:
        return "Opponent went over. You Win 🤩"
    elif user>computer:
        return "You Win 😎"
    else:
        return "You Lose ☹️"

def game():
    print("Welcome to Blackjack game")
    print(""" 
     _     _            _     _            _    
    | |__ | | __ _  ___| | __(_) __ _  ___| | __
    | '_ \| |/ _` |/ __| |/ /| |/ _` |/ __| |/ /
    | |_) | | (_| | (__|   < | | (_| | (__|   < 
    |_.__/|_|\__,_|\___|_|\_\| |\__,_|\___|_|\_\\
                             | |
                             /_/                 
    """)
    is_game_over = False
    user_cards = deal_card(2)
    computer_cards = deal_card(1)

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards} , Currnt Score: {user_score}")
        print(f"Computer's cards: {computer_cards}")

        if user_score==0 or computer_score==0 or user_score>21:
            is_game_over = True
        else:
            draw = input("Type 'y' to get another card, type 'n' to pass: ")
            if (draw =='y'):
                user_cards += deal_card(1)
            else:
                is_game_over = True

    while(computer_score != 0 and computer_score<17):
        computer_cards += deal_card(random.randint(0,2))
        computer_score = calculate_score(computer_cards)

    print(f"Your Final Hand: {user_cards} , Final Score: {user_score}")
    print(f"Computer's Final Hand: {computer_cards} , Final Score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Would you like to play a game of Blackjack? Type 'y' or 'n': ")=="y":
    game()
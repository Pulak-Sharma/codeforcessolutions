import random
print("""
     _______  __   __  _______  _______  _______    _______  __   __  _______    __    _  __   __  __   __  _______  _______  ______   
    |       ||  | |  ||       ||       ||       |  |       ||  | |  ||       |  |  |  | ||  | |  ||  |_|  ||  _    ||       ||    _ |  
    |    ___||  | |  ||    ___||  _____||  _____|  |_     _||  |_|  ||    ___|  |   |_| ||  | |  ||       || |_|   ||    ___||   | ||  
    |   | __ |  |_|  ||   |___ | |_____ | |_____     |   |  |       ||   |___   |       ||  |_|  ||       ||       ||   |___ |   |_||_ 
    |   ||  ||       ||    ___||_____  ||_____  |    |   |  |       ||    ___|  |  _    ||       ||       ||  _   | |    ___||    __  |
    |   |_| ||       ||   |___  _____| | _____| |    |   |  |   _   ||   |___   | | |   ||       || ||_|| || |_|   ||   |___ |   |  | |
    |_______||_______||_______||_______||_______|    |___|  |__| |__||_______|  |_|  |__||_______||_|   |_||_______||_______||___|  |_|
                      
""")
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard': ")

NUMBER = random.randint(1, 100)

def compare(num):
    if num<NUMBER:
        print("Too low.\nGuess again.")
    elif num>NUMBER:
        print("Too high.\nGuess again.")
    elif num==NUMBER:
        print(f"You got it!! The answer was {num}")
    
if level=="easy":
    for i in range(10, 0, -1):
        print(f"You have {i} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        compare(guess)
        if guess==NUMBER:
            break

elif level=="hard":
    for i in range(5, 0, -1):
        print(f"You have {i} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        compare(guess)
        if guess==NUMBER:
            break
    

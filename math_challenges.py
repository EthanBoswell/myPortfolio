import random
import math

# Global score
score = 0

# Number Guessing
def play_guessing_game():
    hidden = random.randint(1, 50)
    attempts = 0
    print("\n--- Number Guessing Game ---")
    while True:
        guess = int(input("Enter your guess (1-50): "))
        attempts += 1
        if guess < hidden:
            print("Too low!")
        elif guess > hidden:
            print("Too high!")
        else:
            print(f"Correct! You guessed it in {attempts} tries.")
            global score
            score += 1
            break

# Part 2 – Dice Battle
def announce_winner(player_wins, computer_wins):
    print("\n--- Dice Battle Results ---")
    print(f"Player wins: {player_wins}")
    print(f"Computer wins: {computer_wins}")
    if player_wins > computer_wins:
        print("You are the champion!")
    elif computer_wins > player_wins:
        print("Computer is the champion!")
    else:
        print("It's a tie!")

def play_dice_battle():
    global score
    player_wins = 0
    computer_wins = 0

    print("\n--- Dice Battle Game ---")
    for round_num in range(1, 6):  # Best of 5 rounds
        input(f"\nPress Enter to roll dice for Round {round_num}...")
        player_roll = random.randint(1, 6) + random.randint(1, 6)
        computer_roll = random.randint(1, 6) + random.randint(1, 6)
        print(f"You rolled {player_roll}, Computer rolled {computer_roll}")

        if player_roll > computer_roll:
            print("You win this round!")
            player_wins += 1
            score += 1
        elif computer_roll > player_roll:
            print("Computer wins this round!")
            computer_wins += 1
        else:
            print("This round is a tie!")

    announce_winner(player_wins, computer_wins)

# Part 3 – Final Adventure
def bonus_round():
    print("\n--- Bonus Round ---")
    print("Since your score is high enough, you get a math challenge!")
    choice = input("Choose: (1) Square root or (2) Factorial? ")

    if choice == "1":
        num = int(input("Enter a number: "))
        print(f"√{num} = {math.sqrt(num)}")
    elif choice == "2":
        num = int(input("Enter a number: "))
        print(f"{num}! = {math.factorial(num)}")
    else:
        print("Invalid choice.")

def main():
    global score
    while True:
        print("\n--- Main Menu ---")
        print("1. Play Number Guessing")
        print("2. Play Dice Battle")
        print("3. View Score")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            play_guessing_game()
        elif choice == "2":
            play_dice_battle()
        elif choice == "3":
            print(f"\nYour current score is: {score}")
            if score >= 5:  # threshold for bonus round
                bonus_round()
        elif choice == "4":
            print("Thanks for playing. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()

       

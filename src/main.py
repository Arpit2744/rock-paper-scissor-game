import random

choices = ['rock', 'paper', 'scissors']

def get_computer_choice():
    return random.choice(choices)

def get_user_choice():
    while True:
        user = input("Enter rock, paper, or scissors: ").lower()
        if user in choices:
            return user
        print("Invalid choice! Try again.")

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    print("Welcome to Rock-Paper-Scissors Game!")
    while True:
        user = get_user_choice()
        computer = get_computer_choice()
        print(f"You chose: {user}")
        print(f"Computer chose: {computer}")
        print(determine_winner(user, computer))
        
        again = input("Play again? (y/n): ").lower()
        if again != 'y':
            break

if __name__ == "__main__":
    main()

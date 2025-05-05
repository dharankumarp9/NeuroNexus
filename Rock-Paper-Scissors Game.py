import random

def rock_paper_scissors():
    print("Welcome to Rock, Paper, Scissors!")
    print("Instructions: Type 'rock', 'paper', or 'scissors' to play.")
    
    user_score = 0
    computer_score = 0

    while True:
        choices = ["rock", "paper", "scissors"]
        user_choice = input("\nYour choice (rock/paper/scissors): ").lower()

        if user_choice not in choices:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

      
        if user_choice == computer_choice:
            result = "It's a tie!"
        elif (
            (user_choice == "rock" and computer_choice == "scissors") or
            (user_choice == "paper" and computer_choice == "rock") or
            (user_choice == "scissors" and computer_choice == "paper")
        ):
            result = "You win!"
            user_score += 1
        else:
            result = "You lose!"
            computer_score += 1

        
        print(result)
        print(f"Score - You: {user_score} | Computer: {computer_score}")

      
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing! Final Score:")
            print(f"You: {user_score} | Computer: {computer_score}")
            break

rock_paper_scissors()


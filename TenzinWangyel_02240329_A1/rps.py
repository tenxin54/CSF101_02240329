import random

class RockPaperScissors:
    def __init__(self):
        self.choices = ["rock", "paper", "scissors"]
        self.user_score = 0
        self.computer_score = 0
        self.ties = 0

    def get_computer_choice(self):
        return random.choice(self.choices)

    def get_user_choice(self):
        while True:
            user_input = input("Choose rock, paper, or scissors (or 'quit' to exit): ").lower()
            if user_input in self.choices + ["quit"]:
                return user_input
            print("Invalid choice. Please try again.")

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "tie"
        winning_conditions = {
            "rock": "scissors",
            "paper": "rock",
            "scissors": "paper"
        }
        if winning_conditions[user_choice] == computer_choice:
            return "user"
        else:
            return "computer"

    def update_score(self, result):
        if result == "user":
            self.user_score += 1
        elif result == "computer":
            self.computer_score += 1
        else:
            self.ties += 1

    def display_result(self, user_choice, computer_choice, result):
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        if result == "tie":
            print("It's a tie!")
        elif result == "user":
            print("You win this round!")
        else:
            print("Computer wins this round!")
        print(f"Score - You: {self.user_score}, Computer: {self.computer_score}, Ties: {self.ties}\n")

    def play_round(self):
        user_choice = self.get_user_choice()
        if user_choice == "quit":
            return False
        computer_choice = self.get_computer_choice()
        result = self.determine_winner(user_choice, computer_choice)
        self.update_score(result)
        self.display_result(user_choice, computer_choice, result)
        return True

    def play_game(self):
        print("Welcome to Rock Paper Scissors!")
        while True:
            if not self.play_round():
                break
        print("\nFinal Results:")
        print(f"You won: {self.user_score} times")
        print(f"Computer won: {self.computer_score} times")
        print(f"Ties: {self.ties}")
        if self.user_score > self.computer_score:
            print("Congratulations! You won the game!")
        elif self.computer_score > self.user_score:
            print("Computer won the game. Better luck next time!")
        else:
            print("The game ended in a tie!")

# Start the game
if __name__ == "__main__":
    game = RockPaperScissors()
    game.play_game()
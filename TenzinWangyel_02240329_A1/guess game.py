import random

class GuessNumberGame:
    def __init__(self, lower=1, upper=50):
        self.lower = lower
        self.upper = upper
        self.secret_number = random.randint(lower, upper)
        self.attempts = 0
        self.valid_numbers = set(range(lower, upper + 1))  # Added for score calculation
    
    def get_user_guess(self):
        while True:
            try:
                guess = int(input(f"Pick your lucky number from {self.lower} to {self.upper}: "))
                if self.lower <= guess <= self.upper:
                    return guess
                else:
                    print(f"Please enter a number between {self.lower} and {self.upper}.")
            except ValueError:
                print("Invalid input! Please enter a valid number.")
    
    def check_guess(self, guess):
        self.attempts += 1
        if guess == self.secret_number:
            print(f"CONGRATULATION! Your guess was correct in {self.attempts} attempt(s)!")
            return True
        else:
            print(f"sorry correct number is:{self.secret_number}")
        return False
    
    def calculate_score(self):  # Added this new method
        valid_count = len(self.valid_numbers)
        score = valid_count - self.attempts
        return max(0, score)
    
    def play(self):
        print("Welcome to the Guess Number Game!")
        print(f"I'm thinking of a number between {self.lower} and {self.upper}.")
        
        while True:
            user_guess = self.get_user_guess()
            if self.check_guess(user_guess):
                break
            print("-" * 30)
        
        print(f"The secret number was: {self.secret_number}")
        print(f"Your score: {self.calculate_score()}")  # Added score display
        print("Thanks for playing!")

# Create and play the game
game = GuessNumberGame()
game.play()
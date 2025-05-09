import random

class GameCollection:
    def __init__(self):
        self.scores = {
            'guess_game': 0,
            'rps_game': 0,
            'trivia_game': 0,
            'pokemon_manager': 0
        }
    
    def display_menu(self):
        print("\n=== Game Collection Menu ===")
        print("1. Guess Number Game")
        print("2. Rock Paper Scissors Game")
        print("3. Trivia Pursuit Game")
        print("4. Pokemon Card Binder Manager")
        print("5. Check Overall Scores")
        print("6. Exit Program")
    
    def guess_number_game(self):
        print("\n=== Guess the Number ===")
        lower = 1
        upper = 10
        secret = random.randint(lower, upper)
        attempts = 0
        
        print(f"I'm thinking of a number between {lower} and {upper}.")
        
        while True:
            guess = input("Your guess: ")
            if not guess.isdigit():
                print("Please enter a valid number.")
                continue
                
            guess = int(guess)
            attempts += 1
                
            if guess < lower or guess > upper:
                print(f"Please enter a number between {lower} and {upper}.")
                continue
            
            if guess == secret:
                print(f"Correct! You guessed it in {attempts} attempts!")
                score = (upper - lower + 1) - attempts
                self.scores['guess_game'] = max(0, score)
                print(f"Your score: {self.scores['guess_game']}")
                break
            elif guess < secret:
                print("Too low! Try higher.")
            else:
                print("Too high! Try lower.")
    
    def rock_paper_scissors(self):
        print("\n=== Rock Paper Scissors ===")
        choices = ['rock', 'paper', 'scissors']
        user_wins = 0
        computer_wins = 0
        
        while True:
            user_choice = input("Choose rock, paper, or scissors (or 'quit'): ").lower()
            
            if user_choice == 'quit':
                break
            elif user_choice not in choices:
                print("Invalid choice. Please try again.")
                continue
                
            computer_choice = random.choice(choices)
            print(f"Computer chose: {computer_choice}")
            
            if user_choice == computer_choice:
                print("It's a tie!")
            elif ((user_choice == 'rock' and computer_choice == 'scissors') or
                  (user_choice == 'paper' and computer_choice == 'rock') or
                  (user_choice == 'scissors' and computer_choice == 'paper')):
                print("You win this round!")
                user_wins += 1
            else:
                print("Computer wins this round!")
                computer_wins += 1
                
        self.scores['rps_game'] = user_wins
        print(f"\nFinal Score - You: {user_wins}, Computer: {computer_wins}")
    
    def trivia_game(self):
        print("\n=== Trivia Pursuit ===")
        questions = {
            "Science": [
                {
                    "question": "What is the chemical symbol for water?",
                    "options": ["A. Wo", "B. H2O", "C. Wa", "D. Wt"],
                    "answer": "B"
                },
                {
                    "question": "Which planet is known as the Red Planet?",
                    "options": ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"],
                    "answer": "B"
                }
            ],
            "History": [
                {
                    "question": "Who was the first prime minister of the Bhutan?",
                    "options": ["A. Tshering Tobgay", "B. Jigme Yoezer Thinley", "C. Lotay Tshering ", "D.Sangay Ngedup"],
                    "answer": "B"
                }
            ],
            "Geography": [
                {
                    "question": "Bhutan is located in which mountain range?",
                     "options": ["A. Alps", "B. Andes", "C. Himalayas", "D. Rockies"],
                    "answer": "C"
                },
                {
                    "question": "What percentage of Bhutan is constitutionally required to remain forested?",
                    "options": ["A. 40%", "B. 50%", "C. 60%", "D. 70%"],
                    "answer": "C"
                },
                {
                     "question": "Which country does NOT share a border with Bhutan?",
                     "options": ["A. India", "B. China", "C. Nepal", "D. Bangladesh"],
                     "answer": "D"
                },
            ]
        }
        
        score = 0
        total = 0
        
        for category in questions:
            print(f"\nCategory: {category}")
            for question in questions[category]:
                total += 1
                print("\n" + question["question"])
                for option in question["options"]:
                    print(option)
                
                while True:
                    answer = input("Your answer (A-D): ").upper()
                    if answer in ['A', 'B', 'C', 'D']:
                        break
                    print("Invalid input. Please enter A, B, C, or D.")
                
                if answer == question["answer"]:
                    print("Correct!")
                    score += 1
                else:
                    print(f"Wrong! The correct answer was {question['answer']}.")
        
        self.scores['trivia_game'] = score
        print(f"\nYour trivia score: {score}/{total}")
    
    def show_scores(self):
        print("\n=== Overall Scores ===")
        print(f"Number of correct guess in Guess Number Game: {self.scores['guess_game']}")
        print(f"Wins in Rock Paper Scissors over computer : {self.scores['rps_game']}")
        print(f"Trivia Correct Answers: {self.scores['trivia_game']}")
        print(f"Pokemon Cards Collected: {self.scores['pokemon_manager']}")
    
    def run(self):
        print("Welcome to the Game Collection!")
        
        while True:
            self.display_menu()
            choice = input("Choose from (1-6) so that you can enjoy playing it: ")
            
            if choice == '1':
                self.guess_number_game()
            elif choice == '2':
                self.rock_paper_scissors()
            elif choice == '3':
                self.trivia_game()
            elif choice == '4':
                print("\nRedirecting to Pokemon Card Binder Manager...")
                cards = input("Enter simulated Pokemon cards collected: ")
                if cards.isdigit():
                    self.scores['pokemon_manager'] = int(cards)
                else:
                    print("Invalid input. Using 0 as default.")
                    self.scores['pokemon_manager'] = 0
            elif choice == '5':
                self.show_scores()
            elif choice == '6':
                print("Thank you for your precious time!")
                break
            else:
                print("Wrong choice. Please enter a number from 1-6.")

if __name__ == "__main__":
    games = GameCollection()
    games.run()
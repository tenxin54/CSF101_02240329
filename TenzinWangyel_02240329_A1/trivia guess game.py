import random

class TriviaGame:
    def __init__(self):
        # Simple trivia questions organized by category
        self.categories = {
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
                    "question": "Who was the first president of the United States?",
                    "options": ["A. Thomas Jefferson", "B. George Washington", "C. Abraham Lincoln", "D. John Adams"],
                    "answer": "B"
                },
                {
                    "question": "In which year did World War II end?",
                    "options": ["A. 1943", "B. 1945", "C. 1947", "D. 1950"],
                    "answer": "B"
                }
            ],
            "Geography": [
                {
                    "question": "What is the capital of France?",
                    "options": ["A. London", "B. Berlin", "C. Paris", "D. Madrid"],
                    "answer": "C"
                },
                {
                    "question": "Which country is the largest by area?",
                    "options": ["A. China", "B. Canada", "C. Russia", "D. USA"],
                    "answer": "C"
                }
            ]
        }
        self.score = 0

    def display_categories(self):
        print("\nAvailable Categories:")
        for i, category in enumerate(self.categories.keys(), 1):
            print(f"{i}. {category}")

    def play_quiz(self):
        print("Welcome to Simple Trivia Pursuit!")
        print("You'll answer questions from different categories.")
        
        while True:
            self.display_categories()
            print(f"\nCurrent Score: {self.score}")
            print("Enter the number of the category you want (or '0' to quit):")
            
            try:
                choice = input("Your choice: ")
                if choice == '0':
                    print(f"\nGame Over! Your final score is: {self.score}")
                    break
                
                choice = int(choice)
                if 1 <= choice <= len(self.categories):
                    category = list(self.categories.keys())[choice - 1]
                    self.ask_question(category)
                else:
                    print("Invalid choice. Please enter a number from the list.")
            except ValueError:
                print("Please enter a valid number.")

    def ask_question(self, category):
        # Get a random question from the selected category
        question_data = random.choice(self.categories[category])
        
        print(f"\nCategory: {category}")
        print(question_data["question"])
        for option in question_data["options"]:
            print(option)
        
        while True:
            user_answer = input("Your answer (enter the letter): ").upper()
            if user_answer in ['A', 'B', 'C', 'D']:
                break
            print("Please enter A, B, C, or D")
        
        if user_answer == question_data["answer"]:
            print("Correct! 🎉")
            self.score += 1
        else:
            print(f"Wrong! The correct answer was {question_data['answer']}.")
        
        print(f"Your current score: {self.score}\n")

# Main program
if __name__ == "__main__":
    game = TriviaGame()
    game.play_quiz()
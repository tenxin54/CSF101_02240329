import random
def guess_num():
    print("Guess number game")
    numb = random.randint(1,50)
    guess=0
    
    guess = int(input("Pick your lucky number from 1 to 50:"))
    
    if (guess == numb):
        print("CONGRATULATION! Your guess was correct")
    
    else:
       print(f"Lucky number is: {numb} \nTry your luck next time!")

def rps_game():
    choices=("rock", "paper", "scissors")
    user= None
    ai= random.choice(choices)

    while user not in choices:
        user= input("Your choice from(rock, paper, scissors):")

    print(f"Yours choice:{user}") 
    print(f"AI choice:{ai}")  

    if user == ai:
        print(" It is draw between you and AI")

    elif user == "rock" and ai == "scissors":
        print(" You won over AI")

    elif user == "scissors" and ai == "paper":
        print(" You won over AI")

    elif user == "paper" and ai == "rock":
        print(" You won over AI")

    else:
        print(" You lost over AI")

while True:
    print("""Select your function from 1 - 3:
          1. Guess Number Game
          2. Rock Paper Scissor Game
          3. EXIT programe""")
    option=int(input("Select which game you want to Play:"))

    if option == 1:
        guess_num()

    elif option == 2:
        rps_game()
    
    elif option == 3:
        print("Sad good bye for now but hope to see you soon. THANK YOU! for playing")
        break
    else:
        print("Invalid choice! Please choose correct option.")
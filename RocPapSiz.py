import random

choices = ["rock", "paper", "scissors"]
py_code = random.choice(choices)
# the next line should be commented out as it for testing purposes
print(py_code)
player  = input("Enter: rock, paper or scissors - please check spelling:  ")
print("Your choice " + player + ", Computer choice " + py_code)

if player == py_code:
    print("It's a tie")
elif player == "rock":
    if py_code == "paper":
        print("Paper covers Rock: computer wins")
    else:
        print("Rock breaks Scissors: you win")
elif player == "paper":
    if py_code == "scissors":
        print("Scissors cuts Paper: computer wins")
    else:
        print("Rock wraps Paper: you win")
elif player == "scissors":
    if py_code == "rock":
        print("Rock breaks Scissors: computer wins")
    else:
        print("Scissors cut Paper: you win")

import random

def rock_paper_scissors(computer):
    
    player = str(input("rock, paper, scissors:\n")).lower()

    if player == computer:
        print("Equal")
    elif player == "rock" and computer == "scissors":
        print("You Won! {0} breaks {1}".format(player, computer))
    elif player == "rock" and computer == "paper":
        print("You Lose! {0} covers {1}".format(computer, player))
    elif player == "scissors" and computer == "paper":
        print("You Won! {0} cuts {1}".format(player, computer))
    elif player == "scissors" and computer == "rock":
        print("You Lose! {0} breaks {1}".format(computer, player))
    elif player == "paper" and computer == "rock":
        print("You Won! {0} covers {1}".format(player, computer))
    elif player == "paper" and computer == "scissors":
        print("You Lose! {0} cuts {1}".format(computer, player))
    else:
        print("Wrong!")

count = 0
while count < 10:
    rps = ["rock", "paper", "scissors"]
    computer = random.choice(rps)
    rock_paper_scissors(computer)
    count += 1



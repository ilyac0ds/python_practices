import random
while True:
    try:
        choose = ["rock", "scissors", "paper"]
        player = input(
            "this is ROCK SCISSORS PAPER game\nchoose between \"ROCK\" & \"SCISSORS\" & \"PAPER\" : ")
        win = {
            "rock": "scissors",
            "scissors": "paper",
            "paper": "rock"
        }

        computer = random.choice(choose)
        print(f"computer choose is {computer}")
        if player == computer:
            print("draw")
        elif win[player] == computer:
            print(f"computer : {computer} so you win")
        else:
            print(f"computer : {computer} sorry but you lose")
    except TypeError as e:
        print(f"error : {e}")

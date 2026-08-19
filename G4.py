import random
while True:
    try:
        print("--dice game--\nruls : if your choose and computer choose are same you win else you lose.\neasy right ? ")
        player_guess = int(input("Guess the number between 1 - 6 : "))
        computer_number = random.randint(1, 10)
        if player_guess == computer_number:
            print(
                f"be happy computer choose {computer_number} same as you do -so\n \033[32m\033[1mYOU WIN\033[0m")
        else:
            print(
                f"computer choose {computer_number} there is \033[31m46655\033[0m case that you lose game. but you can try again any time")
    except ValueError as e:
        print(f"error : {e}")

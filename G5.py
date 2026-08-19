import random

while True:
    try:
        print("--heads tails game--")
        flip = input("press \033[1mENTER\033[0m to flip coin")
        coin = random.randint(1, 2)
        if coin == 1:
            print("got \033[32mheads\033[0m")
        else:
            print("got \033[31mtails\033[0m")
    except ValueError as e:
        print(f"error : {e}")

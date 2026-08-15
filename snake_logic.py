import random
import os

snake = [[5, 5]]
food = [random.randint(0, 9), random.randint(0, 9)]
direction = "d"

while True:
    os.system("cls" if os.name == "nt" else "clear")

    for y in range(10):
        for x in range(10):
            if [x, y] == snake[0]:
                print("O", end="")
            elif [x, y] == food:
                print("*", end="")
            else:
                print(".", end="")
        print()

    print("\nW A S D = Move")
    direction = input("Move: ")

    x, y = snake[0]

    if direction == "w":
        y -= 1
    elif direction == "s":
        y += 1
    elif direction == "a":
        x -= 1
    elif direction == "d":
        x += 1

    if x < 0 or x >= 10 or y < 0 or y >= 10:
        print("Game Over!")
        break

    snake.insert(0, [x, y])

    if [x, y] == food:
        food = [random.randint(0, 9), random.randint(0, 9)]
    else:
        snake.pop()

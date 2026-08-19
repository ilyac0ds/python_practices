import random

print("choose number in your mind I'm gona guss it")
number_range_start = int(input("choose start range of number : "))
number_range_end = int(input("choose end range of number : "))

while True:
    number = random.randint(number_range_start, number_range_end)
    print(f"is this your number : {number}")
    confirm = input("yes or no ?")
    if confirm == "yes":
        print("I know it")
        break
    else:
        print("let's try again")

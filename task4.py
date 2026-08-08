def sam():
    n = int(input("enter number : "))
    numbers = []
    
    for i in range(n):
        number = float(input(f"enter number {i} : "))
        numbers.append(number)

    total = sum(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    average = total / n
    
    print(f"sum is {total}")
    print(f"average is {average}")
    print(f"maximum is {maximum}")
    print(f"minimum is {minimum}")

sam()

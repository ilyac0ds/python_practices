while True:
    try:
        print("--this is a calculator--")
        num1, operator, num2 = input("Enter your operation here : ").split()
        num1 = int(num1)
        num2 = int(num2)

        if operator == "+":
            print(f"{num1} + {num2} = {num1 + num2}")
        elif operator == "-":
            print(f"{num1} - {num2} = {num1 - num2}")
        elif operator == "*":
            print(f"{num1} * {num2} = {num1 * num2}")
        elif operator == "/":
            print(f"{num1} / {num2} = {num1 / num2}")
        elif operator == "**":
            print(f"{num1} ^ {num2} = {num1 ** num2}")
        else:
            print(
                f"this operator {operator} is not exist (exist operators : \"+\" & \"-\" & \"*\" & \"/\" & \"**\")")
    except ValueError as e:
        print(f"error : {e}")

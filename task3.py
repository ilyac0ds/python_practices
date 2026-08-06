try:
    inputs = [float(input("Enter score 1 : ")), float(input("Enter score 2 : ")), float(input(
        "Enter score 3 : ")), float(input("Enter score 4 : ")), float(input("Enter score 5 : "))]
    MIN = min(inputs)
    MAX = max(inputs)
    AVG = sum(inputs) / len(inputs)
    variance = sum((x - AVG) ** 2 for x in inputs) / len(inputs)

    print(f"minimum score is : {MIN}")
    print(f"maximum score is : {MAX}")
    print(f"score variance is : {variance}")
    print(f"score averange score is : {AVG}")
except ValueError as e:
    print(f"error : {e}")

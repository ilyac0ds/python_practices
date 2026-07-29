age = int(input("Enter Your Age : "))

if age < 10:
    print("age : Kid")
elif 10 <= age < 18:
    print("age : Teenager")
elif 18 <= age < 40:
    print("age : Adult")
else:
    print("age : Elder")

mid_exam = int(input("enter midterm exam score : "))
final_exam = int(input("enter final exam score : "))

result = (mid_exam + final_exam) // 2

print(f"Averange scores is : {result}")

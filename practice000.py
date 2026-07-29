import math


NAME = "hi im iliya \n there are my py project-practices"
# print("this is just for beinning command")
print(NAME[:12], len(NAME))
# ---------SCAPE SEQUENS & SCAPE CHARECHTER
print("Hi \n Whaaaaaat ? \t W\"TF ? ")

print("----------")
# ---------formatted string

FIRST = "codding"
SEPERATOR = " "
LAST = "is cool"

FULL = f"{FIRST}{SEPERATOR}{LAST}"
print(FULL)

print("----------")
# ---------concating

FULL_CONCAT = FIRST + SEPERATOR + LAST  # CONCAT
print(FULL_CONCAT)

print("----------")
# ---------string methods

NAME0 = "iliya"
NAME1 = "ILIya"
NAME2 = "iliya"
NAME3 = "  iliya  "
NAME4 = "iliya  "
NAME5 = "  iliya"
NAME6 = "iliya"
NAME7 = "iliya"

print(NAME0.upper())
print(NAME1.lower())
print(NAME2.title())
print(NAME3.strip())
print(NAME4.rstrip())
print(NAME5.lstrip())
print(NAME6.find("l"))
print(NAME7.replace("i", "o"))

print("----------")

# ---------operator: in not in
CAR = "lambor"
print("lam" in CAR)
print("lam" not in CAR)

print("----------")

# ---------int,flout,comlex

X = 1  # int
X = 1.3  # float
X = 2 + 3j  # complex

print("----------")

# ---------operator: + - / * ** //

X = 10
Y = 10
print(X+Y)
print(X-Y)
print(X*Y)
print(X/Y)
print(X//Y)
print(X**Y)
print(X % Y)

print("----------")
# ---------ogmented asyment operator

U = 1
U1 = 1
U2 = 1
U = + 10
print(U)
U1 = - 10
print(U1)
U2 *= 10
print(U2)

print("----------")

# ---------integere function

print(math.ceil(2.2))
print(math.floor(2.2))

print("----------")

# ---------transforming functions

input_0 = input("whats your name : ")
# this is dont need to transtorm becuse the input must be string
print(f"hello {input_0}")

input_1 = input("whats your age : ")
print(f"your age is {input_1}")

input_2 = input("type any number to plus 5 : ")
input_2 = int(input_2)
input_3 = input_2 + 5
print(f"{input_2} + 5 = {input_3}")

# تبدیل استرینگ به بولین
print(bool(""))
print(bool(0))
print(bool(None))
# این سه مقدار فالس رو برمیگردونن و هرچیزی به جز این ها مقدار ترو
print(bool("hlkb"))

print("----------")
# ---------comparision operator
number_0 = 1
print(number_0 > 3)  # false
name_0 = "ali"
name_1 = "mohamad"
a = ord('a')
m = ord('m')
print(f"{name_0}(a) = {a} < and {name_1}(m) = {m} is that true ?")
print(name_0 < name_1)

print("----------")

# conditional expression

temperture = 20

if temperture >= 30:
    print("hot")
elif temperture >= 20:
    print("nice")
else:
    print("cold")

print("----------")

# ---------ternary operator
name_2 = "reza"
password = "1234"

message = "welcome" if name_2 == "reza" and password == "1234" else "wrong password or name"
print(message)

print("----------")

# ---------logical operators (and not or)
hi = True
by0 = False
punch = False
print("hi" if hi and punch and by0 else "bye")
print("hi" if hi or punch or by0 else "bye")
print("hi" if not hi or not punch or not by0 else "bye")
print("hi" if not hi and not punch and not by0 else "bye")

print("----------")

# ---------between condition

# simple one
age = 22
if age >= 18 and age <= 65:
    print("age is between 18 and 65")
else:
    print("you are out of age")

# simple two

if 18 <= age <= 65:
    print("age is between 18 and 65")
else:
    print("you are out of age")

# ---------loop

# simple loop
print("----------")

for variable001 in range(4, 10, 3):
    print(f"simple {variable001} \n" * variable001)

# میخواهیم برنامه ای بنویسیم که 3 بار تلاش میکند و اگر این 3 بار موفق بود پیام موفقیت را بنویسد و اگر موفق نشد بنویسد بعد 3 بار تلاش ناموفق عملیات لغو شده است
variable002 = True
for variable002 in range(3):
    print("try")
    if variable002:
        print("succecful")
        break
else:
    print("after 3 try failed the mission failed !")

# loop in in loop

for x in range(4):
    for y in range(2):
        print(f"({x},{y})")

# ---------قابل پیمایش
print("----------")

for variable003 in range(4):
    print(variable003)
for variable004 in "this count the letter":
    print(variable004)
for variable005 in ["car", "pen", "backpack"]:
    print(variable005)

# ---------while

print("----------")

number_1 = 100
while number_1 > 0:
    print(number_1)
    number_1 //= 2
print("done")

print("$$$$$$")

command = ""
while True:
    command = input("please write somthing: ")
    if command.lower() != "exit":
        print(command)
    else:
        print("exiting ...\n done !")
        break

# ---------make function

print("----------")


def fun_name(first_name):
    print(f"hi {first_name}")


fun_name("iliya")


def fuck_name(first_name, last_name):
    return f"hi {first_name} {last_name}"


message_1 = fuck_name("ali", "khan")
print(message_1)
file = open("content.txt", "w")
file.write(message_1)

# ---------keyword argument
print("----------")


def increment(number, by):
    return number + by


print(increment(number=1, by=2))  # keyword argument

# ---------default argument
print("----------")


def sample000(number, by=1, times=1):
    return number * by - times


print(sample000(3))

# ---------*args
print("----------")


def multiply(*numbers0):
    total = 1
    for number in numbers0:
        total *= number
    return total


print(multiply(1, 2, 3, 4, 5, 6, 7, 8, 9))  # whatever you want

# ---------**args
print("----------")


def values(**user):
    print(user)
    print(user["id"])


# print(values(id=1 , name="ali",age=12))
values(id=1, name="ali", age=12)  # aking dictionary

print("----------")
# ---------scop


def greet(name):  # greet is scop of massage_2
    message_2 = "a"  # local varible
    print(message_2)
    print(name)


greet("aliiii")
message_3 = "global"  # global variable #the hole program is scop of this variable
print(message_3)


def sample001(name):
    global message_3
    message_3 = "use that in there"
    print(name)


sample001("yabo")
print(message_3)

# ---------list
print("----------")
List = ["name", "age", "addres"]
Matrix = [[0, 1], [2, 3]]

print(f"list: {List} matrix: {Matrix}")

# to much values

zeros = [0] * 10
print(zeros)

# concating lists

combine = zeros + List + Matrix
print(combine)

sample002 = list(range(21))  # range
chars = list("hi")  # string
print(sample002, chars, chars[:])

letter = ["a", "b", "c", "d"]
print(letter[0], letter[0:2], letter[:2], letter[:], letter[::2], letter[::-1])
# letter[0:2] = 2
# print(letter)#why is that not working?

# list unpaking

numbers = [1, 2, 3, 4, 5]
First, *middel, last = numbers
print(First, *middel, last)

# پیمایش لیست

for letters in letter:
    print(letters)

# enumerate function

for letters in enumerate(letter):
    print(letters)  # the output type is tuple

for index, letters in enumerate(letter):
    print(index, letters)

# add or remove values

numbers.append(4)  # add in to last part
print(numbers)
numbers.insert(3, 2)  # add in to beggining part
print(numbers)
numbers.remove(1)
print(numbers)
numbers.pop()
print(numbers)
resualt = numbers.pop(2)
print(resualt)
numbers.clear()

del numbers[:2]
print(numbers)

# finding index in list
letters0 = ["a", "b", "c", "d"]
print(letters0.index("a"))
print(letters0.count("b"))

# sort list

num = [12, 11, 24, 94, 1]

num.sort()
print(num)
num.sort(reverse=True)
print(f"reverse : {num}")
print(sorted(num))  # dont apply change on basic list

print("without lambda: ")
items = [
    ("product 1", 100),
    ("product 2", 1000),
    ("product 3", 400),
    ("product 4", 200),

]


def sort_items(item8):
    return item8[1]


items.sort(key=sort_items)
print(items)

print("with lambda: ")
# lambda makes codes so better and cleaner
items.sort(key=lambda sort_items: sort_items[1])
for index, item in enumerate(items):
    print(index, item)

print("----------")
# ---------list maping

price = []
for item in items:
    price.append(item[1])
print(price)

# map function
variable006 = list(map(lambda item: item[1], items))
for item in variable006:
    print(item)


# ---------list filtering
price1 = list(filter(lambda item: item[1] >= 150, items))
print(price1)


# ---------list comprehension
# [expression loop(for) item in items]
price2 = [item[1] for item in items]  # خلاصه شده و نسخه تمیز تر مپ کردن
# خلاصه شده و نسخه تمیز تر فیلتر کردن
price3 = [item[1] for item in items if item[1] >= 150]
print(price2, price3)

# ---------zip

list01 = [1, 2, 3]
list02 = [10, 20, 30]

combine01 = list(zip(list01, list02, "abc"))
print(combine01)

# ---------


# ---------


# ---------


# ---------
list00 = []
print(bool(list00))
counter = 0
input_5 = input("enter: ")
while input_5 == " ":
    input_4 = input("g/b: ")
    if input_4 == "g":
        counter += 1
        list00.append(counter)
        print(list00)
    elif input_4 == "b":
        counter -= 1
        list00.pop(counter)
        print(list00)
    elif not list00:
        print("there is no pages left")
    else:
        print("letter not exist!!!")
# +shift+up/down (duplicate)
# ctrl+enter
# alt+up/down

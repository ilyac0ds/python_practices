import random


def mench(player1=str, player2=str, player3=str, player4=str):
    try:
        player1_position = 0
        player2_position = 0
        player3_position = 0
        player4_position = 0

        from_snack = [12, 23, 24, 30, 56, 80, 98]
        to_snack = [1, 15, 3, 25, 40, 60, 2]

        player1_authorization = False
        player2_authorization = False
        player3_authorization = False
        player4_authorization = False

        from_ladders = [13, 50, 81]
        to_ladders = [30, 71, 95]
        while True:
            print(input(f"{player1} press any botton for play : "))
            tas = random.randint(1, 6)
            if player1_position == 0 and tas == 6:
                player1_authorization = True
                print(f"{player1} has six overs. The dice number is {tas}.")

            if not player1_authorization:
                print(f"{player1} You didn't roll a six.")

            if player1_authorization:
                if player1_position + tas <= 100:
                    player1_position = tas + player1_position
                    print(
                        f"tas = {tas} {player1} position >> {player1_position}")

                elif player1_position in from_snack:
                    player_index = from_snack.index(player1_position)
                    player1_position = to_snack[player_index]
                    print(
                        f"{player1} hit by snake. {player1} position >> {player1_position}")

                elif player1_position in from_ladders:
                    player_index = from_ladders.index(player1_position)
                    player1_position = to_ladders[player_index]
                    print(
                        f"{player1} went up the ladder {player1} position >> {player1_position}")

                else:
                    print("you win")
                    player1_authorization = False
                    break

            print(input(f"{player2} press any botton for play : "))
            tas = random.randint(1, 6)
            if player2_position == 0 and tas == 6:
                player2_authorization = True
                print(f"{player2} has six overs. The dice number is {tas}.")

            if not player2_authorization:
                print(f"{player2} You didn't roll a six.")

            if player2_authorization:
                if player2_position + tas <= 100:
                    player2_position = tas + player2_position
                    print(
                        f"tas = {tas} {player2} position >> {player2_position}")

                elif player2_position in from_snack:
                    player_index = from_snack.index(player2_position)
                    player2_position = to_snack[player_index]
                    print(
                        f"{player2} hit by snake. {player2} position >> {player2_position}")

                elif player2_position in from_ladders:
                    player_index = from_ladders.index(player2_position)
                    player2_position = to_ladders[player_index]
                    print(
                        f"player number two went up the ladder player number two position >> {player2_position}")

                else:
                    print("you win")
                    player2_authorization = False
                    break
            print(input(f"{player3} press any botton for play : "))
            tas = random.randint(1, 6)
            if player3_position == 0 and tas == 6:
                player3_authorization = True
                print(f"{player3} has six overs. The dice number is {tas}.")

            if not player3_authorization:
                print(f"{player3} You didn't roll a six.")

            if player3_authorization:
                if player3_position + tas <= 100:
                    player3_position = tas + player3_position
                    print(
                        f"tas = {tas} {player3} position >> {player3_position}")

                elif player3_position in from_snack:
                    player_index = from_snack.index(player3_position)
                    player3_position = to_snack[player_index]
                    print(
                        f"{player1} hit by snake. {player1} position >> {player1_position}")

                elif player3_position in from_ladders:
                    player_index = from_ladders.index(player3_position)
                    player3_position = to_ladders[player_index]
                    print(
                        f"{player3} went up the ladder {player3} position >> {player3_position}")

                else:
                    print("you win")
                    player3_authorization = False
                    break
            print(input(f"{player4} press any botton for play : "))
            tas = random.randint(1, 6)
            if player4_position == 0 and tas == 6:
                player4_authorization = True
                print(f"{player4} has six overs. The dice number is {tas}.")

            if not player1_authorization:
                print(f"{player4} You didn't roll a six.")

            if player4_authorization:
                if player4_position + tas <= 100:
                    player4_position = tas + player4_position
                    print(
                        f"tas = {tas} {player4} position >> {player4_position}")

                elif player4_position in from_snack:
                    player_index = from_snack.index(player4_position)
                    player4_position = to_snack[player_index]
                    print(
                        f"{player4} hit by snake. {player4} position >> {player4_position}")

                elif player4_position in from_ladders:
                    player_index = from_ladders.index(player4_position)
                    player4_position = to_ladders[player_index]
                    print(
                        f"{player4} went up the ladder {player4} position >> {player4_position}")

                else:
                    print("you win")
                    player4_authorization = False
                    break
    except ValueError as e:
        print(f"some error just happend {e}")

player1_name = input("Enter player one name : ")
player2_name = input("Enter player two name : ")
player3_name = input("Enter player three name : ")
player4_name = input("Enter player four name : ")
mench(player1_name,player2_name,player3_name,player4_name)  # flkflkf

"""
Magical door game
"""
import random
import time
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('magical_doors')

WINNERS = SHEET.worksheet('winners')


def invalid():
    print("Answer not valid")


def get_name():
    name = input("Please enter your name to play the game:\n")
    print("Hi", name)
    return name


def player_lost():
        print("You Lost...")
        print("Good Bye!")
        return Lose


def player_won():
    Treasure = input("Gold, Diamond, Platinum : \n ")
    if Treasure in ('Gold', 'Diamond', 'Platinum', 'gold', 'diamond', 'platinum'): # noqa: E501
        print(" Well done", name + " You're the winner!")   # noqa: E501
        print(" Take your treasure to your home and enjoy!!!")   # noqa: E501
        time.sleep(2)
        print(" Hope you enjoyed the game")
        time.sleep(2)
        print(" If you like the game")
        print(" Give thumbs up!!!")
        return Treasure


def game():
    print("Welcome to Magical Door Game")
    print("===========================================")
    # name = input("Please enter your name to play the game:\n")
    # print("Hi", name)
    Answer = (input(" Are you ready to win your tons of treasures behind the magical door?\n Type YES or NO \n:")) 
    if Answer in ('y','YES'): 
        print(" Now you have two options to choose your path right or left,")
        option1 = input(" which path would you like to go? \n Type Right or Left")
        if option1 == "Right":
            print(" This path lead you to the door.")
            time.sleep(2)
            print(" Only way to reach the door and charge the key is to burn the fence")
            time.sleep(2)
            print(" How do you get the fire to burn and charge?")
            time.sleep(2)
            option2 = input(" Dragon fire or match box? \n")
            if option2 in ('dragon fire', 'dragon'):
                print(" Yes you used the dragon fire to burnt the fence and charged the key")
                print(" CONGRATULATIONS you opened the door")
                return player_won
            elif option2 in ('match box', 'match'):
                print(" sorry you lost the game, play again")
                return player_lost
        elif option1 == "Left":
            print("This door leads to river, you swam across and were eaten by an alligators.")
            print("You lost the game")
            return player_lost
    elif Answer in ('n', 'NO'):
        print(" Sorry you missed the treasure to your family, see you next time")
        player_lost()
    else:
        print(" Not a valid option, you lose")
        invalid()

# user = [name, Answer]
# WINNERS.append_row(user)
# results = WINNERS.get_values()


def main():
    # name = get_name()
    result = game()
    # user = [name, result]
    # WINNERS.append_row(user)



if __name__ == "__main__":
    main()

# def main():
#     main()
#     """
#     Run all program functions
#     """
    # name = get_name()
    # update_worksheet(name, "Name")
    # result = game()
    # update_worksheet(result, "Treasure")

# main()
    
    # result = [name, Answer]

    # user = [name, Answer]
    # WINNERS.append_row(user)
    # results = WINNERS.get_values()









# def print_welcome_msg():
#     """
#     Prints a welcome message to the terminal.
#     """
#     print("\n")
#     print("Welcome to the Magical door\n")
#     name = input("Please enter your name to play the game:\n")

#     print("Hi", name)


# print("       Welcome to the Magical door")
# print("                   ((*)) ")
# print("                 ((* * *))    ")
# print("               ((* * * * *))    ")
# print("             ((* * * * * * *))  ")
# print("           ((* * * * * * * * *)) ")
# print("           *         :         * ")
# print("           *         :         * ")
# print("           *    +    :    +    * ")
# print("           *   + +   :   + +   * ")
# print("           *    +    :    +    * ")
# print("           *         :         * ")
# print("           *         :         * ")
# print("           * * * * * * * * * * * ")
# print("           * * * * * * * * * * * ")
# print("           * * * * * * * * * * * ")
# name = input(" Please enter your name to play the game:\n")
# print(" Hi", name)
# print(" Are you ready to win your tons of treasures behind the magical door?\n ")  # noqa: E501
# answer = input(" Type YES or NO: \n ")
# if answer in ('y', 'yes', 'Y', 'Yes'):
#     print(" You are on the dead end of the straight road")
#     time.sleep(2)
#     print(" Now you have two options to choose your path right or left,")
#     answer = input(" which path would you like to go? \n")
#     time.sleep(2)
#     if answer == "right":
#         print(" This path lead you to the enchanted forest.")
#         time.sleep(2)
#         print(" The trees are chanting the mantra,")
#         time.sleep(2)
#         answer = input(" Is that 1.Divine power or 2.Magical power? Type 1 or 2: \n ")  # noqa: E501
#         if answer == "1":
#             print(" You chosen the right option.")
#             time.sleep(2)
#             print(" The portal is opening for you")
#             time.sleep(2)
#             answer = input(" Type 'enter' to enter the portal: \n ")
#             if answer == "enter":
#                 print(" you entered the new world full of magical creatures")
#                 time.sleep(2)
#                 print(" There are two dragons, Blue and white to choose from.")
#                 time.sleep(2)
#                 print(" The dragon will take you a ride to the final destination.")  # noqa: E501
#                 time.sleep(2)
#                 answer = input(" Type 'Blue' or 'White': \n  ")
#                 if answer in ('white', 'White'):
#                     print(" Dragon took you across the seven mountains and seven seas")  # noqa: E501
#                     time.sleep(2)
#                     print(" In the seven seas there is a beautiful gigantic fish.")  # noqa: E501
#                     time.sleep(2)
#                     print(" It has glittering golden scales")
#                     time.sleep(2)
#                     print(" That holds the key for the magic door.")
#                     time.sleep(2)
#                     print(" For Finding the key? ")
#                     time.sleep(2)
#                     answer = input(" Select the option - 1,2,3,4,5,6,7: \n ")
#                     if answer in ('5', '3', '1'):
#                         print(" Hurrah you got the key from the golden fish")
#                         time.sleep(2)
#                         print(" The dragon dropped you in the destination")
#                         time.sleep(2)
#                         print(" Infront of the door there is a sharp wooden fence")  # noqa: E501
#                         time.sleep(2)
#                         print(" If you want to open the door")
#                         time.sleep(2)
#                         print(" you need to charge the key.")
#                         time.sleep(2)
#                         print(" Only way to reach the door")
#                         time.sleep(2)
#                         print(" And charge the key is to burn the fence.")
#                         time.sleep(2)
#                         print(" How do you get the fire to burn and charge?")
#                         time.sleep(2)
#                         answer = input(" Dragon fire or match box? \n")
#                         if answer in ('dragon fire', 'dragon'):
#                             print(" Yes you used the dragon fire")
#                             print(" To burnt the fence and charged the key.")
#                             time.sleep(2)
#                             print(" Now you can open the magical door")
#                             time.sleep(2)
#                             print(" CONGRATULATIONS you opened the door")
#                             time.sleep(2)
#                             print(" There is tons of Gold, Diamond and Platinum")  # noqa: E501
#                             time.sleep(2)
#                             print(" That glitters like a thunderlight")
#                             print(" Which precious item would you like to choose?")  # noqa: E501
#                             time.sleep(2)
#                             answer = input("Gold, Diamond, Platinum : \n ")
#                             if answer in ('Gold', 'Diamond', 'Platinum', 'gold', 'diamond', 'platinum'):   # noqa: E501
#                                 print(" Well done", name + " You're the winner!")   # noqa: E501
#                                 print(" Take your treasure to your home and enjoy!!!")   # noqa: E501
#                                 time.sleep(2)
#                                 print(" Hope you enjoyed the game")
#                                 time.sleep(2)
#                                 print(" If you like the game")
#                                 print(" Give thumbs up!!!")
#                                 answer = input(" Type the number '1' or '2':\n")
#                                 if answer == "1":
#                                     print(" Thanks for your valuable comment")
#                                 elif answer == "2":
#                                     print(" Thanks for your feedback,")
#                             else:
#                                 print("lost")
#                         elif answer in ('match box', 'Match'):
#                             print(" sorry you lost the game, play again")
#                         else:
#                             print(" sorry you lose the game")
#                     elif answer == "2,4,6,7":
#                         print(" sorry you entered the wrong option,")
#                         time.sleep(2)
#                         print(" you lose the game")
#                         time.sleep(2)
#                         print(" Play again to find the treasure, good luck.")
#                     else:
#                         print(" Not a valid option, you lose")
#                 elif answer in ('Blue', 'blue'):
#                     print(" Sorry your answer is wrong, try again")
#                 else:
#                     print(" Not a valid option, you lose")
#         elif answer == "2":
#             print(" The divine holds the magical door")
#             time.sleep(2)
#             print(" you entered the magical world and you lost your memory.")
#             time.sleep(2)
#             print(" you lose the game.")
#             time.sleep(2)
#             print(" Play again to find the treasure, good luck.")
#         else:
#             print(" Not a valid option, you lose")
#     elif answer == "left":
#         print(" you come to the river.")
#         time.sleep(2)
#         print(" you can walk around or you can swim across the river?")
#         time.sleep(2)
#         answer = input(" Type walk/swim: \n ")
#         if answer == "walk":
#             print(" you walked for miles and ran out of water and food,")
#             time.sleep(2)
#             print(" you died out of starving.")
#             time.sleep(2)
#             print(" you lose the game")
#             time.sleep(2)
#             print(" Play again to find the treasure, good luck.")
#         elif answer == "swim":
#             print(" you swam across and were eaten by an alligators.")
#             time.sleep(2)
#             print(" you lose the game. play again")
#             time.sleep(2)
#             print(" Play again to find the treasure, good luck.")
#         else:
#             print(" Not a valid option, you lose")
#     else:
#         print(" Not a valid option, you lose")
# elif answer in ('n', 'no'):
#     print(" Sorry you missed the treasure to your family, see you next time")

# else:
#     print(" Not a valid option, you lose")

# user = [name, answer]
# WINNERS.append_row(user)
# results = WINNERS.get_values()

# # for result in results:
# print(name,  " wins ",  results)


# def get_questions():
#     print("You are on the dead end of the straight road ")
#     print("Now you have two options to choose your path right or left,")
#     print()


# def select_path():
#     path = ""
#     while path != "right" and path != "left":  # input validation
#         path = input("Which path will you choose? (right / left): ")

#     return path


# # def check_path(selected_path):
# #     print("Y")
# #     time.sleep(2)
# #     print("")
# #     time.sleep(2)
# #     print("")
# #     print()
# #     time.sleep(2)

#     correct_Path = random.randint(1, 2)

#     if selected_path == str(correct_Path):
#         print("This path lead you to the enchanted forest.")
#         print("The trees are chanting the mantra,")
#         print()
#     else:
#         print("you come to the river.")
#         print("you can walk around or you can swim across the river?")
#         print()

 
"""
Magical door game
"""
import time
import json
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
creds = json.load(open('creds.json'))
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('magical_door')


# WINNERS = SHEET.worksheet('winners')

# data = winners.get_all_values()

print("Welcome to the Magical door")
name = input("Please enter your name to play the game:\n")
print("Hi", name)
print("Are you ready to win your tons of treasures behind the magical door?\n ")  # noqa: E501
answer = input("Type YES or NO: \n ")
if answer in ('y', 'yes'):
    print("You are on the dead end of the road")
    time.sleep(1)
    print("Now you have two options to choose your path right or left,")
    time.sleep(1)
    answer = input("which path would you like to go? \n")
    time.sleep(1)
    if answer == "right":
        print("This path lead you to the enchanted forest.")
        time.sleep(1)
        print("The trees are chanting the mantra,")
        time.sleep(1)
        answer = input("Is that 1.Divine power or 2.Magical power? Type 1 or 2: \n ")  # noqa: E501
        if answer == "1":
            print("You chosen the right option.")
            time.sleep(1)
            print("The portal is opening for you")
            time.sleep(1)
            answer = input("Type 'enter' to enter the portal: \n ")
            if answer == "enter":
                print("you entered the new world full of magical creatures")
                time.sleep(1)
                print("There are two dragons, Blue and white to choose from.")
                time.sleep(1)
                print("The dragon will take you to a ride to the final destination.")  # noqa: E501
                time.sleep(1)
                answer = input("Type 'Blue' or 'White': \n  ")
                if answer == "white":
                    print("Dragon took you across the seven mountains and seven seas")  # noqa: E501
                    time.sleep(1)
                    print("In the seven seas there is a beautiful gigantic fish.")  # noqa: E501
                    time.sleep(1)
                    print("It has glittering golden scales")
                    time.sleep(1)
                    print("That holds the key for the magic door.")
                    time.sleep(1)
                    print("For Finding the key? ")
                    time.sleep(1)
                    answer = input("Select the option - 1,2,3,4,5,6,7: \n ")
                    if answer in ('5', '3', '1'):
                        print("Hurrah you got the key from the golden fish")
                        time.sleep(1)
                        print("The dragon dropped you in the destination")
                        time.sleep(1)
                        print("Infront of the door there is a sharp wooden fence")  # noqa: E501
                        time.sleep(1)
                        print("If you want to open the door")
                        time.sleep(1)
                        print("you need to charge the key.")
                        time.sleep(1)
                        print("Only way to reach the door")
                        time.sleep(1)
                        print("And charge the key is to burn the fence.")
                        time.sleep(1)
                        print("How do you get the fire to burn and charge?")
                        time.sleep(1)
                        answer = input("Dragon or match box?")
                        if answer == "dragon":
                            print("Yes you use the dragon fire")
                            print("To burnt the fence and charged the key.")
                            time.sleep(1)
                            print("Now you can open the magical door")
                            time.sleep(1)
                            print("Congratulations you opened the door")
                            time.sleep(1)
                            print("There is tons of gold, diamond, silver")
                            time.sleep(1)
                            print("that glitters like a thunderlight")
                            time.sleep(1)
                            print("Well done, you played brillantly")
                            time.sleep(1)
                            print("The winner is", name)
                            print("Hope you enjoyed the game")
                            time.sleep(1)
                            print("If you like the game")
                            print("Give thumbs up!!!")
                            answer = input("By typing the number'1' if not type'2': \n")
                            if answer == "1":
                                print("Thank you for your valuable comment")
                            elif answer == "2":
                                print("Thanks for your feedback,")
                            else:
                                print("Not a valid option")
                        else:
                            print("sorry you lose the game")
                    elif answer == "2,4,6,7":
                        print("sorry you entered the wrong option,")
                        print("you lose the game ")
                    else:
                        print("Not a valid option, you lose")
                elif answer == "Blue":
                    print("Sorry your answer is wrong, try again")
                else:
                    print("Not a valid option, you lose")
        elif answer == "2":
            print("The divine holds the magical door")
            time.sleep(1)
            print("you entered the magical world and you lost your memory.")
            time.sleep(1)
            print("you lose the game.")
        else:
            print("Not a valid option, you lose")
    elif answer == "left":
        print("you come to the river.")
        time.sleep(1)
        print("you can walk around or you can swim across the river?")
        time.sleep(1)
        answer = input("Type walk/swim: \n ")
        if answer == "walk":
            print("you walked for my miles and ran out of water and food,")
            print("you died out of starving.")
        elif answer == "swim":
            print("you swam across and were eaten by an alligators.")
            print("you lose the game.")
            time.sleep(1)
            print("Play again to find the treasure, good luck.")
        else:
            print("Not a valid option, you lose")
    else:
        print("Not a valid option, you lose")
elif answer in ('n', 'no'):
    print("Sorry you missed the treasure to your family, see you next time")

else:
    print("Not a valid option, you lose")

WINNERS = SHEET.worksheet('winners')
user = [name]
WINNERS.append_row(user)
results = WINNERS.get_all_values()

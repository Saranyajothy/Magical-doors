"""
Magical door game
"""
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
        print("The trees are chanting the mantra,")
        answer = input("Is that 1.Divine power or 2.Magical power? Type 1 or 2: \n ")  # noqa: E501
        if answer == "1":
            print("You chosen the right option.")
            print("The portal is opening for you")
            answer = input("Type 'enter' to enter the portal: \n ")
            if answer == "enter":
                print("you entered the new world full of magical creatures")
                print("There are two dragons, Blue and white to choose from.")
                print("The dragon will take you to a ride to the final destination.")  # noqa: E501
                answer = input("Type 'Blue' or 'White': \n  ")
                if answer == "white":
                    print("Dragon took you across the seven mountains and seven seas")  # noqa: E501
                    print("In the seven seas there is a beautiful gigantic fish.")  # noqa: E501
                    print("It has glittering golden scales")
                    print("That holds the key for the magic door.")
                    print("For Finding the key? ")
                    answer = input("Select the option - 1,2,3,4,5,6,7: \n ")
                    if answer in ('5', '3', '1'):
                        print("Hurrah you got the key from the golden fish")
                        print("The dragon dropped you in the destination")
                        print("Infront of the door there is a sharp wooden fence")  # noqa: E501
                        print("If you want to open the door")
                        print("you need to charge the key.")
                        print("Only way to reach the door")
                        print("And charge the key is to burn the fence.")
                        print("How do you get the fire to burn and charge?")  # noqa: E501
                        answer = input("Dragon or match box?")
                        if answer == "dragon":
                            print("You burnt the fence and charged the key.")
                            print("Now the key the  magical power to open the magical door")  # noqa: E501
                            print("Congratulations you opened the door")
                            print("There is tons of gold, diamond, silver")
                            print("that glitters like a thunderlight")
                            print("Well done, you played brillantly")
                            print("The winner is", name)
                            print("Hope you enjoyed the game")
                            print("If you like the game")
                            answer = input("give thumps up by typing the number '1' if not type '2': \n")  # noqa: E501
                            if answer == "1":
                                print("Thank you for your valuable comment")
                            elif answer == "2":
                                print("Thanks for your feedback, we will try to improve the game")  # noqa: E501
                            else:
                                print("Not a valid option")
                        else:
                            print("sorry you lose the game")
                    elif answer == "1,2,3,4,6,7":
                        print("sorry you entered the wrong option, you lose the game ")  # noqa: E501
                    else:
                        print("Not a valid option, you lose")
                elif answer == "Blue":
                    print("Sorry your answer is wrong, try again")
                else:
                    print("Not a valid option, you lose")
        elif answer == "2":
            print("The divine holds the magical door")
            print("you entered the magical world and you lost your memory.")
            print("you lose the game.")
        else:
            print("Not a valid option, you lose")
    elif answer == "left":
        answer = input("you come to the river, you can walk around or you can swim across the river? walk/swim: \n ")  # noqa: E501
        if answer == "walk":
            print("you walked for my miles and ran out of water and food, you died out of starving.")  # noqa: E501
        elif answer == "swim":
            print("you swam across and were eaten by an alligators.")
            print("you lose the game.")
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

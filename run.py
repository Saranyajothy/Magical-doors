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
SHEET = GSPREAD_CLIENT.open('magical_doors')

WINNERS = SHEET.worksheet('winners')


def get_name():
    """
    Enter the name to start the game
    """
    name = input("Please enter your name to play the game:\n")
    return name


def game():
    """
    Question and select the options to open the magical door
    """
    print(" Welcome to Magical Door Game")
    print("==============================")
    print("                   ((*)) ")
    print("                 ((* * *))")
    print("               ((* * * * *))") 
    print("             ((* * * * * * *))") 
    print("           ((* * * * * * * * *)) ")
    print("           *         :         * ")
    print("           *         :         * ")
    print("           *    +    :    +    * ")
    print("           *   + +   :   + +   * ")
    print("           *    +    :    +    * ")
    print("           *         :         * ")
    print("           *         :         * ")
    print("           * * * * * * * * * * * ")
    print("           * * * * * * * * * * * ")
    print("           * * * * * * * * * * * ")
    name = get_name()
    option1 = (input("Hi " + name + " Are you ready to win your tons of treasures behind the magical door?\n Type YES or NO: \n")) 
    if option1 in ('y', 'YES'): 
        print("Now you have two options to choose your path right or left,")
        option2 = input("which path would you like to go?\nType Right or Left \n")
        if option2 in ('right', 'Right', 'RIGHT'):
            print("This path lead you to the door.")
            time.sleep(2)
            print("This path lead you to the enchanted forest.")
            time.sleep(2)
            print("The trees are chanting the mantra,")
            time.sleep(2)
            option4 = input("Is that 1. Divine power or 2. Magical power? Type 1 or 2: \n")
            if option4 == "1":
                print("The portal is opening for you,")
                time.sleep(2)
                print("you entered the new world full of magical creatures")
                time.sleep(2)
                print("Choose one dragon from two that will take you to a ride,")
                time.sleep(2)
                option5 = input("Type 'Blue' or 'White'\n")
                if option5 in ('white', 'WHITE'):
                    print("white dragon took you across the seven mountains and seven seas and dropped you at the desination")
                    time.sleep(2)
                    print("The magical door is surrounded by sharp wooden fence")
                    time.sleep(2)
                    print("Only way to reach the door and charge the key is to burn the fence")
                    time.sleep(2)
                    print("How do you get the fire to burn and charge?")
                    time.sleep(2)
                    option6 = input("Dragon fire or match box? \n")
                    if option6 in ('dragon fire', 'dragon'):
                        print("Yes you used the dragon fire to burnt the fence and charged the key")
                        time.sleep(2)
                        print("CONGRATULATIONS you opened the door")
                        Answer = player_won()
                    elif option6 in ('match box', 'match'):
                        print("sorry you lost the game, play again")
                        Answer = player_lost()
                    else:
                        print("Not a valid option, you lose")
                        invalid()
                elif option5 in ('blue', 'BLUE'):
                    print("sorry you lost the game, play again")
                    Answer = player_lost()
                else:
                    print("Not a valid option, you lose")
                    invalid() 
            elif option4 == "2":
                print("sorry you lost the game, play again")
                Answer = player_lost()
            else:
                print("Not a valid option, you lose")
                invalid()                   
        elif option2 in ('Left', 'left'):
            option7 = input("you come to the river, you can walk around or you can swim across the river? walk/swim: \n")
            if option7 == "walk":
                print("you walked for my miles and ran out of water and food, you died out of starving")
                Answer = player_lost()
            elif option7 == "swim":
                print("you swam across and were eaten by an alligators")
                Answer = player_lost()
            else:
                print("Not a valid option, you lose")
                invalid() 
        else:
            print("Not a valid option, you lose")
            invalid()
    elif option1 in ('n', 'NO'):
        print("Sorry you missed the treasure to your family, see you next time")
        Answer = player_lost()
    else:
        print("Not a valid option, you lose")
        invalid()

    user = [name, Answer]
    WINNERS.append_row(user)
    results = WINNERS.get_values()


def player_lost():
    """
    The result of the loser
    """
    Answer = "Lose"
    print("You Lost...")
    print("Good Bye!")
    return Answer


def player_won():
    """
    once the player opened the door they have the option to choose their treasures
    """
    Answer = input("Choose your treasure: Gold, Diamond, Platinum : \n ")
    if Answer in ('Gold', 'Diamond', 'Platinum', 'gold', 'diamond', 'platinum'): # noqa: E501
        print("Well done, You're the winner!") 
        time.sleep(2)  # noqa: E501
        print("Take your treasure to your home and enjoy!!!")   # noqa: E501
        time.sleep(2)
        print("Hope you enjoyed the game")
        time.sleep(2)
        return Answer


def invalid():
    """
    when the player enter the invalid option
    """
    print("Answer not valid")


def main():
    game()


if __name__ == "__main__":
    main()

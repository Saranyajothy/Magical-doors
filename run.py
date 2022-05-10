"""
Magical door game
"""
import time
# from termcolor import colored
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
SHEET = GSPREAD_CLIENT.open('magical-doors')

WINNERS = SHEET.worksheet('winners')


def get_name():
    """
    Enter the name to start the game
    """
    name = input("> Please enter your name to play the game:\n")
    return name


def game():
    """
    Question and select the options to open the magical door
    # """
    # print(f"{Fore.YELLOW}$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")  # noqa: E501
    # print(f"{Fore.RED} _  _   __    ___  __  ___   __   __      ____   __    __  ____   ")  # noqa: E501
    # print(f"{Fore.MAGENTA}( \/ ) / _\  / __)(  )/ __) / _\ (  )    (    \ /  \  /  \(  _ \  ")  # noqa: E501
    # print(f"{Fore.BLUE}/ \/ \/    \( (_ \ )(( (__ /    \/ (_/\   ) D ((  O )(  O ))   /  ")  # noqa: E501
    # print(f"{Fore.MAGENTA}\_)(_/\_/\_/ \___/(__)\___)\_/\_/\____/  (____/ \__/  \__/(__\_)  ")  # noqa: E501

    # print(f"{Fore.YELLOW}$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")  # noqa: E501

    print("        Welcome to Magical Door Game")
    print("       ==============================")

    print("                    ((*)) ")
    print("                  ((* * *))")
    print("                ((* * * * *))") 
    print("              ((* * * * * * *))") 
    print("            ((* * * * * * * * *)) ")
    print("            *         :         * ")
    print("            *         :         * ")
    print("            *    +    :    +    * ")
    print("            *   + +   :   + +   * ")
    print("            *    +    :    +    * ")
    print("            *         :         * ")
    print("            *         :         * ")
    print("            * * * * * * * * * * * ")
    print("            * * * * * * * * * * * ")
    print("            * * * * * * * * * * * ")
    name = get_name()
    option1 = input("> Hi " + name + "  Are you ready to win your tons of treasures behind the magical door?\nType YES or NO: \n")  # noqa: E501
    if option1 in ('y', 'YES', 'yes', 'Y'):
        print("> Now you have two options to choose your path right or left,")
        option2 = input("> which path would you like to go?\nType Right or Left \n")  # noqa: E501
        if option2 in ('  right', 'Right', 'RIGHT'):
            print("This path lead you to the enchanted forest.")
            time.sleep(2)
            print("The trees are chanting the mantra,")
            time.sleep(2)
            option3 = input("Is that 1. Divine or 2. mundane? Type 1 or 2 : \n")
            if option3 == "  1":
                print("The portal is opening for you,")
                time.sleep(2)
                print("you entered the new world full of magical creatures")
                time.sleep(2)
                print("Choose one dragon from two that will take you to a ride")  # noqa: E501
                time.sleep(2)
                option4 = input("Type 'Red' or 'White'\n")
                if option4 in ('red', 'Red', 'RED'):
                    print("Red dragon took you across the seven mountains and seven seas ")  # noqa: E501
                    time.sleep(2)
                    print("One of the seven seas there is a beautiful gigantic fish with glittering gold scales")  # noqa: E501
                    time.sleep(2)
                    print("That fish holds the key for the magical door.")
                    time.sleep(2)
                    print("Find the fish?")
                    option5 = input("select the option - 1,2,3,4,5,6,7:   \n")
                    if option5 in ('1', '3', '5', '7'):
                        print("Hurrah you got the key")
                        time.sleep(2)
                        print("The magical door is surrounded by sharp wooden fence")  # noqa: E501
                        time.sleep(2)
                        print("Only way to reach the door and charge the key is to burn the fence")  # noqa: E501
                        time.sleep(2)
                        print("How do you get the fire to burn and charge?")
                        time.sleep(2)
                        option6 = input("Dragon fire or match box? \n")
                        if option6 in ('dragon fire', 'dragon', 'DRAGON FIRE' 'DRAGON', 'Dragon'):  # noqa: E501
                            print("Yes you used the dragon fire to burnt the fence and charged the key")  # noqa: E501
                            time.sleep(2)
                            print("CONGRATULATIONS you opened the door")
                            answer = player_won()
                        elif option6 in ('match box', 'match', 'Match', 'MATCH', 'MATCH BOX'):  # noqa: E501
                            print("sorry you lost the game, play again")
                            answer = player_lost()
                        else:
                            print("Not a valid option, you lose")
                            print("Play again")
                            answer = invalid()
                    elif option5 in ('2', '4', '6'): 
                        print("Oops you've chosen the wrong answer")
                        print("sorry you lost the game, play again")
                        answer = player_lost() 
                    else:
                        print("Not a valid option, you lose")
                        print("Play again")
                        answer = invalid()        
                elif option4 in ('red', 'Red', 'RED'):
                    print("Oops you've chosen the wrong answer")
                    print("sorry you lost the game, play again")
                    answer = player_lost()
                else:
                    print("Not a valid option, you lose")
                    print("Play again")
                    answer = invalid()
            elif option3 == "2":
                print("Oops you've chosen the wrong answer")
                print("sorry you lost the game, play again") 
                answer = player_lost()
            else:
                print("Not a valid option, you lose")
                print("Play again")
                answer = invalid()
        elif option2 in ('Left', 'left', 'LEFT'):
            option7 = input("you come to the river, you can walk around or you can swim across the river? walk/swim: \n")  # noqa: E501
            if option7 in ('walk', 'Walk', 'WALK'):
                print("you walked for my miles and ran out of water and food, you died out of starving")  # noqa: E501
                answer = player_lost()
            elif option7 in ('swim', 'Swim', 'SWIM'):
                print("you swam across and were eaten by an alligators")
                print("sorry you lost the game, play again")
                answer = player_lost()
            else:
                print("Not a valid option, you lose")
                print("Play again to win the treasure")
                answer = invalid()
        else:
            print("Not a valid option, you lose")
            print("Play again")
            answer = invalid()
    elif option1 in ('n', 'NO', 'no', 'No'):
        print("Sorry you missed the treasure to your family,")
        print("see you next time")
        answer = player_lost()
    else:
        print("Not a valid option, you lose")
        print("Play again")
        answer = invalid()

    user = [name, answer]
    WINNERS.append_row(user)
    answer = WINNERS.get_values()


def player_lost():
    """
    Assigned the result of the loser
    """
    answer = "Lose"
    return answer


def player_won():
    """
    once the player opened the door they have the option to choose their
    treasures
    """
    answer = input("Choose your treasure: Gold, Diamond, Platinum : \n ")
    if answer in ('Gold', 'Diamond', 'Platinum', 'gold', 'diamond', 'platinum'):  # noqa: E501
        print()
        print("WELL DONE, You're the WINNER!")
        time.sleep(2)
        print("Take your treasure to your home and enjoy!!!")
        time.sleep(2)
        print("Hope you enjoyed the game")
        time.sleep(2)
        return answer


def invalid():
    """
    when the player enter the invalid answer
    """
    answer = "Lose"
    return answer


def main():
    """
    assign the game
    """
    game()


if __name__ == "__main__":
    main()

# colorama.init(autoreset=True)

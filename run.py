import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_PLAYER = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_PLAYER.open('Magical-doors')

# winners = SHEET.worksheet('winners')

# data = winners.get_all_values(

# print(data) 
 
print("Welcome to the Magical door")
name = input("Please enter your name to play the game:  ")
print("Hi", name, "Are you ready to win your tons of treasures behind the magical door?  ")
answer = input("Type YES or NO:  ")
if answer == "yes":
    answer = input("You are on the dead end of the road, now you have two options to choose your path right or left, which path would you like to go?  ")
    if answer == "right":
        answer = input("This path lead you to the enchanted forest. The trees are chanting the mantra, Is that 1. Divine power or 2. Magical power? Type 1 or 2:  ")
        if answer == "1":
            answer = input("you chosen the right option. The portal is opening for you, type 'enter' to enter the portal:  ")
            if answer == "enter":
                print("you entered the new world full of magical creatures")
                answer = input("There are two dragons, Blue and white to choose from. The dragon will take you to a ride to the final destination, type 'Blue' or 'White':   " )
                if answer == "white":
                    print("white dragon took you across the seven mountains and seven seas")
                    answer = input("In the seven seas there is a beautiful gigantic fish with glittering gold scales that holds the key for the magic door. find the key? select the option - 1,2,3,4,5,6,7:  ")
                    if answer == "5":
                        print("Hurrah you got the key from the golden fish and the dragon dropped you in the destination")
                        answer = input("Infront of the door there is a sharp wooden fence and if you want to open the door you need to charge the key. Only way to reach the door and charge the key is to burn the fence. How do you get the fire to burn the fence and charge the key? Guess and Give one word answer:  ")
                        if answer == "dragon":
                            print("you burnt the fence and charged the key. now the key the  magical power to open the magical door")
                            print("congratulations you opened the magical door, there is tons and tons of gold, diamond, silver glitters like thunderlight")
                            print("This precious treasure is all yours, you played brillantly, well done")
                            print("Hope you enjoyed the game")
                            answer = input("If you like the game give thumps up by typing the number '1' if not type '2': ")
                            if answer == "1":
                                print("Thank you for your valuable comment")
                            elif answer == "2":
                                print("Thanks for your feedback, we will try to improve the game")
                            else:
                                print("Not a valid option")
                        else:
                            print("sorry you lose the game")    
                    elif answer == "1,2,3,4,6,7":
                            print("sorry you entered the wrong option, you lose the game ")
                    else:
                        print("Not a valid option, you lose")
                elif answer == "Blue":
                    print("")
                else:  
                    print("Not a valid option, you lose")        
        elif answer == "2":
             print("you entered the magical world and you lost memory, you lose the game. The divine holds the magical door")
        else:  
            print("Not a valid option, you lose")  
    elif answer == "left":
        answer = input("you come to the river, you can walk around or you can swim across the river? walk/swim: ")
        if answer == "walk":
            print("you walked for my miles and ran out of water and food, you died out of starving")
        elif answer == "swim":
            print("you swam across and were eaten by an alligators")
            print("you lose the game")
            print("Play again to find the treasure")
        else:
            print("Not a valid option, you lose")    
    else: 
        print("Not a valid option, you lose")     
elif answer == "no":
    print("Sorry you missed the treasure to your family, see you next time")

else: 
    print("Not a valid option, you lose")  



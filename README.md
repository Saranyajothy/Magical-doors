# Magical door
Magical door is a Python terminal game. Magical door is an interactive game with an objective to guide the player to navigate through a path to identify hidden treasures. This game is suitable for all age groups and its tests the players’ aptitude, intelligence and a tiny bit of luck.

The player gets through a magical door by entering their name and the game greets the player with interactive questions and options. The options selected by the player determine the players’ luck to stay in the game and to navigate through the path to either become a winner or to loose. For every option chosen, the player will be informed about what to expect in their route.

[click here to view the site](https://magical-doors.herokuapp.com/)
# Table of contents
- [User Experience](#user-experience)
- [How to play](#how-to-play)
    - [User's journey](#user's-journey)
- [Website Structure](#website-structure)
    - [Features](#features)
- [Testing](#testing)
    - [Code validation](#code-Validation)
    - [Manual testing](#manual-testing)
    - [Bug fixing](#bug-fixing)
- [Technology Used](#technology-Used)
- [Deployment](#deployment)
- [Credits](#credits)
- [Acknowledgement](#acknowledgement)
____

# User experience
### First Time Visitor Goals
As a First Time User, I want to explore the game. I can see at the very beginning, the game is called Magical Door and it interacts with me with written sentences on the screen.
As a First Time User, I want to understand how to play the game. After typing in my name, the game interacts with my name which is good to address the player during the game, and gives me options to choose upon how I wish to play the game. I know exactly what is expected of me, what I need to do to get the treasure in this game, and how I can navigate through it.
As a First Time User, I will get an experience of what to expect with the options chosen. The game also explains what they could experience with the options they have chosen.
As a First Time User, I want feedback on whether I have chosen the best option to stay in the game and to navigate through different stages or section. The game communicates with me at every stage and explains me what is on the route.  
As a First Time User, I want to know how to become a winner and navigate through each section to become a winner at the end and to get the treasure of the game Magical door.
As a First Time User, I want to be communicated with the progress I made at every stage of the game, it tells me if I have cleared the stage and gives me an appropriate message for each occasion. I want to know, if I have lost or won the game.
### Returning / Frequent Visitor Goals
As a Returning / Frequent Visitor, I want to be able to play the game again and to learn the best options to stay in the game and to learn how to win.

# How to play
The player will be greeted with a message “welcome to Magical Door Game”. The game prompts the player to enter his/her name.  
- A player starts to play Magical door by typing their name and they will be greeted and given two options to proceed with the game, Yes or No.

- The game won’t proceed if the player chooses the option “No”.

- If the player agrees to play by typing “Yes”, it gives further two options to select a path, Right or left.

- If the player chooses, “Right”,

- The path to the “Right” will lead to enchanted forest and gives some more descriptions. It asks the player whether the Mantras chanted are 1. Divine or 2.Mundane. If they choose Mundane, they lose the game.

- If they choose, Divine, they will proceed to next level, which will open the portal to enter the new magical world with full of magical creatures.

- The game gives further two options to choose between red or white dragon to take a ride to magical road. If the choose White Dragon, they are out of the game.

- If they choose Red Dragon, it will take the player across seven mountains and seven seas. One of the seven seas has a beautiful giant fish with glittering gold scales which hold the key for magical door. They player will be given seven options, such as numbers 1 to 7 and the odd numbers will get a key, which needs to be charged to proceed to next level. If they choose even numbers, they lose the game.

- The magical door has sharp wooden fence. The player needs to burn the fence and also needs to charge it with fire. The player is now given options to choose between, Dragon’s fire or match box.

- If the player choose, Match box they will lose the game. If they choose, dragon fire they can burn the fence and also charge the key.

- As the key is charged, they player can open the door and will get the options to choose from Gold, Diamond and Platinum as a treasure.

- The player can choose their desired treasure as their prize.

- If the player chooses, “Left”,

- The path to the “Left” will lead to a river and they play need to choose between the options to swim or walk around.

- If they choose to walk around, they will be left with no water and food, so eventually they will die.

- If they choose to swim, they will be eaten by Aligator.

- This means, the path to the “Left” is not the road to win the treasure.

# Features

## Existing Features

The game is designed to enter a magical door and to navigate through some options to get the treasure. During this navigation, they might lose or win.  
- Screenshot of Game introduction
[!start](/readme-images/start.png)
- Screenshot of player choosing path to the “Right” and choose the right option and win.
[!winner](/readme-images/winner.png) 
- screensjot of the player the lose the game.
[!loser](/readme-images/loser.png)
- enter invalid option
[!validate](/readme-images/validate.png) 
- Screenshot of the google sheet with player's details update.
[!sheet](/readme-images/sheet.png)
## Future Features

- To add interactive voice.
- To make the game more adventurous and interesting options to explore.


# Code validation
## Validator Testing

### PEP8
[!pep8](/readme-images/pep8.png)
- Errors were detected and resolved
- Line length errors detected and resolved
- Line breaks after operators/operands detected and resolved
### python syntac checker
[!python-syntax](/readme-images/python-syntax.png)
- No Errors or warnings detected

## Manual testing
Manual testing was carried out in addition to automated process.
## Bug fixing
#### Issues

![bug1](/readme-images/bug1.png)
  fixed the problem in the google sheet update.

# Technology Used
- Python- To create Multiple choice question.
- GitPod- is an open source platform for ready-to-code and automated.
- GitHub- to save and host the project to run.
- Heroku- used for deployment the app.
- Python Tutor - to check how the Python code behaves in each line.
- Google Sheet- To store name and winner details of the player.
- Google Cloud Platform- for activating API Credentials.

# Deployment
- Deploying the app to heroku
 Type the below details in gitpod terminal.
1. Login to heroku and enter your details.
 command: heroku login -i

2. Get your app name from heroku.
command: heroku apps

3. Set the heroku remote. (Replace app_name with your actual app name)
command: ﻿heroku git:remote -a app_name

4. Add, commit and push to githubcommand: git add . && git commit -m "Deploy to Heroku via CLI"

5. Push to both github and heroku
command: git push origin main
command: git push heroku main

MFA/2FA enabled?
1. Click on Account Settings (under the avatar menu)
2. Scroll down to the API Key section and click Reveal. Copy the key.
3. Enter the command: heroku_config , and enter your api key you copied when prompted
4. Complete the steps above, if you see an input box at the top middle of the editor...
 a. enter your heroku username
 b. enter the api key you just copied

### Need to deploy again?
You should just be able to add, commit and push, and if prompted enter your username and api key again.

# Credits

- I got alot of information from Google, W3 School and Youtube for this project.

- I like to give credits to the Love sanwinch project by Code Institute and it is a wonderful resource for budding developers.

- My sincere thanks to my classmate 'Rhiannon' and special thanks to 'kavitha' for helping me in critical situation1.
 
# Acknowledgement

I would like to thank my mentor Brian and my tutors Kasia for their support feedback and guidance when needed.
I would like to thank the students of Code Institute and Slack Community for sharing the open discussion from various students.
I got alot of information from Google, W3 School and Youtube for this project.
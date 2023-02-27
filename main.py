#######################
#Game Title: "Hotel Meetup"
#Setting: Hotel in Harrisonbrug, first floor
#Game Summary: 
#   You are with the baseball team in the hotel lobby 
#   The coach texted asking to meet at his room for a meeting in 13 mins
#   He also says to bring him towels on the way up
#   Your team goes to the pool to grab towels
#   Once you grab the towels you head to his room before the 13 mins
#Global Variables: 
#   minutes (starts at 0 and increases by at least 1 every move. game ends at 13)
#   havetowels (boolean, starts as false and becomes True when you pick up the towels)
########################

################
#Import Modules
################
import calendar
import os
import time

################
#Define Functions
################
def check_time():
    os.system('clear')
    global minutes
    minutes = minutes + 1
    if minutes >= 13:
        late()
    else:
        print("Coach wants you in", 13 - minutes, "minutes")

def late():
    global day, minutes, havetowels
    print("You didnt get to coach before the 13 minutes")
    if day < 5:
        again = input("Restart? Say yes or no\n")
        if again.lower() == "yes":
            day = day + 1
            minutes = 0
            havetowels = False
            towelhand = False
            start()
        else:
            print("\nGood luck next time")

def start():
    global day
    os.system('clear')
    print("Happy", calendar.day_name[day], "!")
    print("\nYour baseball coach just texed us asking to meet him at his room in 13 minutes")
    print("\nYour standing in the hotel lobby with your teammates")
    move = input("\nWhere would you like to go? Say one of these choices:\n\toutside\n\tarcade\n\thallway\n\trec center\n\tstay here\n")
    if move.lower() == "outside":
        outside()
    elif move.lower() == "arcade":
        arcade()
    elif move.lower() == "hallway":
        hallway()
    elif move.lower() == "rec center":
        recCenter()
    elif move.lower() == "stay here":
        lobby()
    else:
        print("\nsorry, I don't understand your input. I'll assume you want to stay here")
        time.sleep(1)
        lobby()

def outside():
    check_time()
    print("\nThere is a massive thunderstorm outside you cant go outside it is too dangerous")
    input("\nPress enter to go back.")
    lobby()

def arcade():
    check_time()
    print("\nyou play some games with you baseball team and have \nlots of fun!")
    move = input("\nWhat would you like to do next? Say one of these choices:\n\tlobby\n\tstay here\n")
    if move.lower() == "lobby":
        lobby()
    elif move.lower() == "stay here":
        arcade()
    else:
        print("\nsorry, I don't understand your input. I'll assume you want to stay here")
        time.sleep(2)
        arcade()
    
def hallway():
    check_time()
    print("you have entered the hallway to the rooms. There looks like a endless amount of rooms")
    move = input("\nWhere would you like to go next? Say one of these choices:\n\tbathroom\n\tcoaches room\n\tlobby\n")
    if move.lower() == "lobby":
        lobby()
    elif move.lower() == "bathroom":
        bathroom()
    elif move.lower() == "coaches room":
        coach()
    else:
        print("\nsorry, I don't understand your input. I'll assume you want to stay here")
        time.sleep(2)
        hallway()

def coach():
    global havetowels, towelhand
    check_time()

    if not havetowels:
        print("\nThe coach cant start his meeting until he has a towel")
        print("\nYou know that the pool will have towels for him. So we have to go to the pool before the time is up")
        input("\nPress enter to go back out to the hallway")
        havetowels = True
        hallway()
    elif havetowels and not towelhand:
        print("\nThe coach is waiting why are you still here")
        input("\nPress enter to go back out to the hallway")
        hallway()
    else:
        print("You hand coach his towel.")
        time.sleep(2)
        print("The coach is happy that he can dry himself off from the rain")
        time.sleep(2)
        print("He is now happy and starts his team meeting")
        print("Congrats, you dont have to run now at next practice")

def bathroom():
    global minutes
    check_time()
    print("")
    print("\nYou are now in the bathroom. Your whole team is in the bathroom.")
    print("\nThey start to joke around and splash water")
    move = input("\nDo you want to join them? Say yes or no\n")
    if move.lower() == "yes":
        print("\nyou join in on the water fight")
        print("\nyou forgot about the towel and loose track of time")
        time.sleep(2)
        print("...")
        time.sleep(2)
        print("...")
        time.sleep(2)
        print("\nhow long have the team been here?")
        time.sleep(2)
        minutes = minutes + 5
        bathroom()
    elif move.lower() == "no":
        print("\nYou try to leave but everyone calls you a coaches kid")
        print("\nYou dont want that knick name so you go back in the bathroom")
        print("\nyou start throwing water and lose track of time")
        time.sleep(2)
        print("...")
        time.sleep(2)
        print("...")
        time.sleep(2)
        print("whoa, how long have we been here?")
        time.sleep(2)
        print("you turn around and the team leaves")
        time.sleep(1)
        minutes = minutes + 5
        hallway()
   
def recCenter():
    check_time()
    move = input("you have entered the rec center. There are many things to do here. Say one of these choices:\n\tpool\n\tgym\n\tlobby\n")
    if move.lower() == "pool":
        pool()
    elif move.lower() == "gym":
        gym()
    elif move.lower() == "lobby":
        lobby()
    else:
        print("sorry, I don't understand your input. I'll assume you want to chill here for a bit")
        time.sleep(1)
        recCenter()
  
def pool():
    global minutes
    global havetowels
    global towelhand
    check_time()
    if not havetowels:
        print("Welcome to the pool said the lifegaurd.")
    elif havetowels and not towelhand:
        print("You ask the lifegaurd where the towel are")
        print("He walks over to the rack and hands you a towel")
        towelhand = True
        print("What would you like to do next?")
    else:
        print("The coach is waiting in his room and your just standing here where would you like go")

    move = input("Say one of these choices:\n\tget in the pool\n\tGet in the hot tub\n\tleave\n")
    if move.lower() == "hop in the pool":
        print("You just in the pool with your team and loose track of the time")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("...")
        input("Press enter to continue")
        minutes = minutes + 5
        pool()
    elif move.lower() == "get in the hot tub":
        print("you sit in the hot tub and relax")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("...")
        input("Press enter to continue")
        minutes = minutes + 5
        pool()
    elif move.lower() == "leave":
        hallway()
    else:
        print("sorry, I don't understand your input. I'll assume you want to chill here for a bit")
        time.sleep(1)
        pool()

def gym():
    check_time()
    print("You need an adult to go in the gym with you said the \nreceptionist ")
    input("Press enter to go back.")
    hallway()

def lobby():
    check_time()
    print("You are in lobby.")
    move = input("Where would you like to go? Say one of these choices:\n\toutside\n\tarcade\n\thallway\n\trec center \n\tlobby\n")
    if move.lower() == "outside":
        outside()
    elif move.lower() == "arcade":
        arcade()
    elif move.lower() == "hallway":
        hallway()
    elif move.lower() == "rec center":
        recCenter()
    elif move.lower() == "lobby":
        lobby()
    else:
        print("sorry, I don't understand your input. I'll assume you want to stay in the lobby")
        time.sleep(1)
        lobby()

################
#Main
################
havetowels = False
towelhand = False
day = 0
minutes = 0
start()
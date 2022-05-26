from asyncio import wait_for
from tkinter import END
import os, sys
clear = lambda: os.system('cls')
print(" \u001b[34m  ______ __       ____   ______   ______  __  __   ____      _  __    ______   ______   ____")
print("\u001b[34m  / ____// /      /  _/  / ____/  / ____/ / / / /  /   |     / | / /  / ____/  / ____/  / __ \ ")
print("\u001b[34m / /    / /       / /   / /_     / /_    / /_/ /  / /| |    /  |/ /  / / __   / __/    / /_/ /")
print("\u001b[36m/ /___ / /___   _/ /   / __/    / __/   / __  /  / ___ |   / /|  /  / /_/ /  / /___   / _, _/")
print("\u001b[36m\____ /_____/  /___/  /_/      /_/     /_/ /_/  /_/  |_|  /_/ |_/   \____/  /_____/  /_/ |_| Version 0.2")
print("\u001b[36m")
print("Your ship went down due to hitting an iceberg, you managed to get to land using")
print("the ships life-raft. Your mission is to get to a safe point to be rescued...")
print("  \u001b[37m   ")
name = "dwayne"
name = (input("Please enter name?"))
print(f"Welcome {name}")

health = 100
#global variable

def main():
    global health
    print("\u001b[31m")
    ("")
    print(f"You have {health} health.")
    print("    \u001b[37m            ")
    print("you arrived at the foot of a large mountain, that you must climb!")
    print("\u001b[32m")
    print("Press 1 for left, press 2 for right.")
    print("\u001b[37m")
    path = input(f">> ")

    if path == "1":
        left()
    elif path == "3":
        bonus()
    elif path == "2":
        right()
    else: 
        print("\u001b[31m")
        print("Incorrect selection!")
        print("\u001b[37m")
        main()

#//////BONUS///////
def bonus():
    global health
    print("\u001b[34m")
    print("IF YOU SMELLLLLL, WHAT THE ROCK IS COOKING!")
    print("Dwayne, 'The Rock' Johnson falls from the top of the mountain and kills you")
    health -= 100
    print(f"You have {health} health.")
    print("\u001b[35m")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠛⠛⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⠋⠈⠀⠀⠀⠀⠐⠺⣖⢄⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⡏⢀⡆⠀⠀⠀⢋⣭⣽⡚⢮⣲⠆⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⡇⡼⠀⠀⠀⠀⠈⠻⣅⣨⠇⠈⠀⠰⣀⣀⣀⡀⠀⢸⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⡇⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣟⢷⣶⠶⣃⢀⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⡅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⠀⠈⠓⠚⢸⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⢀⡠⠀⡄⣀⠀⠀⠀⢻⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠐⠉⠀⠀⠙⠉⠀⠠⡶⣸⠁⠀⣠⣿⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⣦⡆⠀⠐⠒⠢⢤⣀⡰⠁⠇⠈⠘⢶⣿⣿⣿⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠠⣄⣉⣙⡉⠓⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣀⣀⠀⣀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
    main()
#//////BONUS///////    
def left():
    print("\u001b[36m")
    print("You turned left")
    path_split()

def right():
    print("\u001b[36m")
    print("You turned right")
    print("\u001b[34m")
    safehouse()

def path_split():
    print("You have come to a split on the mountain...")
    print("There seems to be a way UP and a way DOWN...")
    print("    \u001b[32m                              ")
    print("Please press 1 for UP or 2 for DOWN")
    print("\u001b[37m")
    path = input(f">> ")

    if path == "1":
        up1()
    elif path == "2":
        down1()
    else:
        print("\u001b[31m")
        print("Incorrect selection!")
        print("\u001b[36m")
        path_split()
        
def up1():
    print("\u001b[36m")
    print("You climbed up...")
    print("\u001b[32m")
    print("You see a safehouse, don't give up now!")
    print("\u001b[37m")
    safehouse()
    
def down1():
    global health
    print("\u001b[31m")
    print("You climbed down...")
    print("Oh no, a mountain goat hits you, knocking you unconcious")
    print("You recover but you end up back at the split in the path...")
    print("You lose 10 health...")
    health -= 10
    print(f"You have {health} health.")
    print("\u001b[37m")
        
    if health == 80:
        print("Being knocked unconcious seems to have damaged your brain")
        main()
    elif health == 0:
        print("  \u001b[36m  ")
        print("\u001b[34m   ▄████     ▄▄▄          ███▄ ▄███▓   ▓█████        ▒█████      ██▒   █▓   ▓█████     ██▀███  ")
        print("\u001b[34m  ██▒ ▀█▒   ▒████▄       ▓██▒▀█▀ ██▒   ▓█   ▀       ▒██▒  ██▒   ▓██░   █▒   ▓█   ▀     ▓██ ▒ ██▒")
        print("\u001b[34m ▒██░▄▄▄░   ▒██  ▀█▄     ▓██    ▓██░   ▒███         ▒██░  ██▒    ▓██  █▒░   ▒███       ▓██ ░▄█ ▒")
        print("\u001b[36m ░▓█  ██▓   ░██▄▄▄▄██    ▒██    ▒██    ▒▓█  ▄       ▒██   ██░     ▒██ █░░   ▒▓█  ▄     ▒██▀▀█▄  ")
        print("\u001b[36m ░▒▓███▀▒    ▓█   ▓██▒   ▒██▒   ░██▒   ░▒████▒      ░ ████▓▒░      ▒▀█░     ░▒████▒   ░██▓ ▒██▒")
        print("\u001b[36m ░▒   ▒     ▒▒   ▓▒█░   ░ ▒░   ░  ░   ░░ ▒░ ░      ░ ▒░▒░▒░       ░ ▐░     ░░ ▒░ ░    ░ ▒▓ ░▒▓░")
        print("\u001b[36m  ░   ░      ▒   ▒▒ ░   ░  ░      ░    ░ ░  ░        ░ ▒ ▒░       ░ ░░      ░ ░  ░     ░▒ ░ ▒░")
        print("\u001b[36m░ ░   ░      ░   ▒      ░      ░         ░         ░ ░ ░ ▒          ░░        ░        ░░   ░ ")
        print("       ░          ░  ░          ░         ░  ░          ░ ░           ░        ░  ░      ░     ")
        print("                                                                    ░                         ")
        print("\u001b[31m")
        print("Too many attempts tried, you will be returned to the start")
        main()

    else:
        path_split()
        # Behaviour is tempromental!!!         

def safehouse():
    print("\u001b[37m")
    print("Please select 1 for UP or 2 for DOWN")
    path = input(f">> ")

    if path == "1":
        up2()
    elif path == "2":
        down2()
    else:
        print("\u001b[31m")
        print("Please select correct input")
        print("\u001b[37m")
        safehouse()

def up2():
    print("  \u001b[36m  ")
    print("\u001b[34m   ▄████     ▄▄▄          ███▄ ▄███▓   ▓█████        ▒█████      ██▒   █▓   ▓█████     ██▀███  ")
    print("\u001b[34m  ██▒ ▀█▒   ▒████▄       ▓██▒▀█▀ ██▒   ▓█   ▀       ▒██▒  ██▒   ▓██░   █▒   ▓█   ▀     ▓██ ▒ ██▒")
    print("\u001b[34m ▒██░▄▄▄░   ▒██  ▀█▄     ▓██    ▓██░   ▒███         ▒██░  ██▒    ▓██  █▒░   ▒███       ▓██ ░▄█ ▒")
    print("\u001b[36m ░▓█  ██▓   ░██▄▄▄▄██    ▒██    ▒██    ▒▓█  ▄       ▒██   ██░     ▒██ █░░   ▒▓█  ▄     ▒██▀▀█▄  ")
    print("\u001b[36m ░▒▓███▀▒    ▓█   ▓██▒   ▒██▒   ░██▒   ░▒████▒      ░ ████▓▒░      ▒▀█░     ░▒████▒   ░██▓ ▒██▒")
    print("\u001b[36m ░▒   ▒     ▒▒   ▓▒█░   ░ ▒░   ░  ░   ░░ ▒░ ░      ░ ▒░▒░▒░       ░ ▐░     ░░ ▒░ ░    ░ ▒▓ ░▒▓░")
    print("\u001b[36m  ░   ░      ▒   ▒▒ ░   ░  ░      ░    ░ ░  ░        ░ ▒ ▒░       ░ ░░      ░ ░  ░     ░▒ ░ ▒░")
    print("\u001b[36m░ ░   ░      ░   ▒      ░      ░         ░         ░ ░ ░ ▒          ░░        ░        ░░   ░ ")
    print("       ░          ░  ░          ░         ░  ░          ░ ░           ░        ░  ░      ░     ")
    print("                                                                    ░                         ")
    print("\u001b[31m")
    print("You freeze to death...")
    print("YOU DIED...")
    print("")
    print("You respawn at the base of the mountain")
    main()
    

def down2():
    print("\u001b[32m")
    print("Congratulations, you've reached the safehouse!")
    print("...Thats strange! ...it looks abandoned")
    print("Your going to have to continue on foot...")
    print("     \u001b[37m        ")
    event_1()

def event_1_yes():
    print("\u001b[32m")
    print("You push yourself leading through the undergrowth and threw the small hidden pathway. However, the undergrowth was a home to many aggressive snakes which bit at your ankles as you pass.")
    global health
    health -= 8
    print("\u001b[31m")
    print("You have taken 8 DMG.")
    print(f"You now have {health} HP.")
    print("\u001b[37m")
    event_3()

# Ignore Shortcut
def event_1_no():
    print("\u001b[32m")
    print("You ignore the pathway and continue on your journey.")
    print("\u001b[37m")
    event_2()
# Death by Falling
def event_2_1():
    print("You press yourself against the cliff face and slowing begin to shimmy across. Unfortunately, you slip and fall. Your fall is briefly broken by one of the stepping stones in the stream. The strong current whisks you down stream and over the cliff, plummeting you to your death.")
    print("  \u001b[36m  ")
    print("\u001b[34m   ▄████     ▄▄▄          ███▄ ▄███▓   ▓█████        ▒█████      ██▒   █▓   ▓█████     ██▀███  ")
    print("\u001b[34m  ██▒ ▀█▒   ▒████▄       ▓██▒▀█▀ ██▒   ▓█   ▀       ▒██▒  ██▒   ▓██░   █▒   ▓█   ▀     ▓██ ▒ ██▒")
    print("\u001b[34m ▒██░▄▄▄░   ▒██  ▀█▄     ▓██    ▓██░   ▒███         ▒██░  ██▒    ▓██  █▒░   ▒███       ▓██ ░▄█ ▒")
    print("\u001b[36m ░▓█  ██▓   ░██▄▄▄▄██    ▒██    ▒██    ▒▓█  ▄       ▒██   ██░     ▒██ █░░   ▒▓█  ▄     ▒██▀▀█▄  ")
    print("\u001b[36m ░▒▓███▀▒    ▓█   ▓██▒   ▒██▒   ░██▒   ░▒████▒      ░ ████▓▒░      ▒▀█░     ░▒████▒   ░██▓ ▒██▒")
    print("\u001b[36m ░▒   ▒     ▒▒   ▓▒█░   ░ ▒░   ░  ░   ░░ ▒░ ░      ░ ▒░▒░▒░       ░ ▐░     ░░ ▒░ ░    ░ ▒▓ ░▒▓░")
    print("\u001b[36m  ░   ░      ▒   ▒▒ ░   ░  ░      ░    ░ ░  ░        ░ ▒ ▒░       ░ ░░      ░ ░  ░     ░▒ ░ ▒░")
    print("\u001b[36m░ ░   ░      ░   ▒      ░      ░         ░         ░ ░ ░ ▒          ░░        ░        ░░   ░ ")
    print("       ░          ░  ░          ░         ░  ░          ░ ░           ░        ░  ░      ░     ")
    print("                                                                    ░                         ")
    print("\u001b[31m")
    print("You Died. Game Over.")
# Death by Strong Current
def event_2_2_jump():
    print("You decide to jump before it's too late. The strong current catches you as you jump and you are send flying down stream and off the edge of the mountain.")
    print("  \u001b[36m   ")
    print("  \u001b[36m  ")
    print("\u001b[34m   ▄████     ▄▄▄          ███▄ ▄███▓   ▓█████        ▒█████      ██▒   █▓   ▓█████     ██▀███  ")
    print("\u001b[34m  ██▒ ▀█▒   ▒████▄       ▓██▒▀█▀ ██▒   ▓█   ▀       ▒██▒  ██▒   ▓██░   █▒   ▓█   ▀     ▓██ ▒ ██▒")
    print("\u001b[34m ▒██░▄▄▄░   ▒██  ▀█▄     ▓██    ▓██░   ▒███         ▒██░  ██▒    ▓██  █▒░   ▒███       ▓██ ░▄█ ▒")
    print("\u001b[36m ░▓█  ██▓   ░██▄▄▄▄██    ▒██    ▒██    ▒▓█  ▄       ▒██   ██░     ▒██ █░░   ▒▓█  ▄     ▒██▀▀█▄  ")
    print("\u001b[36m ░▒▓███▀▒    ▓█   ▓██▒   ▒██▒   ░██▒   ░▒████▒      ░ ████▓▒░      ▒▀█░     ░▒████▒   ░██▓ ▒██▒")
    print("\u001b[36m ░▒   ▒     ▒▒   ▓▒█░   ░ ▒░   ░  ░   ░░ ▒░ ░      ░ ▒░▒░▒░       ░ ▐░     ░░ ▒░ ░    ░ ▒▓ ░▒▓░")
    print("\u001b[36m  ░   ░      ▒   ▒▒ ░   ░  ░      ░    ░ ░  ░        ░ ▒ ▒░       ░ ░░      ░ ░  ░     ░▒ ░ ▒░")
    print("\u001b[36m░ ░   ░      ░   ▒      ░      ░         ░         ░ ░ ░ ▒          ░░        ░        ░░   ░ ")
    print("       ░          ░  ░          ░         ░  ░          ░ ░           ░        ░  ░      ░     ")
    print("                                                                    ░                         ")
    print("\u001b[31m")
    print("You Died. Game Over.")
# Death by Bear
def event_3_run():
    print("\u001b[32m")
    print("You burst into a full sprint away from the bear and the bear puts up chase. I shouldnt have to explain how this one ends.")
    print(" \u001b[36m    ")
    print("  \u001b[36m  ")
    print("\u001b[34m   ▄████     ▄▄▄          ███▄ ▄███▓   ▓█████        ▒█████      ██▒   █▓   ▓█████     ██▀███  ")
    print("\u001b[34m  ██▒ ▀█▒   ▒████▄       ▓██▒▀█▀ ██▒   ▓█   ▀       ▒██▒  ██▒   ▓██░   █▒   ▓█   ▀     ▓██ ▒ ██▒")
    print("\u001b[34m ▒██░▄▄▄░   ▒██  ▀█▄     ▓██    ▓██░   ▒███         ▒██░  ██▒    ▓██  █▒░   ▒███       ▓██ ░▄█ ▒")
    print("\u001b[36m ░▓█  ██▓   ░██▄▄▄▄██    ▒██    ▒██    ▒▓█  ▄       ▒██   ██░     ▒██ █░░   ▒▓█  ▄     ▒██▀▀█▄  ")
    print("\u001b[36m ░▒▓███▀▒    ▓█   ▓██▒   ▒██▒   ░██▒   ░▒████▒      ░ ████▓▒░      ▒▀█░     ░▒████▒   ░██▓ ▒██▒")
    print("\u001b[36m ░▒   ▒     ▒▒   ▓▒█░   ░ ▒░   ░  ░   ░░ ▒░ ░      ░ ▒░▒░▒░       ░ ▐░     ░░ ▒░ ░    ░ ▒▓ ░▒▓░")
    print("\u001b[36m  ░   ░      ▒   ▒▒ ░   ░  ░      ░    ░ ░  ░        ░ ▒ ▒░       ░ ░░      ░ ░  ░     ░▒ ░ ▒░")
    print("\u001b[36m  ░ ░   ░      ░   ▒      ░      ░         ░         ░ ░ ░ ▒          ░░        ░        ░░   ░ ")
    print("            ░          ░  ░          ░         ░  ░          ░ ░           ░        ░  ░      ░     ")
    print("                                                                    ░                         ")
    print("\u001b[31m")
    print("You Died. Game Over.")                                                                       
# Survive Strong Current
def event_2_2_wait():
    print("\u001b[32m")
    print("You wait for the current to die down before continuing. The strong current crashes against the stepping stones and you hold on for dear life. Soon the current begins to die down and you can cross safely, dispite being somewhat wet now.")
    print("\u001b[37m")
    event_3()
# Survive Bear
def event_3_liedown():
    print("\u001b[32m")
    print("You lie down on the ground for a while. Eventually the bear loses interest and walks away.")
    print("\u001b[37m")
    ending_k()
# Event 2.2: Strong Current
def event_2_2():
    print("\u001b[36m")
    print("You take a deep breath and leap onto the first stepping stone safely. As you managed to reach the halfway point across the stream, you feel the current becoming more powerful.")
    print("(1) Wait")
    print ("(2) Jump to next stepping stone")
    print("\u001b[37m")
    answer2_2 = input(">> ")
    if answer2_2 == "1":
        event_2_2_wait()
    elif answer2_2 == "2":
        event_2_2_jump()
    else:
        print("\u001b[31m")
        print("Please select a valid input")
        print("\u001b[36m")
        event_2_2()
# First Event: The Shortcut
def event_1():
    print("\u001b[36m")
    print("You find a shortcut through the forest thick with undergrowth. The pathway is obscured but you think you can make it through. Do you take the shortcut?")
    print("(1) Yes, Take shortcut.")
    print ("(2) No, Stick to the normal path.")
    answer1 = input(">> ")
    if answer1 == "1":
        event_1_yes()
    elif answer1 == "2":
        event_1_no()
    else:
        print("\u001b[31m")
        print("Invalid response. Please try again.")
        print("\u001b[37m")
        event_1()
# Second Event: Stepping Stones across stream
def event_2():
    print("\u001b[32m")
    print("You continue down the path as it gradually becomes more and more tretcherous, eventually leading you to the edge of a waterfall. As it blocks your only way forward, you have no choice but to go through it.")
    print("(1) Shimmy across the cliff face underneath the waterfall.")
    print ("(2) Cross the stepping stone path.")
    answer2 = input(">> ")
    if answer2 == "1":
        event_2_1()
    elif answer2 == "2":
        event_2_2()
    else:
        print("\u001b[31m")
        print("Invalid response. Please try again.")
        event_2()
def event_3():
    print("\u001b[36m")
    print("You come to a clearing near the top of the mountain. The harsh rocky ground is now covering with soft green grass. You walk across the clearing with no obsticles in sight. It is then you notice you are being watched by a bear not to far away.")
    print("(1) Lie Down.")
    print ("(2) RUN!")
    answer_3 = input(">> ")
    if answer_3 == "1":
        event_3_liedown()
    elif answer_3 == "2":
        event_3_run()
    else:
        print("\u001b[31m")
        print("Please select a valid input")
        print("\u001b[36m")
        event_3()
def ending_k():
    print("\u001b[34m")
    print("Suddenly a rescue helicopter roars over head. Leaves scatter and the grass flattens around you. The pilot has seen you in the open and is landing to pick you up. Soon you will we warm and dry and able to put this all behind you...")
    print("\u001b[36m")
    print("\u001b[36m   ███             ▄█    █▄            ▄████████         ▄████████      ███▄▄▄▄        ████████▄  ")
    print("\u001b[36m▀█████████▄       ███    ███          ███    ███        ███    ███      ███▀▀▀██▄      ███   ▀███ ")
    print("\u001b[36m  ▀███▀▀██        ███    ███          ███    █▀         ███    █▀       ███   ███      ███    ███ ")
    print("\u001b[36m   ███   ▀       ▄███▄▄▄▄███▄▄       ▄███▄▄▄           ▄███▄▄▄          ███   ███      ███    ███ ")
    print("\u001b[34m   ███          ▀▀███▀▀▀▀███▀       ▀▀███▀▀▀          ▀▀███▀▀▀          ███   ███      ███    ███ ")
    print("\u001b[34m   ███            ███    ███          ███    █▄         ███    █▄       ███   ███      ███    ███ ")
    print("\u001b[34m   ███            ███    ███          ███    ███        ███    ███      ███   ███      ███   ▄███ ")
    print("\u001b[34m  ▄████▀          ███    █▀           ██████████        ██████████       ▀█   █▀       ████████▀  ")
    print("    \u001b[37m                                                                                                ")
  
main()




        



      











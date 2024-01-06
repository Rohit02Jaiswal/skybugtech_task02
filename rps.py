import random

print("---------------------Welcome to Rock Paper Scissor----------------------")

# Taking Variable.................
user_score = 0
computer_score = 0
ties = 0

name = input("Enter Your Name: ")
print("""
Winning Rules:
____________________________________________________________________________________
1. Rock beat Scissor
2. Scissor beat Paper
3. Paper beat Rock
------------------------------------------------------------------------------------
""")

print("""Choises are: 
Choose 1 for Rock
Choose 2 for Paper
Choose 3 for Scissor
-------------------------------------------------------------------------------------""")
while True:
    choises = int(input("Enter Your Choise: "))

    # Checking the users input and applied limit to their input.............
    while choises>3 or choises<1:
        choises = int(input("Enter Valid Choise (Your choise should be 1, 2, or 3): "))

    # Adding to Variable................
    if choises==1:
        user_choise="Rock"
    elif choises==2:
        user_choise="Paper"
    else:
        user_choise="Scissor"

    print(f"Your Choise is : {user_choise}")

    # Ab computer ki bari.............................
    computer = random.randint(1,4)
    if computer==1:
        comp_choise="Rock"
    elif computer==2:
        comp_choise="Paper"
    else:
        comp_choise="Scissor"

    print(f"choise of Jaiswal-G is: {comp_choise}")
    print("----------------------------------------------------------------------------")

    # Logic:
    # Comparission between Rock and Paper:
    if ((user_choise=="Paper" and comp_choise=="Rock") or (user_choise=="Rock" and comp_choise=="Paper")):
        # print("Paper wins.")
        print("------------------------------------------------------------------------")
        result="Paper"

    # Comparission between Rock and Scissor:
    elif ((user_choise=="Scissor" and comp_choise=="Rock") or (user_choise=="Rock" and comp_choise=="Scissor")):
        # print("Rock wins.")
        print("-------------------------------------------------------------------------")
        result="Rock"

    # if user's choise and computer's choise is same then its a tie condition.
    elif (user_choise==comp_choise):
        print("Its a Tie.")
        result="Tie"
        print("-------------------------------------------------------------------------")

    # Comparission between Paper and Scissor:
    else:
        # print("Scissor wins")
        result="Scissor"
        print("-------------------------------------------------------------------------")

    # Score board count:
    if result=="Tie":
        ties += 1
    elif result==user_choise:
        print(f"Weldone! {name}, Keep it up.")
        user_score += 1
    else:
        print("Jaiswal-G wins.")
        computer_score += 1

    # Printing Score Board.......
    print("....................................................................................")
    print("Score Board:")
    print(f"Score of {name} is : {user_score}")
    print(f"Score of Jaiswal-G is: {computer_score}")
    print(f"Game Ties: {ties}")

    print(".....................................................")
    repeat = input("Do you want to Play Again ?")
    if repeat=="No" or repeat=="no":
        break;

print("---------------------------------------------------------------")
print("Thanks for Playing..!")
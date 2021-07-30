import random

user_choice=input("Enter r for Rock, p for Paper, or s for Scissor")
if user_choice=="r":
    user_input="Rock"
elif user_choice=="p":
    user_input="Paper"
elif user_choice=="s":
    user_input="Scissor"
else:
    print("This is not valid input")
number=random.randint(1,3)
if number==1:
    computerchoice="Rock"
elif number==2:
    computerchoice="Paper"
elif number==3:
    computerchoice="Scissor"
print("You chose", user_input)
print("The computer chose", computerchoice)
if user_input=="Rock" and computerchoice=="Rock":
    print("Tie")
elif user_input=="Rock" and computerchoice=="Paper":
    print("You lose")
elif user_input=="Rock" and computerchoice=="Scissor":
    print("You win")
elif user_input=="Paper" and computerchoice=="Rock":
    print("You win")
elif user_input=="Paper" and computerchoice=="Paper":
    print("Tie")
elif user_input=="Paper" and computerchoice=="Scissor":
    print("You lose")
elif user_input=="Scissor" and computerchoice=="Rock":
    print("You lose")
elif user_input=="Scissor" and computerchoice=="Paper":
    print("You win")
elif user_input=="Scissor" and computerchoice=="Scissor":
    print("Tie")

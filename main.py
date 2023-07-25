import random
#USER INPUT
user_input = int(input("What do you choose ???0 for rock, 1 for paper ,2 for scissor"))
#COMPUTER CHOICE SELCTION
computer_choice=random.randint(1,2)
print (f"computer selected {computer_choice}" )

 #CONDITION FOR WIN AND LOOSE
if user_input>=3 or user_input<0:
    print("invalid input")
if user_input == 0 and computer_choice == 2:
    print("you win")
elif computer_choice==0 and user_input==2:
    print("you loose")
elif user_input == computer_choice:
    print ("it is draw")
elif user_input > computer_choice:
    print("you win")
elif computer_choice > user_input:
    print("you loose")
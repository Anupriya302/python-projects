import random
computer_choice=random.randint(0,2)
user_choice=int(input("enter your choice"))
#rock win against scissor
#scissor win against paper
# paper win against rock
#rock=0
#paper=1
#scissor=2
if computer_choice>user_choice:
    print("computer won")
elif computer_choice<user_choice:
    print("user won")
elif computer_choice==user_choice:
    print("it is a tie")
elif computer_choice==0 and user_choice==2:
    print("computer will win") 
elif user_choice==0 and computer_choice==2:
    print("user will win")
else:
    print("end of the game")
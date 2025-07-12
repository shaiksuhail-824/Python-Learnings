import random

user_score = 0
computer_score = 0
option = ['rock','paper','sissors']
while True :
        user_input = input("Enter the any Rock or Paper or Siccors or E for exit: ").lower()

        if user_input == "e" :
            quit()
        elif user_input  not in option :
            continue
        elif user_input in option :
             computer_num= random.randint(0,2)
             

        if user_input == option[computer_num] :
             print("you win")
             user_score = user_score + 1
        else :
             print("you lost")
             computer_score = computer_score +1
print("user_score",user_score)
print("computer_score",computer_score)
print("you quit the game")
        
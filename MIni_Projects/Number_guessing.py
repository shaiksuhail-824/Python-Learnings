import random
lower=int(input("Enter the lower bound:"))
upper=int(input("Enter the upper bound:"))
for i in range(lower,upper):
       random_num=random.randint(lower,upper)
       
       chances=7
       guess_chance=0
       while(guess_chance<chances):
            guess_chance+=1
            guess_num=int(input("Enter the your guess"))
              
            if(guess_num==random_num):
                    print(f'Correct! The number is {random_num}. You guessed it in {guess_num} attempts.')
            elif(guess_num>random_num):
                print("To high,try the lower bond")
            elif(guess_num<random_num):
                print("Too low,try the upper bond")
            elif(guess_num>=random_num and guess_num!=random_num):
                print(f'sorry! The number is{random_num}.Better luck for next time')
                            
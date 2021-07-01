#import random for number generator 
import random
#counter for while loop
user_won_count = 0
comp_won_count = 0


choices = ["rock", 'paper', 'scissors']

tie = "Tied"
won = "You Win"
lose = "You lost"

outcome = [[tie,lose,won],
[won,tie,lose],
[lose,won,tie]]

#loops intill user wins
while user_won_count < 2 and comp_won_count < 2:
    
    #computers choice
    computer_choice = random.randint(0,2)

    #place input in try/except so only int is valid
    try:
        #Ask user for input for Rock paper scissors
        user = int(input("Enter 1 for Rock, 2 for Paper, 3 for Scissors: "))
    #if input is not INT
    except(ValueError):
        print('try again')
        continue
    try:
        #lookup for 1D list
        print("You chose: ", choices[user - 1])
    #if input is not INT
    except(IndexError):
        print('try again')
        continue
    #lookup for 1D list
    print("Computer chose: ", choices[computer_choice])
    
    #lookup for 2D list
    result = outcome[user - 1][computer_choice]
    print(result)
    
    #conditional for RPS results
    if result == won:
        user_won_count += 1
        print(user_won_count)
    elif result == lose:
        comp_won_count += 1
        print(comp_won_count)
    

print("GoodBye")





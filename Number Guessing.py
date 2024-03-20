num = 9
guess_limit=3
guess_count=0
while guess_count<guess_limit:
    guess=int(input("Enter the number - "))
    guess_count+=1
    if guess==num:
        print('You WON :)')
        break
else:
    print("Sorry you failed :(") 
    
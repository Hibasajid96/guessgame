import random

rand = random.randint(1,10)
print(rand)

count = 5
while count>=1:
    
    ans = int(input("Guess the random number"))

    if ans == rand:
        print("you won")
        break
    else:
        print("try again")
        count=count-1
    

if count==0:
    print("you lost")

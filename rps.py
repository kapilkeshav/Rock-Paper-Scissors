import random

class user:
    def __init__(self,name):
        self.name = name

Choices = ['rock','paper','scissors']
cs = 0
us = 0
u = 0
c = 0
ctr = 0
def computer():
    global c
    a = random.choice(Choices)
    if a==c:
        return random.choice(Choices)
    else:
        return a
    

def check(u,c):
    global cs
    global us
    if u=='rock' and c =='scissors':
        us+=1
        return us
    elif u=='rock' and c=='paper':
        cs+=1
        return cs
    elif u=='paper' and c=='scissors':
        cs+=1
        return cs
    elif u=='paper' and c=='rock':
        us+=1
        return us
    elif u=='scissors' and c=='rock':
        cs+=1
        return cs
    elif u=='scissors' and c=='paper':
        us+=1
        return us
    else:
        return 0


print("********************** Rock Paper Scissors **********************" )
print("                     Made by Keshav Dev Kapil                    ")

user1 = user(input("Enter name of user1: "))

print("Welcome to Rock, Paper Scissors. How do you want to play:\n1.{} Vs Computer\n2.{} Vs friend".format(user1.name,user1.name))
chs = int(input("enter choice(1 for computer, 2 for friend): "))
if chs == 1:
    while(True):
        print("\nChoose your option:\nRock \nPaper \nScissors\n")
        u = input("Enter your choice: ").lower()
        c = computer()
        if u not in Choices:
            print("Enter valid choice!\n")
            continue
        else:
            print("User Choice: {} \t Computer Choice: {}".format(u,c))
            check(u,c)
            print("User score: {} \t \t Computer Score: {}".format(us,cs))
            if us == 3:
                print("\nCongratulations, You win!")
                break
            elif cs == 3:
                print("\nyou lost :(")
                break   
            else:
                continue

elif chs == 2:
    user2 = user(input("Entee name of user2: "))
    while(True):
        print("\nChoose your option:\nRock \nPaper \nScissors\n")
        u = input("Enter your choice, {}: ".format(user1.name)).lower()
        c = input("Enter your choice, {}: ".format(user2.name)).lower()
        if u not in Choices or c not in Choices:
            print("Enter valid choice!\n")
            continue
        else:
            print("{}: {} \t {}: {}".format(user1.name,u,user2.name,c))
            check(u,c)
            print("{}: {} \t {}: {}".format(user1.name,us,user2.name,cs))
            if us == 3:
                print("\nCongratulations, {} win this game!!!\n{} lost :(".format(user1.name,user2.name))
                break
            elif cs == 3:
                print("\nCongratulations, {} win this game!!!\n{} lost :(".format(user2.name,user1.name))
                break   
            else:
                continue
    


    
    
    
        
    

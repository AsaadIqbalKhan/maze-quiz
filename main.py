from colorama import init
from termcolor import colored
from colorama import just_fix_windows_console
just_fix_windows_console()
import random

#generating the initial maze of n*n size
def mazegenerator(n):
    mazematrix=[]
    for row in range(n):
        currRow=[]
        for col in range(n):
            currRow.append("o")
        mazematrix.append(currRow)
    
    #adding 25% random walls
    qn=(n*n)//4
    dic={}
    countwalls=0
    while countwalls<qn:
        rand1=random.randint(0,n-1)
        rand2=random.randint(0,n-1)
        if (rand1,rand2) not in dic:
            dic[(rand1,rand2)]=0
            mazematrix[rand1][rand2]="▓"
            countwalls+=1
    
    #definining start and end
    mazematrix[0][0]="S"
    mazematrix[n-1][n-1]="E"
    print(mazematrix)
    return mazematrix


#displaying the maze

def displaymaze(mazematrix):
    n=len(mazematrix)
    for row in range(n):
        for col in range(n):
            if mazematrix[row][col]=="o":
                print(colored("|o|","blue","on_black"),end="")
            elif mazematrix[row][col]=="▓":
                print(colored("|▓|","red","on_black"),end="")
            elif mazematrix[row][col]=="◍":
                print(colored("|◍|","green","on_black"),end="")
            elif mazematrix[row][col]=="S":
                print(colored("|S|","green","on_black"),end="")
            else:
                print(colored("|E|","green","on_black"),end="")
        print()
displaymaze(mazegenerator(5))



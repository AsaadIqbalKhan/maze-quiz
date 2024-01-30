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

    return mazematrix

mazegenerator(5)



import random
env=[[0,0,0],
    [0,"A",0],
    [0,0,0]]

row=int(input("enter row for dirt (0-2) : "))
coloumn=int(input("enter coloumn for dirt (0-2) : "))
env[row][coloumn]=1
for i in env:
    print(i)
print("dirt added",end = '\n')
movements=[-1,0,1]; curr=[1,1]; d=0; cp=[]; cost=0
while env[curr[0]][curr[1]]!=2:
    ch1=random.choice(movements); ch2=random.choice(movements)
    if (curr[0]+ch1<len(env) and curr[0]+ch1>-1) and (curr[1]+ch2<len(env) and curr[1]+ch2>-1):
        if (env[curr[0]+ch1][curr[1]+ch2])==1:
            env[curr[0]+ch1][curr[1]+ch2]="A"; env[curr[0]][curr[1]]=0
            for i in env:
                print(i)
            print()
            print("dirt cleaned")
            cost+=1
            break
        if (env[curr[0]+ch1][curr[1]+ch2])==0 and [curr[0]+ch1,curr[1]+ch2]:
            env[curr[0]+ch1][curr[1]+ch2]="A"; env[curr[0]][curr[1]]= 0
            for i in env:
                print(i)
            print()
            curr[0]+=ch1; curr[1]+=ch2
            cost+=1
print("Path cost : ",cost)

def numpattern(n):
    for i in range(1,n+1):
        for j in  range(1,i+1):
            print(j*i,end=" ")
        print(" ")
num=int(input("enter a limit:"))
numpattern(num)

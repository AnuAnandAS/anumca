def factorial(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        fact=1
        for i in range(n,0,-1):
            fact=fact*i
        return fact
i=int(input("enter a number:"))
f=factorial(i)
print("factorial=",f)

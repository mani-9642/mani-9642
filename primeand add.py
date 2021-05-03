n=int(input('Enter the Start number : '))
k=int(input("Enter the end number : "))
t=0
for x in range(n,k+1):
    #print(x,end="\t")
    if x==2 or x==3 or x==5:
        print(x,"is a Prime Number")
        t = t + x
    elif x%2==0 or x%3==0 or x%5==0:
        pass
    else:
        print(x,"is a prime Number")
        t=t+x
print(t)
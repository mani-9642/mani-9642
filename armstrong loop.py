ch="y"
while ch=="y":
    n = int(input("Enter the Number : "))
    s = 0
    t = n
    while t>0:
        r=t%10
        s+=r**3
        t//=10
    if n==s:
        print(n,"is Armstrong Number")
    else:
        print(n,"is not a Armstrong Number")
    ch=input("Do you want to check again (Y/N) : ")
print("Thank You")
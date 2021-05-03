ch="y"
while ch=="y":
    n=int(input("Enter the Number : "))
    s=0
    while n>0:
        r=n%10
        s=s*10+r
        n=n//10
    print(s)
    ch=input("Do you want check Again (Y/N) : ")
print("Thank you")
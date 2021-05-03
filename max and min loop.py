ch="y"
while ch=="y":
    a=[]
    n=int(input("No.Of Number : "))
    for x in range(n):
        k=int(input("Enter the Number : "))
        a.append(k)
    print(a)
    print("Maximum Number is ",max(a),"\n Minimum Number is ",min(a))
    ch=input("Do you Want to Check again (Y/N) : ")
print("Thank You")
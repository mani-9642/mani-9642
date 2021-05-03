n=int(input("Enter the Year : "))
a=[]
for x in range(1,n):
    if x%4==0 or x%100==0 or x%400==0:
        print(x,"is a leap Year")
        a.append(x)
print(a)
print(len(a))
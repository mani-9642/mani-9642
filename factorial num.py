n=int(input("Enter the factorial Number : "))
f=1
for x in range(1,n+1):
    print(x,end="\t")
    f=f*x
print(f)
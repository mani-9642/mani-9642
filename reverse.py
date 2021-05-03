n=int(input("Enter the Number : "))
r=0
while n>0:
   re=n%10
   r=(r*10)+re
   n=n//10
print(r)
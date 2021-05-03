n=int(input("Enter the Number : "))
def digit(n):
  if n<10:
    print(n,end=" ")
  else:
    digit(n//10)
    k=n%10
    print(k,end=" ")
digit(n)
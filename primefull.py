x=int(input())
if x==1:
    print("Not Prime")
else:
    if x%2==0 and x>2:
        print("Not Prime")
    else:
        for y in range(3,int(x**1/2)+1,2):
            if x%y==0:
                print("Not Prime")
                break
        else:
            print("Prime")
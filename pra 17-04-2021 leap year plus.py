start = int(input("Enter start year: "))
end = int(input("Enter end year: "))
a=[]
if start < end:
    print ("Here is a list of leap years between " + str(start) + " and " + str(end)  + ":")
while start < end:
    if start % 4 == 0 and start % 100 != 0:
        a.append(start)
        print(start)
    if start % 100 == 0 and start % 400 == 0:
        a.append(start)
        print(start)
    start += 1

if start >= end:
 print("Check your year input again.")
print(a)
print(len(a))
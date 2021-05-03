a = []
k=["Pizza","Breadsticks","Pasta","Burger","Cake","Chips"]
class PizzaHut:
    def selection(self):
        print("\t\t\t Dominos Pizza Hut")
        print("1.Pizza\n2.Breadsticks\n3.Pasta\n4.Burger\n5.Cake\n6.Chips")
        ch="y"
        while ch=="y":
            n = int(input("Enter your Item : "))
            if n<7 and n>0:
                if n == 1:
                    a.append("Pizza")
                elif n == 2:
                    a.append("Breadsticks")
                elif n == 3:
                    a.append("Pasta")
                elif n == 4:
                    a.append("Burger")
                elif n == 5:
                    a.append("Cake")
                elif n == 6:
                    a.append("Chips")
            else:
                print("Wrong Selection Try again")
            ch=input("Do you want to add any Item (y/n) : ")
        print("Your Order is : ",a)
class modify(PizzaHut):
    def change(self):
        m=input("Do you want to modify order (y/n) : ")
        while m=="y":
            print("1. Add Item\n2.Delete Item\n3.Modify Item")
            l=int(input("Enter your choice : "))
            if l == 1:
                PizzaHut.selection(self)
                m = input("Do you want to modify again (y/n): ")
            elif l == 2:
                print(a)
                d=input("Enter the delete item : ")
                if d in a:
                    a.remove(d)
                    m=input("Do you want to modify again (y/n): ")
                    print("Your order is", a)
                else:
                    print("Sorry item is not available\nYour order is :",a)
                    m = input("Do you want to modify again (y/n): ")
            elif l == 3:
                print("Your Order is : ",a)
                c=input("Enter Item Name to Modify : ")
                if c in a:
                    i=a.index(c)
                    print("1.Pizza\n2.Breadsticks\n3.Pasta\n4.Burger\n5.Cake\n6.Chips")
                    r=input("Enter Item to replace : ")
                    if r in k:
                        a[i] = r
                        print("Your order is", a)
                        m = input("Do you want to modify again (y/n): ")
                    else:
                        print("Sorry Item is not available")
                        m = input("Do you want to modify again (y/n): ")
                else:
                    print("Sorry Item is not available in your order")
                    m = input("Do you want to modify again (y/n): ")
            else:
                print("Thank You")
                m = input("Do you want to modify again (y/n): ")
class values(modify):
    def prices(self):
        print("1.",k[0],"-->340.0")
        print("2.",k[1],"-->160.0")
        print("3.",k[2], "-->95.0")
        print("4.",k[3], "-->180.0")
        print("5.",k[4], "-->120.0")
        print("6.",k[5], "-->70")
s=values()
s.selection()
s.change()
print("Your Order is : ",a)
s.prices()
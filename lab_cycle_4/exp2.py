def add(a,b): 
        return a+b
def subtract(a,b):
        return a-b
def multiply(a,b):
        return a*b
def divide(a,b):
        return a/b if b!=0 else "cannot divide by zero"
def calculator():
        while True:
                print("\n1.Addition\n2.Subtaction\n3.Multiplication\n4.Division\n5.Exit")
                choice=int(input("Enter Choice:"))
                if choice==5:
                        break;
                a=float(input("Enter First Number:"))
                b=float(input("Enter Second  Number:"))
                if choice==1:
                        print("Result:",add(a,b))
                elif choice==2:
                        print("Result",subtract(a,b))
                elif choice==3:
                        print("Result",multiply(a,b))
                elif choice==4:
                        print("Result",divide(a,b))
                else:
                        print("Invalid Choice!")
calculator()

num=int(input("Enter a  number"))
factorial=1
if num<0:
        print("factorial of negative numbers is not defined")
else:
        for i in range(1,num+1):
                factorial*=i
        print("The factorial of",num,"is",factorial)

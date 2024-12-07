'''program to add variable length integer arguments
passed to the function 'add' and also to demonstrate 
the use of docstrings '''
def add(*args):
        return sum(args)
n=int(input("Enter the number of elements:"))
l=[]
for i in range(n):
        a=int(input("Enter a number:"))
        l.append(a)
result=0
for i in l:
        result=result+i
print("The sum is:", result)

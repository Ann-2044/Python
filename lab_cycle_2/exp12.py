n=int(input("Enter number of integers to input:"))
list1=[]
for i in range(n):
        num=int(input("Enter Integer"))
        list1.append(num)
n=int(input("Enter no.of integers to input:"))
list2=[]
for i in range(n):
        num=int(input("Enter Integers:"))
        list2.append(num)
if len(list1)==len(list2):
        print("The list are of the same length")
else:
        print("The list are of the different length")
if sum(list1)==sum(list2):
        print("The list sum to the same value")
else:
        print("The list do not have the same sum value")
common=set(list1).intersection(list2)
if common:
        print(f"Common values in both list:{common}")
else:
        print("There is no common values in both the sets") 

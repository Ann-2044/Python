num = input("Enter a list of numbers separated by space: ")
n = num.split()
lst = []
for i in n:
    lst.append(int(i.strip()))

powers_of_2 = list(map(lambda x: 2 ** x, lst))
print("Powers of 2:", powers_of_2)

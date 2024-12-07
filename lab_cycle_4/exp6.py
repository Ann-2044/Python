num = input("Enter a list of numbers separated by space: ")
n = num.split()
lst = [int(i.strip()) for i in n]
multiples_of_3 = list(filter(lambda x: x % 3 == 0, lst))
print("Multiples of 3:", multiples_of_3)

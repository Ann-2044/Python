import math
start = 1000
end = 9999
result = []
for num in range(start, end + 1):
    num_str = str(num)
    if all(digit in '02468' for digit in num_str):
        sqrt = int(math.sqrt(num))
        if sqrt * sqrt == num:
            result.append(num)
print("List of four-digit numbers(1000-9999)with all even digits and perfect squares:   ")
print(result)

input_numbers=input("Enter Integer seperated by commas:").split(',')
result=[]
for num in input_numbers:
        if int(num)>100:
                result.append('over')
        else:
                result.append(int(num))
print(result)

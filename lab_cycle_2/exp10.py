num=input("Enter the integers seperated by commas").split(',')
result=[]
for n in num:
        number=int(n)
        if(number%2)!=0:
                result.append(int(n))

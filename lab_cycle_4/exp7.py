def factorial(num):
        if num==0 or num==1:
                return 1
        else:
                result=1
                for i in range(2,num+1):
                        result*=i
                return result
def sum_series(n):
        series_sum=0
        for i in range(1,n+1):
                term=(i**i)/factorial(i)
                series_sum+=term
        return series_sum
n=int(input("Enter a positive integer:"))
if n<0:
        print("Please enter a positive integer.")
else:
        result=sum_series(n)
        print(f"The sum of the series 1/1! + 4/2! + 27/3! + .... upto {n} terms is: {result}")

def is_prime(num):
        if num<=1:
                return False
        for i in range(2,int(num**0.5)+1):
                if num%i==0:
                        return False;
                return True
def nth_prime(n):
        count=0
        num=2
        while True:
                if is_prime(num):
                        count+=1
                        if count+1==n:
                                return num
                num+=1
n=int(input("Enter the value of n to find the nth prime number:"))
if n<=0:
        print("Please enter a positive integer")
else:
        result=nth_prime(n)
        print(f"The {n}th prime number is: {result}")

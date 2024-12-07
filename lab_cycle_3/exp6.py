n=int(input("Enter value: "))
primes=[]
for n in range(2,n+1):
        prime=True
        for i in range(2,int(n**0.5)+1):
                if n%i==0:
                        prime=False
                        break
        if prime:
                        primes.append(n)
for i in range(0,len(primes),2):
        print(primes[i],end=" ")
        print()

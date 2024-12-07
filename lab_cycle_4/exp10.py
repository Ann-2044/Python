def factorial(n):
        if n==0 or n==1:
                return 1
        else:
                return n*factorial(n-1)
def permutation(n,r):
        return factorial(n)/factorial(n-r)
def combination(n,r):
        return factorial(n)/(factorial(r)*factorial(n-r))
n=int(input("Enter the value of n:"))
r=int(input("Enter the value of r:"))
print(f"The number of permutaions of {n} objects taken {r} at a time : p({n},{r}) = {n}!/({n}-{r})! = {permutation(n,r)}")
print(f"The number of Combinations of {n} objects taken {r} at a time : c({n},{r}) = {n}!/({r}! * ({n}-{r})!) = {combination(n,r)}")

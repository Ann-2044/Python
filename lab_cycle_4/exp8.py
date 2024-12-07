def compare(s1,s2,n):
        if s1[:n]==s2[:n]:
                return True
        else:
                return False
s1=input("Enter first String:")
s2=input("Enter second String:")
n=int(input("Enter an integer:"))
result=compare(s1,s2,n)
if result==True:
        print(f"The first {n} characters of both the strings are same.")
else:
        print(f"The first {n} characters of both the strings are not same.")

import math
a=float(input("Enter the coefficient of a"))
b=float(input("Enter the coefficient of b"))
c=float(input("Enter the coefficient of c"))
d=b**2-4*a*c
if d>0:
    root1=-b+math.sqrt(d)/(2*a)
    root2=-b-math.sqrt(d)/(2*a)
    print(f"THE ROOTS ARE DIFFERENT,solutions of the given quadratic equations are {root1} & {root2}")
elif d==0:
    root=-b/2*a
    print(f"THE ROOTS ARE EQUAL,solutions are{root}")
else:
    real_part=-b/2*a
    imaginary_part=math.sqrt(-d)/2*a
    print(f"THE ROOTS ARE COMPLEX,solutions of the given quadratic equations are {real_part}+{imaginary_part},{real_part}-{imaginary_part}")

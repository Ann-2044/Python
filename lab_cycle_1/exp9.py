year=int(input("Enter year:"))
if year%400==0: 
        print(f"It is a centuary year,{year} is a leap year")
elif year%100!=0 and year%4==0:
        print(f"{year} is a leap year")
else:
        print(f"{year} not a leap year")

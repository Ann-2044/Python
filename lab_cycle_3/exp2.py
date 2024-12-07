terms=int(input("Enter the number of terms:"))
if terms<0:
        print("Please enter a positive integer")
else:
        print("Fibonacci Series:")
        first_term=0
        second_term=1
        print(first_term)
        print(second_term)
        for i in range(2,terms):
                next_term=first_term+second_term
                print(next_term)
                first_term=second_term
                second_term=next_term

numbers=[-10,15,-37,25,18,0]
positive_no=[num for num in numbers if num>0]
print(f"Positive numbers in {numbers}:",positive_no)
N=5
squares=[num**2 for num in range(1,N+1)]
print("Squares of first 5 numbers:",squares)
word="comprehension"
vowels=[char for char in word if char in'aeiou']
print(f"vowel in word:{word}",vowels)
word="hello"
oridinal_values=[ord(char) for char in word]
print("Ordinal values of each character in the word :hello",oridinal_values)

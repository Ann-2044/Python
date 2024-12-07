string=input("Enter the string:")
newstr=string[0]+string[1:].replace(string[0],'$')
print(newstr)

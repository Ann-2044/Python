list=input("Enter the list of elements seperated by space:")
words=list.split()
length=0
for i in words:
        if len(i)>length:
                length=len(i)
print("The longest word has length",length)

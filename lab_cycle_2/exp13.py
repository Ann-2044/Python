text=input("Enter line of text:")
words=text.split()
word_count={}
for word in words:
        word=word.lower()
        if word in word_count:
                word_count[word]+=1
        else:
                word_count[word]=1
print("Word occurences:",word_count)

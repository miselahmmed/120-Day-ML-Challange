data = "banana"
uWord = {}
for x in data:
    if uWord.get(x) == None:
        uWord[x] = 1
    elif uWord.get(x) != None:
        uWord[x] = uWord[x] + 1
print(uWord)
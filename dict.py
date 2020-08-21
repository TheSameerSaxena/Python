dik = dict()
line = input('Enter a line: ')
words = line.split()
for word in words:
    dik[word] = dik.get(word , 0) + 1
print(dik) 

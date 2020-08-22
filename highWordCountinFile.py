mailist = list()
file = input("Enter file name: ")
fhand = open(file)
for line in fhand:
    if line.startswith('From '):
        word = line.split()
        mailist.append(word[1])

dik = dict()
for count in mailist:
    dik[count] = dik.get(count, 0) + 1

bigword = None
bigcount = None
for woord,coount in dik.items():
    if bigcount is None or coount > bigcount:
        bigword = woord
        bigcount = coount
print(bigword, bigcount)

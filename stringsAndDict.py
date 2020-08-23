llist = list()
fhand = input("Enter a string: ")
line = fhand.split()
for word in line:
    llist.append(word)

dik = dict()
for count in llist:
    dik[count] = dik.get(count, 0) + 1

bigword = None
bigcount = None
for woord,coount in dik.items():
    if bigcount is None or coount > bigcount:
        bigword = woord
        bigcount = coount
print(bigword, bigcount)

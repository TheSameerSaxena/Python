llist = list()
string = input("Enter a string: ")
words = string.split()
for word in words:
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

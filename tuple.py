fhand = open('mbox-short.txt')
lst = list()
for line in fhand:
    if line.startswith('From '):
        words = line.split()
        time = words[5]
        timepiece = time.split(':')
        hour = timepiece[0]
        lst.append(hour)

dict = dict()
for count in lst:
    dict[count] = dict.get(count, 0) + 1
dict = sorted(dict.items())

for k,v in dict:
    print(k,v)
# lst2 = list()
# for k,v in dict.items():
#     lst2.append((k,v))
# for k,v in sorted(lst2):
#     print(k,v)

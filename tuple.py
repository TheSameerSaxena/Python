'''Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.

You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.

From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.'''

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
# Accept a list of n items, Check whether all elements of list are even. if yes, print True.

my_list = []
list_size = int(input('Enter List Size: '))
for i in range(list_size):
    value = int(input(f"Enter {i+1} list value: "))
    my_list.append(value)
print('List is: ', my_list)

odd = 0
for i in my_list:
    if i % 2 != 0:
        odd = 1

if odd == 1:
    print("The List contains ODD value(s), therefore: FALSE")
else:
    print("The List contains all EVEN values, therefore: TRUE") 

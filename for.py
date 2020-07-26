#The quick way
number1 = [6,2,6,2,2]
for j in number1:
    print('*'*j)
print('\n')

#The long way
number = [6,2,6,2,2]
for i in number:
    output = ""
    for item in range(i):
        output += '*'
    print(output)
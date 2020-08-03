largest = None
smallest = None
while True:
    num = input("Enter a Number: ")
    if num == 'done': break
    try:
        num = int(num)
        if largest is None or largest < num : largest = num
        if smallest is None or smallest > num : smallest = num
    except:
        print("Invalid Input")
        continue
print('Largest is ', largest)
print('Smallest is ', smallest)


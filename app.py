weight = int(input("Enter your weight: "))
choice = input("(L)bs or (K)gs ? ")
if choice == 'l' or choice == 'L':
    wei = str((weight*0.45))
    print("Your weight in Kilos is: "+wei+" Kgs")
elif choice == 'k' or choice == 'K':
    wei1 = str((weight*2.205))
    print("Your weight in Pounds is: "+wei1+" Pounds")
else:
    print("Wrong Choice.") 

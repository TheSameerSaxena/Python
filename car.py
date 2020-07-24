choice =""
started = False
stopped = False
while choice != "quit":
    choice = input("> ").lower()
    if choice == "start":
        if started == True:
            print("Car has already started and is moving.")
        else:
            print("Car has now started and is moving.")
            started = True
            stopped = False
    elif choice == "stop":
        if stopped == True:
            print("Car has already stopped.")
        else:
            print("Car stopped.")
            stopped = True
            started = False
    elif choice == "help":
        print('''
start - to start the car.
stop - to stop the car.
exit - to exit
            ''')
    elif choice == "exit":
        break
    else:
        print("Sorry wrong input!")
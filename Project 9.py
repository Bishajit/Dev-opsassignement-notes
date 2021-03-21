car = True
started = False

while car == True:
    user = input ("> ").lower()
    if user == "start":
        if started == True:
            print("Car is already started!")
        else:
            started = True
            print("Car started...")
    elif user == "stop":
            if not started:
                print("Car is already started!")
            else:
                started = False
                print("Car stopped...")
    elif user == "help":
        print("start - to start the car")
        print("to stop the car")
        print("quit-to exit")
    elif user=="quit":
        print("car stopped")
        car = False

    else:
        print ("I don't understand that...")




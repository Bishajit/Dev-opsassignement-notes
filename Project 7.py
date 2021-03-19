Weight = input("Weight: ")



User_choice = input("(L)bs or (K)g: ")


if User_choice == "L" or User_choice == "l":
    Kgs = float (Weight)/.45
    print("You are " + str(Kgs) + " pounds")
elif User_choice ==  "K" or User_choice ==  "k":
    Lbs = float (Weight) * .45
    print("You are " + str(Lbs) + " pounds")


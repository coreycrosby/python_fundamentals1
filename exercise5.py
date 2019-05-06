counter = 0

while counter >=0:
    print("Would you like to walk or run?")
    action = input()

    if action == "walk":
        print("Distance from home is {} km.".format(counter +1))
        counter += 1

    elif action == "run":
        print("Distance from home is {} km".format(counter +5))
        counter += 5


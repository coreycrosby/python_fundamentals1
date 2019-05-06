counter = 0
energy = 100

while counter >=0:
    print("Would you like to walk or run?")
    action = input()

    if action == "walk":
        print("Distance from home is {} km. Your energy level is {}.".format(counter +1, energy +25))
        counter += 1
        energy += 25

    elif action == "run":
        print("Distance from home is {} km. Your energy level is {}.".format(counter +5, energy -50))
        counter += 5
        energy -= 50

    elif action == "go home":
        print("You can go home")
        break
    
    else: print("This command doesn't exist")

    if energy <=0:
        print ("You are out of energy")
        break
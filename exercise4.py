print ("Enter a number")
number = input ()

if int(number) >= 100:
    print("that's a big number")

else: print("why not dream a little bigger")

print ("Enter your age")
user_age = input()

if int(user_age) > 105:
    print("I'm not sure I believe you")

remaining_age = 22 - int(user_age)
print ("We are {} years apart".format(remaining_age))

name = "Corey"
print ("What is your name?")
user_name = input()

if str(user_name) == "Corey":
    print("We have the same name!")

secret_number = 7
print ("Enter a number")
number = input()

if int(number) == secret_number:
    print ("You win!")

elif int(number) == secret_number -1:
    print ("So close!")

elif int(number) == secret_number +1:
    print ("So close!")

else: print ("Try again")
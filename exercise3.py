print ("What is your name?")
user_name = input()
print ("Hello {}".format(user_name))

secret_password = "please"

print ("What's the password?")
password_attempt = input()

correct_or_not = (password_attempt == secret_password)

print ("That's {}!".format(correct_or_not))

print ("How many cookies have been eaten?")
eaten = input()

remaining_cookies = 12 - int(eaten)

print("There are {} cookies left.".format(remaining_cookies))

print("How old are you?")
user_age = input()

user_birth_year = 2019 - int(user_age)

print("You were born in {}".format(user_birth_year))

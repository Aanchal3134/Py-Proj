import random


top_of_range = input("Type a number: ")
# whatever the user types in the input will be returned as a string - so we convert it later
# int("25") -> 25

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('Please type a number larger than 0 next time.')
        quit()
else: 
    print('Please type a valid number next time.')
    quit()

# r = random.randrange(-10, 11) 
# # 11 is upper limit - not included

# a = random.randint(1, 12) 
# #here it includes 12

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else: 
        print('Please type a valid number next time.')
        continue
        
    if user_guess == random_number:
        print("You got it !")
        break
    elif user_guess > random_number:
            print("You were above the number")
    else:
            print("You were below the number")

print("you got it in", guesses, "guesses")



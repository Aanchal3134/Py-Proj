print("Welcome to the Fandom quiz !")

playing = input("Do you want to play the game ? ") 

if playing.lower() != "yes" :
    quit()

print("Okay ! Let's start the game :) ")    
score = 0

answer = input("Who is the Queen of Terrasen ? ")
if answer.lower() == "aelin ashryver":
    print("Correct ! ")
    score += 1
else: 
    print("Incorrect !")


answer = input("Who is the mother of dragons ? ")
if answer.lower() == "daenerys targaryen":
    print("Correct ! ")
    score += 1
else: 
    print("Incorrect !")

answer = input("Who won the Triwizard Tornament ? ")
if answer.lower() == "harry potter":
    print("Correct ! ")
    score += 1
else: 
    print("Incorrect !")

 
answer = input("Who is the Hero of ages ? ")
if answer.lower() == "sazed":
    print("Correct ! ")
    score += 1
else: 
    print("Incorrect !")


answer = input("Who is Kaladin's spren ? ")
if answer.lower() == "syl":
    print("Correct ! ")
    score += 1
else: 
    print("Incorrect !")

print("Your score is : " , (score))
print("Your percentage is : " , ((score/5) * 100), "%.")





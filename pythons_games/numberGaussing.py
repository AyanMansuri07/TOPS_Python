import random
winNumber = random.randint(1,100)
# winNumber = 40
print("-------THIS IS THE FIRST LEVEL OF THE GAME YOU Have to guess the number between 1 to 100")
number = int(input("Enter number: "))

while number != winNumber:
    if number > winNumber:
        print("Number is too high")
    elif number < winNumber:
        print("Number is too low")
    
    # Ask again inside the loop
    number = int(input("Enter number again: "))

print("YOU WIN THE GAME!")

print("\n--NOW YOU ARE GOING TO THE SECOND LEVEL--")
print("----NOW YOU HAVE ONLY 7 ATTEMPTS IN THIS LEVEL")
winLevelNumber = random.randint(1,100)

for i in range (1,8):
    levelnumber = int(input("Enter the number : "))
    if number > winLevelNumber:
        print("Number is too high")
    elif number < winLevelNumber:
        print("Number is too low")
    else:
        print("YOU WIN")
        print("COngratulation you creak this level-----")
        
print("you reach out maximum attempts ")
print(" The secret number is ",winLevelNumber)
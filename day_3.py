# Modulo Operator
# The modulo operator (%) returns the remainder of a division operation.

# print("Check number even or odd")

# number = int(input("Number: "))

# if number % 2 == 0:
#     print("Even")
# else:
#     print("Odd")



# age = int(input("Enter age: "))
# if age <= 12:
#     print("Pay $5")
# elif age <= 18:
#     print("Pay $10")
# else:
#     print("Pay $12")

print("Welcome to Treasure Island. "
"Your mission is to find the treasure")

choice1 = input("Left or Right? ").lower()
if choice1 == 'left':
    choice2 = input("Swim or Wait? ").lower()
    if choice2 == 'wait':
        choice3 =input("Which door? Red or Blue or Yellow? ").lower()
        if choice3 == 'yellow':
            print("You Won. ")
        elif choice3 == 'blue':
            print("Eaten by beasts. "
                  "Game Over. ")
        elif choice3 == 'red':
            print('Burned by fire. '
                  'Game Over.')
        else:
            print('Game Over.')
    else:
        print("Attacked by trout. Game Over.")
else:
    print("Fall into a hole. Game Over.")

# choice2




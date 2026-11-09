# print("Welcome to the Rollercoster!")
# height = int(input("Enter your height (in cm):\n"))

# if height < 120:
#     print("Enjoy your ride")
#     age = int(input("Enter your age: "))
#     if age >= 18:
#         print("You will pay $17")
#     else:
#         print("You will pay $10")

# else:
#     print("Sorry you can't ride the rollercoaster")


# # num = int(input("Enter your number: "))

# # if num % 2 == 0:
# #     print(f'Your number {num} is even')

# # else:
# #     print(f'Your number {num} is odd')


# Pizza Order Practice
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, L: ")
# bill = 0
# if size == "S":
#     bill += 10
#     print("Your bill is $10")
    
# elif size == "M":
#     bill += 15
#     print("Your bill is $15")

# elif size == "L":
#     bill += 20
#     print("Your bill is $20")

# else:
#     print("Choose an accurate size")

# pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
# if pepperoni == "Y":
#     if size == "S":
#      bill += 2
#      print(f'Your price is ${bill}')

#     else:
#         bill += 3
#         print(f"Your price is ${bill}")


# extra_cheese = input("Do you want extra cheese? Y or N: ")
# if extra_cheese == "Y":
#     bill += 1
#     print(f'Your total bill is ${bill}')


# DAY 3 PROJECT: TREASURE ISLAND
print("Welcome to Treasure Island")
print("Your mission is to find the treasure")
choice1 = input("Choose left or right: ")
if choice1 == "left":
    choice2 = input("Choose swim or wait: ")
    if choice2 == "wait":
     choice3 = input("Which door do you want to choose? Red Blue Yellow: ")
     if choice3 == "Blue":
        print("Eaten by beasts.Game Over.")

     elif choice3 == "Red":
        print("Burned by fire.Game Over.")

     elif choice3 == "Yellow":
        print("You Win")

     else:
        print("Game over")
    
    
    else:
        print("Attacked by trout.Game Over." ) 
else:
    print("Fall into a hole.Game Over")


    

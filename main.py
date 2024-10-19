import random
#Choose any of the number for 
rock = 1
paper = 2
scissors = 3
user_choice = input("Enter your choice(1.rock,2.paper,3.scissors):")
computer_choice = random.randint(1,3)
if user_choice == rock and computer_choice == scissors :
    print("You win!")
elif user_choice == paper and computer_choice == rock:
    print("You win!")
elif user_choice == computer_choice:
    print("It's a tie.")
elif user_choice == scissors and computer_choice == paper:
    print("You win!")
else:
    print("You lose!")
print()
print("Computer went with:",computer_choice)
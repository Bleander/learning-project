def treasure_island():
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.")

    # First choice
    choice1 = input("You're at a cross road. Do you go 'left' or 'right'? ").lower()
    if choice1 != "left":
        print("You fell into a hole. Game over.")
        return

    # Second choice
    choice2 = input("You come to a lake. Do you 'wait' for a boat or 'swim' across? ").lower()
    if choice2 != "wait":
        print("You tried to swim and were eaten by a trout. Game over.")
        return

    # Third choice
    choice3 = input("You arrive at three doors: 'red', 'blue', or 'yellow'. Which one do you choose? ").lower()
    if choice3 == "yellow":
        print("You found the treasure! You win!")
    elif choice3 == "red":
        print("You entered a room of fire. Game over.")
    elif choice3 == "blue":
        print("You entered a room of beasts. Game over.")
    else:
        print("That door doesn't exist. Game over.")
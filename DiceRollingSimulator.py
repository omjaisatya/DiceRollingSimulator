import random

def roll_dice(num_dice, num_rolls):
    for _ in range(num_rolls):
        outcomes = [random.randint(1, 6) for _ in range(num_dice)]
        total = sum(outcomes)

        print(f"Roll: {outcomes} => Total: {total}")

if __name__ == "__main__":
    while True:
        try:
            num_dice = int(input("Enter the number of dice: "))
            if num_dice <= 0:
                print("Please enter a positive integer for the number of dice.")
                continue
        
            num_rolls = int(input("Enter the number of rolls: "))
            
            if num_rolls <= 0:
                print("Please enter a positive integer for the number of rolls.")
                continue
            roll_dice(num_dice, num_rolls)
            repeat = input("Do you want to roll the dice again? (yes/no): ").lower()

            if repeat != 'yes':
                print("Goodbye!")
                break

        except ValueError:
            print("Invalid input. Please enter a valid number.")

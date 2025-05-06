import random

NUM_SIDE = 6

def roll_dies():
    die1 = random.randint(1, NUM_SIDE)
    die2 = random.randint(1, NUM_SIDE)

    total = die1 + die2
    print(f"Die 1 : {die1} Die 2 : {die2} , Total {total}")

def main():
    die1 = 10

    print(f"die1 in main() start as {die1}")

    for _ in range(3):
        roll_dies()

        print(f"die1 in main() is still now {die1}")

if __name__ == "__main__":
    main()
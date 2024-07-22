# 5-6 Stages of Life
# Write an if-elif-else chain that determines a person's stage of life.  Set a
# value for the variable age, and then:

# If the person is less than 2 years old print a message that the person is a
# baby.

# If the person is at least 2 years old but less than 4, print a message that
# the person is a toddler.

# If the person is at least 4 years old but less than 13, print a message that
# the person is a kid.

# If the person is at least 13 years old but less than 20, print a message that
# the person is a teenager

# If the person is at least 20 years old but less than 65, print a message that
# the person is an adult.

# If the person is age 65 or older, print a message that the person is an elder



messages = [
    "the person is a baby",
    "the person is a toddler",
    "the person is a kid",
    "the person is a teenager",
    "the person is an adult",
    "the person is an elder",
    "are you sure about that",
    "unknown input",
]
# green: < 2
# yellow: >= 2, < 4
# red: >= 4, < 131
# white: = >=13, < 20
# blue: >=20, < 65
# orange: >= 65, <100
# black: >= 100

def guessing_game():
    print("Welcome to age allocator")
    print("Input your age and output will be your group")

    while True:
        try:
            guess = int(input("Enter your age (between 1 and 100): "))
            if guess < 2:
                msg = f"Hello, {messages[0]}!"
                print(msg)
    # baby
            elif guess >= 2 and guess < 4:
            # if guess < 4:
                msg = f"Hello, {messages[1]}!"
                print(msg)
    # toddler
            elif guess >= 4 and guess < 13:
                msg = f"Hello, {messages[2]}!"
                print(msg)
    # kid
            elif guess >= 13 and guess < 20:
                msg = f"Hello, {messages[3]}!"
                print(msg)
    # teenager
            elif guess >= 20 and guess < 65:
                msg = f"Hello, {messages[4]}!"
                print(msg)
    # adult
            elif guess >= 2 and guess < 100:
                msg = f"Hello, {messages[5]}!"
                print(msg)
    # elder
            else:
                msg = f"Hello, {messages[6]}!"
                print(msg)
        except ValueError:
            print("Invalid input! Please enter a valid number.")

            break

play_again = input("Any more questions? (yes/no): ").lower()
if play_again == "yes":
    guessing_game()
elif play_again == "y":
    guessing_game()
elif play_again == "ye":
    guessing_game()
else:
    print("Thanks for playing!")

# Start the game
guessing_game()

# checks users enter yes (y) or no (n)
def yes_no(question):
    while True:
        response = input(question).lower()

        # checks user response, question
        # repeats if users don't enter yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes / no")


# Displays instructions to user
def instruction():
    print('''

**** Instructions ****

CHANGE To begin, decide the overall score needed to be crowned the winner of the game (eg: first person to get a 
score of 50 or more).

At the start of each round, the user and the computer each roll two dice. The initial number of points 
for each player is the total shown by the dice. Then, taking turns, the user and computer each roll a 
single die and add the result to their points. The goal is to get 13 points (or slightly less) for a 
given round. Once you are happy with your number of points, you can ‘pass’.

- If you go over 13, then you lose the round (and get zero points).

- If the computer goes over 13, the round ends and your score is the number of points that 
  you have earned.

- If the computer gets more points than you (eg: you get 10 and they get 11, then you lose your score 
  stays the same).

- If you get more points than the computer (but less than 14 points), you win and add your points to 
  your score. The computer’s score stays the same.

- If the first roll of your dice is a double, then your score is increased by double the number of 
  points, provided you win. If the computer’s first roll of the dice is a double, then its points are 
  not doubled (this gives the human player a slight advantage).

- The ultimate winner of the game is the first one to get to the specified score goal.

    ''')


def int_check(question):
    while True:
        error = "Please enter an integer that is 1 or more."

        to_check = input(question)

        # check fpr infinite mode
        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

            # checks that the number is more than or equal to 1
            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# main routine starts here

# initialise game variables
mode = "regular"
rounds_played = 0

print("🔼🔼🔼 Welcome to the Higher Lower Game 🔽🔽🔽")
print()

want_instructions = yes_no("Do you want to read the instructions? ")

# checks users enter yes (y) or no (n)
if want_instructions == "yes":
    instruction()

# ask user for number of rounds / infinite mode
num_rounds = int_check("How many rounds would you like? Push <enter> for infinite mode: ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

# game loop starts here
while rounds_played < num_rounds:

    # rounds headings (based on mode)
    if mode == "infinite":
        rounds_heading = f"\n♾♾♾ {rounds_played + 1} (Infinite Mode) ♾♾♾"
    else:
        rounds_heading = f"\n💿💿💿 rounds {rounds_played + 1} of {num_rounds} 💿💿💿"

    print(rounds_heading)
    print()

    # get user choice
    user_choice = input("choose: ")

    # if user choice is the exit code, break the loop
    if user_choice == "xxx":
        break

    rounds_played += 1

    # if users are in infinite mode, increase number of rounds!
    if mode == "infinite":
        num_rounds += 1

# game loop ends here

# game history / statistics area

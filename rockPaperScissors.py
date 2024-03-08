import random

def greeting():
    return "Ready?"
print(greeting()) #this will print to the console what is entered

def battle():
    person_one = "Rock."
    person_two = "Paper."
    person_three = "Scissors."

    return "Rock, paper, scissors, shoot."
draw = battle()
print(draw)



# creating input for user
# creating a list

def get_choices():
    player_choice = input("Enter choice (rock, paper, or scissors): ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player" : player_choice, "computer" : computer_choice}
    return choices


# implementing arguments and statements; concatantaion 
# Refactoring - process of restructuring code while keeping functionality; usually to make simpler code & nesting

def check_winner(thePlayer, theComputer):           # would run by calling 'check_winner' and inputting arugments EX: check_winner("rock", "paper")
    print(f"You chose {thePlayer}. The computer chose {theComputer}.")          # print("You chose " + player + ". The computer chose " + computer)
    if thePlayer == theComputer:
        return "It's a tie!"
    elif thePlayer == "rock":
        if theComputer == "scissors":
            return "You win!"
        else:
            return "You lose..."
    elif thePlayer == "paper":
        if theComputer == "rock":
            return "You win!"
        else:
            return "You lose..."
    elif thePlayer == "scissors":
        if theComputer == "paper":
            return "You win!"
        else:
            return "You lose..."


# accessing dicionary values
        
choices = get_choices()
result = check_winner(choices["player"], choices["computer"])
print(result)





# EXTRA : types
name = "Max"
age = 39

print(type(name))       # this should print the data type of 'name' in the console (should come out as string)

print(type(name) == str)        # this checks if data type equals string, and puts out a boolean (True or False)
print(isinstance(age, int))     # does the same, checking datatype matches (is age an integer)


# conversion
myAge = int("20")

price = "3.76"
thePrice = float(price)     # called 'casting'

# complex   for complex numbers
# bool  for booleans
# list  for lists
# tuple for tuples
# range     for ranges
# dict  for dictionaries
# set   for sets

# Arithmetic Operators : + , - , * , / , % , ** , //

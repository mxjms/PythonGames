import random

def greeting():
    return "Are you ready?"

print(greeting())

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
    choices = {"player" : player_choice.lower(), "computer" : computer_choice}
    return choices


# implementing arguments and statements; concatantaion 

def check_winner(thePlayer, theComputer):
    print(f"You chose {thePlayer}. The computer chose {theComputer}.")
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


# accessing dictionary values
        
choices = get_choices()
result = check_winner(choices["player"], choices["computer"])
print(result)
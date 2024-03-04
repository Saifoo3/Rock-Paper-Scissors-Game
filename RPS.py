import random

userc = input("Enter Rock, Paper, or Scissor: ").lower()
choices = ["rock", "paper", "scissor"]
sysc = random.choice(choices)

print(f"You chose: {userc}")
print(f"The system chose: {sysc}")

if userc == sysc:
    print("It's a tie!")
elif (userc == "rock" and sysc == "scissor") or \
    (userc == "paper" and sysc == "rock") or \
    (userc == "scissor" and sysc == "paper"):
    print("You Win!")
else:
    print("You Lose!")

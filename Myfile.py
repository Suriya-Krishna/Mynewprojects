import random
i = 1
Dict = {}
user = 0
comptr = 0
name = input("Enter your name:")
print(f"Welcome {name}! Let's start playing")
print("Available actions are: [rock,paper,scissors]")
while i <= 10:
    user_sn = input("Enter your action:")
    comptr_sn = random.choice(["rock", "paper", "scissors"])
    print(f"\n{name} chose {user_sn}, and computer chose {comptr_sn}.\n")
    Dict[i] = [[name, user_sn], ['comptr', comptr_sn]]
    if user_sn == comptr_sn:
        print("It's a tie!!")
    elif user_sn == "paper":
        if comptr_sn == "rock":
            user = user + 1
        else:
            comptr = comptr + 1
    elif user_sn == "scissors":
        if comptr_sn == "paper":
            user = user + 1
        else:
            comptr = comptr + 1
    elif user_sn == "rock":
        if comptr_sn == "scissors":
            user = user + 1
        else:
            comptr = comptr + 1
    i = i + 1
print("Game Over")
print(f"You scored : {user}, Computer scored : {comptr}")
if user == comptr:
    print("Both of you are winners!! YaaY")
elif user > comptr:
    print(f"{name} won, Congratulations!!")
else:
    print(f"Oops! Sorry {name}, Better luck next time!")
option = int(input("Enter the round you need to review:"))
#print(Dict)
for i in range(1, 10):
    if i == option:
        print("Here's the actions:")
        print(Dict[option])

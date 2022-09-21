import replit as rp
import secret_auction_game_logo as logo

rp.clear()
print(logo.logo)
question=input("Do you want to play game? Y or N\n").lower()
bid={}
while question=="y":
    name=input("Please enter your name:\n")
    amount=int(input("please enter the betting amount:\n$"))
    bid[name]=amount
    question=input("Do you want to continue the game? Y or N\n").lower()
    rp.clear()
start=0
k=""
for i in bid:
    if bid[i]>start:
        start=bid[i]
        k=i
if(question=="n"):
    print(logo.logo)
    print(f"The winner is {k} having a bet of {start}$")


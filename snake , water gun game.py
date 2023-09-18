import random

you = input("enter your choices for (snake,water,gun) :- ")

x = ["snake","water","gun"]
computer = random.choice(x)


if you == computer :
    print("both the partcipant chhose {}".format(computer))

elif you == "snake" and computer == "water" :
    print(" congralutaions you win , sanke drink water ")

elif you == "snake"  and computer == "gun" :
    print("you losses , gun kill snake") 

elif you == "water" and computer == "snake":
    print("you losses , sanke drink the water")

elif you =="water"   and computer == "gun" :
    print("you win , gun will drown in water")

elif you == "gun"    and computer == "snake":
    print("you win , gun kills snake")

elif you == "gun" and computer =="water":
    print("you looose , gun drown in water")

else :
    print("wrong format please choose the wright one")


print("computer chooses :- {}".format(computer))                  
import random

computer = """ ___________
 | Working |
 | Working |
 | Working |
 ===========
  ===========
   ============"""


while True:

    print("your computer is not running, fix it. ")
    starting_computer = input("> ")
    if starting_computer.lower() == "help":
        print("""plug: unplug and plug it back in
kick: kick it
buy: buy new one
cry: cry""")

    elif starting_computer.lower() == "plug":
        plug_chance = random.randint(1, 5)
        ran_plug = input("Enter a number 1-5: ")
        if int(ran_plug) == plug_chance:
            print("It Works!")
            print(computer)
            break
        else:
            print("You don't know where the wires go anymore")

    elif starting_computer.lower() == "kick":
        kick_chance = random.randint(1, 10)
        ran_kick = input("Enter a number 1-10: ")
        if int(ran_kick) == kick_chance:
            print("It Works... somehow")
            print(computer)
            break
        else:
            print("Its cracked.")
            break

    elif starting_computer.lower() == "buy":
        buy_chance = random.randint(1, 25)
        ran_buy = input("Enter a number 1-25: ")
        if int(ran_buy) != buy_chance:
            print("The new one works")
            print(computer)
            break
        else:
            print("its crack.")
            break

    elif starting_computer.lower() == "cry":
        cry_chance = random.randint(1, 15)
        ran_cry = input("Enter a number 1-15: ")
        if int(ran_cry) == cry_chance:
            print("The computer somehow feels sympathy and starts working.")
            print(computer)
            break
        else:
            print("your sad.")

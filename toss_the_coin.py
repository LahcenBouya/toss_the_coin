import random

random_number = random.random()

print("""welcome to the  coin guessing  game!
      choose a method to toss the coin:
      1. using random.random()
      2. using random.randint()""")

choice = input("Enter your choice (1 or 2): ")


if choice == "1" :
    random_number = random.random()
    guess = input("enter your guess (head or tails): ").lower()


    if random_number >= 0.5 :
        computer_choice = "head"
        if guess == computer_choice:
            print("congratulations")
        else:
            print("sorry you lost!")
    else:
        computer_choice = "tails"
        if guess == computer_choice:
            print("congratulations")
        else:
            print("sorry you lost!")

elif choice == "2":
    random_number = random.randint(0, 1)
    guess = input("enter your guess (head or tails): ").lower()
    if random_number >= 0.5 :
        computer_choice = "head"
        if guess == computer_choice:
            print("congratulations")
        else:
            print("sorry you lost!")
    else:
        computer_choice = "tails"
        if guess == computer_choice:
            print("congratulations")
        else:
            print("sorry you lost!")

else:
    print("please enter 1 or 2")


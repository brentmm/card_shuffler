#creating list
numberDeck = [
    'Ace ', 'Two ', 'Three ', 'Four ', 'Five ', 'Six ', 'Seven ', 'Eight ',
    'Nine ', 'Ten ', 'Jack ', 'Queen ', 'King '
]
suitDeck = ['Spades', 'Hearts', 'Diamonds', 'Clubs']

card_deck = []

for x in numberDeck:
    for y in suitDeck:
        card_deck.append(x + "of " + y)


#fucntion to shuffle card_deck
def shuffling_deck(shuffle):
    import random
    for i in range(len(shuffle)):
        NumGenerator = random.randint(0, (len(shuffle) - 1))
        shuffle[i], shuffle[NumGenerator] = shuffle[NumGenerator], shuffle[i]
    return shuffle


#function to print card_deck
def print_deck():
    print("")
    print(card_deck)


#function to quit program
def quit(action):
    print("Thanks for playing")


#intro / instructions
print("Welcome to the Card Shuffler Program.")
print("")
print("")
print("You can Shuffle the deck, Display the deck, and Quit the program.")
print("")
print(" (1) Shuffle Deck \n (2) Display Deck \n (3) Quit Progam")
print("")

#asking user what they want to do
choice = input("What action would you like to preform?: ")
while choice != "1" and choice != "2" and choice != "3":
    choice = input("What would you like to do? (Select a #) ")

#checking users input and steps into required function function
while choice == "1" or choice == "2" or choice == "3":
    if choice == ("1"):
        card_deck = shuffling_deck(card_deck)
        choice = input("What would you like to do? (Select a #) ")
    elif choice == ("2"):
        print_deck()
        print("")
        choice = input("What would you like to do? (Select a #) ")
    elif choice == ("3"):
        action = input("Would you like to quit? (yes or no): ").lower()
        if action == ("yes"):
            quit(action)
            print("")
            choice = "Brent"
        else:
            print("")
            choice = input("What would you like to do? (Select a #) ")

    #asking user what they wanna do if choice was not valid
    while choice != "Brent" and choice != "1" and choice != "2" and choice != "3":
        choice = input("What would you like to do? (Select a #) ")

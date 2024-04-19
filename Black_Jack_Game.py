import random

# used for creating cards
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}  # the value of ace is assigned 11 here
# but it's value will be changed to 1 in the game if required :)


# for creating cards
class Cards:

    def __init__(self, suit, rank):

        self.rank = rank
        self.suit = suit
        self.value = values[rank]

    def __str__(self):  # for returning the info of the card in print

        return f"{self.rank} of {self.suit}"


# for creating a deck out of the cards created using the class Card
class Deck:

    def __init__(self):

        self.deck = []  # Initially creating an empty dek

        for suit in suits:  # Filling the deck using nested for loop
            for y in ranks:
                card = Cards(suit, y)
                self.deck.append(card)

        random.shuffle(self.deck)  # shuffling the deck created above

        # doing all these in __init__ because anyway we will have to those things

    def give_card(self):  # for giving cards to the dealer(bot) or the player

        return self.deck.pop()


# for creating player and dealer profile
class Player:

    def __init__(self, name):

        self.name = name
        self.player_cards = []
        self.money = 500  # only the player will be spending money :)

    def add_card(self, new_card):  # for giving card to the player and the dealer

        self.player_cards.append(new_card)

    def __str__(self):

        return f"{self.name} have ${self.money}!"

    def bet(self, bet_money):  # for reducing the money that have been bet by the person

        self.money = self.money - bet_money

    def bet_won(self, bet_money):  # for adding the money won by the player

        self.money = self.money + bet_money * 2

    def display_cards(self):  # for displaying the cards of the player

        print("\nYou have")
        for card in self.player_cards:
            print(card)

    def rank_number(self):

        num = 0
        for card in player.player_cards:
            num += card.value
        return num

    def sum_value(self):  # for finding the sum of the values of the cards for both dealer and player

        num_bot = 0

        for card in self.player_cards:
            num_bot += card.value

        return num_bot

    def num_ace(self):  # for checking the number of aces

        mylist = []

        for card in self.player_cards:
            if card.rank == 'Ace':
                mylist.append("a")
        return len(mylist)

    def clear_player_deck(self):  # for clearing the hand of the player and the dealer after a round

        self.player_cards = []


game_on = True  # setting some variables for the game to run
getting_card = True
dealer_turn = True

player = Player("Player")  # creating player and dealer profile
bot = Player("Dealer")


def bet_amount():  # for cross-checking that the bet amount enter is valid

    try:
        money = input("Enter the amount you want to bet:")

        if int(money) > player.money:
            print("You cannot bet more money than you have!!")
            return int(a)  # creating an intentional error when amount entered is more than they have in the pocket
                           # this return will cause a "NameError"

        return int(money)

    except NameError:
        return bet_amount()

    except:
        print("Enter a number!!")
        return bet_amount()


def play_again():  # for asking if the player want to play the game again
    play = 1
    while play not in ["Y", "N"]:

        play = input("Do you wanna play again?(Y or N): ")
        play = play.upper()

        if play not in ["Y", "N"]:
            print("Please enter a valid option!")

    return play









while game_on:

    getting_card = True  # for resetting the conditions after a game
    dealer_turn = True

    new_deck = Deck()  # created a deck

    for x in range(2):  # distribute cards to the player and the dealer

        player.add_card(new_deck.give_card())
        bot.add_card(new_deck.give_card())

    print(f"You have ${player.money}")
    bet_money = bet_amount()
    player.bet(bet_money)
    print(f"\nOne of the card of the dealer is: {bot.player_cards[0]}")

    num_ace_player = player.num_ace()

    while getting_card:  # player's turn

        player.display_cards()
        num = player.sum_value()

        if num > 21 and num_ace_player != 0:  # for changing the value of ace to 1 when required

            for z in range(num_ace_player):

                num = num - 10
                num_ace_player = num_ace_player - 1  # so that the same ace doesn't get counted 2 times and more

                if num < 21:
                    break

        if num > 21 and num_ace_player == 0:

            print("\nBust!! You went over 21!")
            getting_card = False
            break

        move = input("\nHit(H) or Stay(S):")
        move = move.upper()

        if move == "H":
            player.add_card(new_deck.give_card())

            if player.player_cards[-1].rank == 'Ace':
                num_ace_player = num_ace_player + 1  # if the player gets a new ace then it be added to the tally
                                                     # for reducing the value

            getting_card = True

        elif move == 'S':
            getting_card = False

        else:
            print("Invalid move\n")

    num = player.sum_value()

    if num > 21:
        dealer_turn = False

    num_ace = bot.num_ace()

    while dealer_turn:  # dealer's turn
        num_bot = bot.sum_value()

        if num_bot > 21 and num_ace != 0:

            for z in range(num_ace):
                num_bot = num_bot - 10
                num_ace = num_ace - 1

                if num_bot < 21:
                    break

        if num_bot > 21 and num_ace == 0:

            print("\nThe dealer have:")

            for cardd in bot.player_cards:
                print(cardd)

            print("\nYou win!!\n")
            player.bet_won(bet_money)
            dealer_turn = False
            break

        if num_bot <= num:
            pass

        elif num < num_bot <= 21:

            print("\nThe dealer have:")

            for cardd in bot.player_cards:
                print(cardd)

            print("\nYou lose!!\n")
            dealer_turn = False
            break

        bot.add_card(new_deck.give_card())

        if bot.player_cards[-1].rank == 'Ace':
            num_ace = num_ace + 1

    player.clear_player_deck()
    bot.clear_player_deck()

    if player.money == 0:
        print("\nYou lost all money!! \nBring some money first, noob!")
        break

    play = play_again()

    if play == 'Y':
        game_on = True

    elif play == 'N':
        game_on = False



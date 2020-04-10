# blackjack game created

import random
import os
import time

suits = ("Hearts", "Diamonds", "Spades", "Clubs")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")
values = {"Two":2, "Three":3, "Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8, "Nine":9, "Ten":10, "Jack":10,
          "Queen":10, "King":10, "Ace":11}

class Card:
    """
    This class represents the card object.
    """
    def __init__(self, suit, rank):
        """
        Initialize card object.
        :param suit:
        :param rank:
        """
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " " + self.suit


class Desk:
    """
    This class represents the whole desk
    """
    def __init__(self):
        self.desk = []
        for suite in suits:
            for rank in ranks:
                self.desk.append(Card(suite, rank))

    def __str__(self):
        output = ""
        for card in self.desk:
            output += card.__str__() + "\n"
        return output

    def __len__(self):
        return len(self.desk)

    def shuffel(self):
        random.shuffle(self.desk)

    def deal(self):
        """
        Get one card from the desk
        :return:
        """
        return self.desk.pop()

class Card_Owner:
    """
    This class represents the card owner, it is parent class for either Player or Dealer.
    """
    def __init__(self, name="Card_Owner", debt=0):
        self.name = name
        self.debt = debt
        self.cards_on_hand = []
        self.no_of_aces = 0
        self.cards_value = 0

    def __str__(self):
        output = self.name + " cards on hand: \n"
        for card in self.cards_on_hand:
            output += card.__str__() + "\n"
        output += "Value of your cards is: " + str(self.cards_value)
        return output

    def calculate_cards_value(self):
        """
        Methods calculates value of cards on hand
        :return: Nothing
        """
        # set the cards value to 0 for proper calculations
        self.cards_value = 0
        if self.cards_on_hand:
            for card in self.cards_on_hand:
                value = values[card.rank]
                # check Ace calculation, if higher than 21 count Ace as 1
                if card.rank == 'Ace':
                    if (self.cards_value + value) > 21:
                        value = 1
                self.cards_value += value

    def get_card(self, card):
        """
        Get card to your hand and update cards value
        :return:
        if value of cards <= 21 return 'OK'
        if value if >21 return 'BUST'
        """
        # get new card
        self.cards_on_hand.append(card)
        # update value of cards
        self.calculate_cards_value()
        # count special Ace value
        if card.rank == 'Ace':
            self.no_of_aces += 1

    def check_bust(self):
        return self.cards_value > 21

    def check_blackjack(self):
        return self.cards_value == 21

class Player(Card_Owner):
    """
    This class represents the Player.
    """
    def __init__(self, name="Player One", debt=100):
        Card_Owner.__init__(self, name, debt)
        self.bet_amount = 0

    def __str__(self):
        """
        Print Player cards and debt
        :return: string
        """
        output = Card_Owner.__str__(self)
        output += '\n'
        output += self.current_balance()
        return output

    def current_balance(self):
        output = f'\n{self.name} current balance is: {self.debt}'
        return output

    def bet(self, bet_amount):
        """
        Method is checking if betting is possible, if there is enough money on the debt.
        :param bet_amount:
        :return:
        """
        if bet_amount <= self.debt:
            self.bet_amount = bet_amount
            return True
        else:
            return False

class Dealer(Card_Owner):
    """
    This class represents the Dealer.
    """
    def __init__(self, name="Dealer", debt=1000):
        Card_Owner.__init__(self, name, debt)

    def hide_first_card(self):
        output = self.name + " cards on hand: \n"
        output += "*** Hidden card ***\n"
        for card in self.cards_on_hand[1:]:
            output += card.__str__() + "\n"
        output += "Value of your cards is: " + str(values[self.cards_on_hand[1].rank])
        return output

    # check if threshold 17 is overtaken
    def check_17_threshold(self):
        if self.cards_value >= 17:
            return True
        else:
            return False

class Game:
    """
    Class to keep the players and display the table.
    """
    start = True

    def __init__(self, desk, dealer, player):
        # shuffle the desk before game starts
        desk.shuffel()
        self.desk = desk
        self.dealer = dealer
        self.player = player
        # this flag keeps one hidden card on Dealer side
        self.hidden_card = True
        # this flag keeps one turn of game
        self.game_over = False

    def deal(self):
        """
        Start game and ask for a betting sum.
        :return:
        """
        #os.system('cls')
        #print(self.player.current_balance())
        bet_amount = int(input("\nPlease, give your betting amount: "))
        while (not self.player.bet(bet_amount)) or (bet_amount <= 0):
            #os.system('cls')
            bet_amount = int(input("\nPlease, give your betting amount: "))

    def initialize(self):
        # get 2 first cards for Dealer
        for i in range(2):
            card = self.desk.deal()
            self.dealer.get_card(card)
        # get 2 first cards for Player
        for i in range(2):
            card = self.desk.deal()
            self.player.get_card(card)
        self.print_table()

    def print_table(self):
        os.system('cls')
        if self.hidden_card:
            print(self.dealer.hide_first_card())
        else:
            print(self.dealer)
        print('\n')
        print(self.player)

    def hit(self):
        # get new card for Player
        card = self.desk.deal()
        self.player.get_card(card)

    def stand(self):
        # show all Dealer cards
        self.hidden_card = False
        # stand and finish the one tour hidden_card, get cards for Dealer until points reach 17
        while not self.dealer.check_17_threshold():
            card = self.desk.deal()
            self.dealer.get_card(card)
            self.print_table()

    def check_blackjack(self):
        if game.dealer.check_blackjack() and game.player.check_blackjack():
            print("\nBoth sides have BLACKJACK!")
            #check wins
            time.sleep(2)
            game.check_win()
            game.game_over = True
            game.hidden_card = False
        elif game.dealer.check_blackjack():
            print(f"{self.dealer.name} has a BLACKJACK!")
            #check wins
            time.sleep(2)
            game.check_win()
            game.game_over = True
            game.hidden_card = False
        elif game.player.check_blackjack():
            print(f"{self.player.name} has a BLACKJACK!")
            #check wins
            time.sleep(2)
            game.check_win()
            game.game_over = True
            game.hidden_card = False
        else:
            pass
        #print actual values
        game.print_table()

    def user_move(self):
        """
        User decide if he/she wants to hit or stand
        :return:
        """
        while not self.game_over:
            decision = input("\nIf you want to HIT press 'H' or if you want to STAND press 'S': ")
            if decision.upper() == 'H':
                game.hit()
                if game.player.check_bust():
                    game.check_win()
                    game.hidden_card = False
                    game.game_over = True
                game.print_table()
            elif decision.upper() == 'S':
                game.stand()
                game.check_win()
                game.print_table()
                game.game_over = True

    def check_win(self):
        if self.dealer.check_bust() and self.player.check_bust():
            print(f"\n{self.dealer.name} has a BUST!")
            print(f"\n{self.player.name} has a BUST!")
            time.sleep(2)
        elif self.dealer.check_bust():
            print(f"\n{self.dealer.name} has a BUST!")
            time.sleep(2)
            self.player.debt += self.player.bet_amount
        elif self.player.check_bust():
            print(f"\n{self.player.name} has a BUST!")
            time.sleep(2)
            self.player.debt -= self.player.bet_amount
        elif self.dealer.cards_value < self.player.cards_value:
            self.player.debt += self.player.bet_amount
        elif self.dealer.cards_value > self.player.cards_value:
            self.player.debt -= self.player.bet_amount

#initialize players debt
player_debt = 100
#clear view
os.system('cls')

try:
    while True:
        # create Desk object
        desk = Desk()
        # create Dealer object
        dealer = Dealer()
        # create Player object
        player = Player(debt=player_debt)
        # start the game
        game = Game(desk, dealer, player)
        # for first iteration only print this current balance
        if Game.start:
            print(game.player.current_balance())
        #start deal
        game.deal()
        #get first cards
        game.initialize()
        #check if dealer or player has a blackjack
        game.check_blackjack()
        #check user move
        game.user_move()
        #remember debt value from last game
        player_debt = game.player.debt
        #do not print playars balance in next iterations
        Game.start = False
except KeyboardInterrupt:
    print("\nEND of the GAME!")
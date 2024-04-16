import random
#este es el juego de black jack
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

class Deck:
    def __init__(self):
        self.cards = []
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))
        random.shuffle(self.cards)
        
    def deal_card(self):
        return self.cards.pop()

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    
    def add_card(self, card):
        self.cards.append(card)
        if card.rank in ['Jack', 'Queen', 'King']:
            self.value += 10
        elif card.rank == 'Ace':
            self.value += 11
            self.aces += 1
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
        else:
            # Asignar valores numéricos directamente
            if card.rank == 'Two':
                self.value += 2
            elif card.rank == 'Three':
                self.value += 3
            elif card.rank == 'Four':
                self.value += 4
            elif card.rank == 'Five':
                self.value += 5
            elif card.rank == 'Six':
                self.value += 6
            elif card.rank == 'Seven':
                self.value += 7
            elif card.rank == 'Eight':
                self.value += 8
            elif card.rank == 'Nine':
                self.value += 9
            elif card.rank == 'Ten':
                self.value += 10
def blackjack():
    deck = Deck()
    player_hand = Hand()
    dealer_hand = Hand()

    player_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())

    print("Your cards:", [card.rank for card in player_hand.cards])
    print("Dealer's cards:", [dealer_hand.cards[0].rank, "Hidden"])

    while True:
        choice = input("Do you want to Hit or Stand? (H/S): ").lower()
        if choice == 'h':
            player_hand.add_card(deck.deal_card())
            print("Your cards:", [card.rank for card in player_hand.cards])
            if player_hand.value > 21:
                print("You busted! Dealer wins.")
                break
        elif choice == 's':
            break

    if player_hand.value <= 21:
        print("Dealer's cards:", [card.rank for card in dealer_hand.cards])
        while dealer_hand.value < 17:
            dealer_hand.add_card(deck.deal_card())
            print("Dealer's cards:", [card.rank for card in dealer_hand.cards])
            if dealer_hand.value > 21:
                print("Dealer busted! You win.")
                break

        if dealer_hand.value <= 21:
            if dealer_hand.value > player_hand.value:
                print("Dealer wins.")
            elif player_hand.value > dealer_hand.value:
                print("You win!")
            else:
                print("It's a tie!")

blackjack()
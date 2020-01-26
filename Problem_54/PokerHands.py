from globs import *

"""
    In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

    High Card: Highest value card.
    One Pair: Two cards of the same value.
    Two Pairs: Two different pairs.
    Three of a Kind: Three cards of the same value.
    Straight: All cards are consecutive values.
    Flush: All cards of the same suit.
    Full House: Three of a kind and a pair.
    Four of a Kind: Four cards of the same value.
    Straight Flush: All cards are consecutive values of same suit.
    Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
    The cards are valued in the order:
    2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.
    
    If two players have the same ranked hands then the rank made up of the highest value wins; for example, 
    a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both 
    players have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.
    
    Consider the following five hands dealt to two players:

    Hand	Player 1	 	        Player 2	 	        Winner
    1	 	5H 5C 6S 7S KD          2C 3S 8S 8D TD          Player 2
            Pair of Fives           Pair of Eights

    2	 	5D 8C 9S JS AC          2C 5C 7D 8S QH          Player 1
            Highest card Ace        Highest card Queen

    3	 	2D 9C AS AH AC       	3D 6D 7D TD QD          Player 2
            Three Aces              Flush with Diamonds      
            
    4	 	4D 6S 9H QH QC          3D 6D 7H QD QS          Player 1
            Pair of Queens          Pair of Queens
            Highest card Nine       Highest card Seven
    
    5	 	2H 2D 4C 4D 4S          3C 3D 3S 9S 9D          Player 1
            Full House              Full House
            With Three Fours        with Three Threes

    The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file 
    contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are 
    Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each 
    player's hand is in no specific order, and in each hand there is a clear winner.

    How many hands does Player 1 win?
"""

DEBUG_ON = False


class Hand:
    def __init__(self, hand: list):
        self.values, self.suits = [], []
        self.hand_name = None
        self.hand, self.score = hand, 0
        self.straight, self.flush = False, False

    def sort_hand(self):
        for card in self.hand:
            v = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}.get(card[0], None)
            if not v:
                v = int(card[0])
            self.values.append(v)
            self.suits.append({'S': 'Spades', 'H': 'Hearts', 'D': 'Diamonds', 'C': 'Clubs'}.get(card[1]))

        self.check_flush_check_straight()
        self.check_hand()

    def check_flush_check_straight(self):
        # If the len of a set of suits == 1, then it's a flush.
        if len(set(self.suits)) == 1:
            self.flush = True

        # If it gets through this without breaking then it's a Straight
        if sorted(self.values) == [2, 3, 4, 5, 14]:
            self.straight = True
        else:
            vals_sorted = sorted(self.values)
            for i, sv in enumerate(vals_sorted[1:]):
                if sv != vals_sorted[i] + 1:
                    break
            else:
                self.straight = True

    def check_hand(self):
        if self.straight and self.flush and sorted(self.values) == [10, 11, 12, 13, 14]:
            self.hand_name = 'Royal Flush'
            self.score = 1000
            return

        if self.straight and self.flush and sorted(self.values) != [10, 11, 12, 13, 14]:
            self.hand_name = 'Straight Flush'
            self.score = 900 + max(self.values)
            return

        counts = [self.values.count(card_val) for card_val in self.values]

        if 1 in counts and 4 in set(counts):
            n = self.values[counts.index(4)]
            c = {10: 'Ten', 11: 'Jack', 12: 'Queen', 13: 'King', 14: 'Ace'}.get(n, n)
            self.hand_name = f'Four of a Kind, Four {c}s'
            self.score = 800 + n
            return

        if 2 in counts and 3 in set(counts):
            m = self.values[counts.index(3)]
            n = self.values[counts.index(2)]
            c1 = {10: 'Ten', 11: 'Jack', 12: 'Queen', 13: 'King', 14: 'Ace'}.get(m, m)
            c2 = {10: 'Ten', 11: 'Jack', 12: 'Queen', 13: 'King', 14: 'Ace'}.get(n, n)

            self.hand_name = f'Full House, Three {c1}s over Two {c2}s'
            self.score = 700 + 3*m
            return

        if self.flush and not self.straight:
            self.score = 600 + max(self.values)
            suit = self.suits[0]
            c = {10: 'Ten', 11: 'Jack', 12: 'Queen', 13: 'King', 14: 'Ace'}.get(max(self.values), max(self.values))
            self.hand_name = f'Flush with High Card, {c} of {suit}'
            return

        if self.straight and not self.flush:
            m = max(self.values)
            self.score = 500 + m
            i = self.values.index(m)
            self.hand_name = f'Straight with High Card {max(self.values)} of {self.suits[i]}'
            return

        if 1 in counts and 3 in set(counts):
            m = self.values[counts.index(3)]
            c = {10: 'Ten', 11: 'Jack', 12: 'Queen', 13: 'King', 14: 'Ace'}.get(m, m)
            self.hand_name = f'Three {c}s'
            self.score = 400 + m
            return

        if sorted(counts) == [1, 2, 2]:
            m = self.values[counts.index(2)]
            c = {10: 'Ten', 11: 'Jack', 12: 'Queen', 13: 'King', 14: 'Ace'}.get(m, m)
            self.hand_name = f'Two Pairs of {c}s'
            self.score = 300
            return

        if sorted(counts) == [1, 1, 1, 2]:
            m = self.values[counts.index(2)]
            c = {10: 'Ten', 11: 'Jack', 12: 'Queen', 13: 'King', 14: 'Ace'}.get(m, m)
            self.hand_name = f'One Pair of {c}s'
            self.score = 200
            return

        m = max(self.values)
        n = self.values.index(m)
        o = self.suits[n]
        c = {10: 'Ten', 11: 'Jack', 12: 'Queen', 13: 'King', 14: 'Ace'}.get(m, m)

        self.hand_name = f'High Card, {c} of {o}'
        self.score = 100 + max(self.values)

    def __str__(self):
        return f"{self.hand_name} ({self.score})"


class Poker:

    def __init__(self, ):
        self.player1_score = 0
        self.player2_score = 0
        self.hand_number = 0
        self.hand_results = []

    def another_hand(self, hands: list):
        self.hand_number += 1
        p1 = Hand(hands[0: 5])
        p2 = Hand(hands[5:])

        for player in (p1, p2):
            player.sort_hand()

        self.who_won(p1, p2)

    def who_won(self, p1, p2):
        if p1.score > p2.score:
            self.player1_score += 1
            who_won = 'Player 1 won'
        elif p2.score > p1.score:
            self.player2_score += 1
            who_won = 'Player 2 won'
        else:
            who_won = 'A Draw'

        self.hand_results.append({'HandNum': self.hand_number, 'Result': who_won, "P1": p1, "P2": p2})

    def display_results(self):
        if DEBUG_ON:
            for hand in self.hand_results:
                EULER_LOGGER.debug(f"")
                EULER_LOGGER.debug(f"> {hand['HandNum']:<6}  {hand['Result']}")
                EULER_LOGGER.debug(f"    P1:  {str(hand['P1'].hand):<35} {hand['P1'].__str__()} ")
                EULER_LOGGER.debug(f"    P2:  {str(hand['P2'].hand):<35} {hand['P2'].__str__()} ")

            EULER_LOGGER.debug(f"")
            EULER_LOGGER.debug(f"Player 1: {self.player1_score:<10} Player 2: {self.player2_score}")


def main():
    with open("p054_poker.txt", "r") as f:
        hands_list = f.readlines()

    p = Poker()
    for hands in hands_list:
        p.another_hand(hands.replace('\n', '').split(' '))

    p.display_results()
    return p.player1_score


if __name__ == '__main__':
    answer = main()
    show_answer(answer)

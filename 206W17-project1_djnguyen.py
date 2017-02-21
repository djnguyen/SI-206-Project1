import random
import unittest

class Card(object):
	suit_names =  ["Diamonds","Clubs","Hearts","Spades"]
	rank_levels = [1,2,3,4,5,6,7,8,9,10,11,12,13]
	faces = {1:"Ace",11:"Jack",12:"Queen",13:"King"}

	def __init__(self, suit=0,rank=2):
		self.suit = self.suit_names[suit]
		if rank in self.faces: # self.rank handles printed representation
			self.rank = self.faces[rank]
		else:
			self.rank = rank
		self.rank_num = rank # To handle winning comparison 

	def __str__(self):
		return "{} of {}".format(self.rank,self.suit)

class Deck(object):
	def __init__(self): # Don't need any input to create a deck of cards
		# This working depends on Card class existing above
		self.cards = []
		for suit in range(4):
			for rank in range(1,14):
				card = Card(suit,rank)
				self.cards.append(card) # appends in a sorted order

	def __str__(self):
		total = []
		for card in self.cards:
			total.append(card.__str__())
		# shows up in whatever order the cards are in
		return "\n".join(total) # returns a multi-line string listing each card

	def pop_card(self, i=-1):
		# removes and returns a card from the Deck
		# default is the last card in the Deck
		return self.cards.pop(i) # this card is no longer in the deck -- taken off

	def shuffle(self):
		random.shuffle(self.cards)

	def replace_card(self, card):
		card_strs = []
		for c in self.cards:
			card_strs.append(c.__str__())
		if card.__str__() not in card_strs:
			self.cards.append(card)

	def sort_cards(self):
		# Basically, remake the deck in a sorted way
		# This is assuming you cannot have more than the normal 52 cards in a deck
		self.cards = []
		for suit in range(4):
			for rank in range(1,14):
				card = Card(suit,rank)
				self.cards.append(card)


# Class Hand: Represents a hand of cards for a game, with basic functionality
# Functionality available: Number of cards attribute
# Methods: Can place a card out of the hand, add a card to the hand that is not a duplicate, find all suits available, find all ranks available, look for a specific card in the hand and return it if there
class Hand(object): 
	def __init__(self,deck_to_use,num_cards=5): # Constructor
		self.deck = deck_to_use # Needs a deck
		self.cards_in_hand = [] 
		for i in range(num_cards):
			self.cards_in_hand.append(self.deck.pop_card(-1))

	def place_card(self,i=0):
		return self.cards_in_hand.pop(i) # Basically the same as pop_card from the deck, but referencing the HAND's cards

	def get_suits_available(self): # Returns list of all the suits that are in the hand
		suits = []
		for c in self.cards_in_hand:
			if c.suit not in suits:
				suits.append(c.suit)
		return suits

	def get_ranks_available(self): # Returns list of all the ranks that are in the hand
		ranks = []
		for c in self.cards_in_hand:
			if c.rank not in ranks:
				ranks.append(c.rank)
		return ranks

	def specific_card(self,suit,rank):
		card_strs = []
		ind = 0
		for c in self.cards_in_hand:
			if c.suit == suit and c.rank == rank:
				return self.place_card(ind) # If find the card in the hand, get rid of that card from the hand and return it from this method
			ind = ind + 1
		return None # if there is none such card in the hand, return None value
		
	def add_card(self,card): # add card to hand (if there is no identical one, assuming working with 1 deck here)
		card_strs = []
		for c in self.cards_in_hand:
			card_strs.append(c.__str__())
		if card.__str__() not in card_strs:
			self.cards_in_hand.append(card)

	def __str__(self):
		total = []
		for card in self.cards_in_hand:
			total.append(card.__str__())
		# shows up in whatever order the cards are in
		return "\n".join(total) # returns a multi-line string listing each card

#### Functions for games ####

# Function that plays an altered version of the game of War when invoked.
def play_war_game(testing=False):
	player1 = Deck()
	player2 = Deck()

	p1_score = 0
	p2_score = 0

	player1.shuffle()
	player2.shuffle()
	if not testing:
		print("\n*** BEGIN THE GAME ***\n")
	for i in range(52):
		p1_card = player1.pop_card()
		p2_card = player2.pop_card()
		if not testing:
			print("Player 1 plays", p1_card,"& Player 2 plays", p2_card)

		if p1_card.rank_num > p2_card.rank_num:
			if not testing:
				print("Player 1 wins a point!")
			p1_score += 1
		elif p1_card.rank_num < p2_card.rank_num:
			if not testing:
				print("Player 2 wins a point!")
			p2_score += 1
		else:
			if not testing:
				print("Tie. Next turn.")

	if p1_score > p2_score:
		return "Player1", p1_score, p2_score
	elif p2_score > p1_score:
		return "Player2", p1_score, p2_score
	else:
		return "Tie", p1_score, p2_score

## Below this line, indented beneath it, goes function invocations, any code you want to run when you run this file.
if __name__ == "__main__":

	print("Test code here!\n")
	## The following is code to try out functionality of the class Hand. Uncomment the following lines to try it out. Note that each line depends on the former lines!

	deck_to_play = Deck() # Create a deck
	deck_to_play.shuffle() # Shuffle the deck!
	single_hand = Hand(deck_to_play,num_cards=5) # Deal one hand of 5 cards
	print(single_hand) # Print the hand to view it
	print("\n\n\n") # Print new lines, just for clarity


########### TESTS SHOULD GO BELOW THIS LINE ###########

# INCLUDE YOUR TESTS FROM HW2 HERE.
class ProblemSet2Tests(unittest.TestCase):

## Test that if you create a card with rank 12, its rank will be "Queen"
	def test_rank_12(self):
		value_of_card = Card(0,12)
		self.assertEqual(value_of_card.rank,"Queen")

## Test that if you create a card with rank 1, its rank will be "Ace"
	def test_rank_1(self):
		value_of_card = Card(0,1)
		self.assertEqual(value_of_card.rank,"Ace")

## Test that if you create a card instance with rank 3, its rank will be 3
	def test_rank_3(self):
		value_of_card = Card(0,3)
		self.assertEqual(value_of_card.rank, 3)

## Test that if you create a card instance with suit 1, it will be suit "Clubs"
	def test_suit_1(self):
		value_of_card = Card(1,3)
		self.assertEqual(value_of_card.suit,"Clubs")

## Test that if you create a card instance with suit 2, it will be suit "Hearts"
	def test_suit_2(self):
		value_of_card = Card(2,3)
		self.assertEqual(value_of_card.suit,"Hearts")

## Test that if you create a card instance, it will have access to a variable suit_names that contains the list ["Diamonds","Clubs","Hearts","Spades"]
	def test_list_of_suit_names(self):
		value_of_card = Card()
		self.assertEqual(value_of_card.suit_names, ["Diamonds","Clubs","Hearts","Spades"])

## Test that if you invoke the __str__ method of a card instance that is created with suit=2, rank=7, it returns the string "7 of Hearts"
	def test_string_method(self):
		value_of_card = Card(2,7)
		self.assertEqual(value_of_card.__str__(), "7 of Hearts")
## Test that if you create a deck instance, it will have 52 cards in its cards instance variable
	def test_deck_instance(self):
		value_of_card = Deck()
		self.assertEqual(len(value_of_card.cards), 52)

## Test that if you invoke the pop_card method on a deck, it will return a card instance.
	def test_pop_card(self):
		value_of_card = Deck()
		self.assertEqual(type(value_of_card.pop_card()), type(Card()))

## Test that the return value of the play_war_game function is a tuple with three elements, the first of which is a string. (This will probably require multiple test methods!)
	def test_play_war_game(self):
		value_of_card = play_war_game(testing = True)
		self.assertTrue(value_of_card[0], type(tuple))
		self.assertEqual(len(value_of_card), 3)

## Write at least 2 additional tests (not repeats of the above described tests). Make sure to include a descriptive message in these two so we can easily see what you are testing!
	def test_rank_levels(self):
		value_of_card = Card()
		self.assertEqual(len(value_of_card.rank_levels), 13, "testing if there are 13 rank levels")

	def test_rank_faces(self):
		test_if_king = Card(0,13)
		value_of_card = Card()	
		self.assertTrue(value_of_card.faces, type(dict)) # testing that faces are within a dictionary
		self.assertEqual(test_if_king.rank, "King", "testing if card with suit 12, it's rank will be King")

## Add tests, as described in instructions.
## Here is a sample.
class HandClassTests(unittest.TestCase):
	def test_add_card(self):
		d1 = Deck()
		h1 = Hand(d1) # default number of cards
		num = len(h1.cards_in_hand) # length of the cards list in the hand
		new_card = d1.pop_card() # pop another card off the deck
		h1.add_card(new_card) # invoke add_card method with the card that we popped off the deck
		self.assertEqual(len(h1.cards_in_hand),num+1) # Testing that the new number of cards in the hand is equal to the old number plus 1
	
		# Testing that cards_in_hand is a list
	def test_cards_in_hand(self):
		d2 = Deck()
		h2 = Hand(d2)
		self.assertEqual(type(h2.cards_in_hand), type([]))

	# Testing that the __init__ method in the Hand class with the default input returns a length of 5 cards in a hand
	def test_constructor_hand_with_5_cards(self):
		d3 = Deck()
		h3 = Hand(d3)
		self.assertEqual(len(h3.cards_in_hand), 5)

	# Testing that the __init__ method in the Hand class with a different input returns the same length of cards in a hand.
	def test_constructor_hand_with_2_cards(self):
		d4 = Deck()
		h4 = Hand(d4,2)
		self.assertEqual(len(h4.cards_in_hand), 2)

	# Testing that get_suits_available method returns a list
	def test_get_suits_available(self):
		d5 = Deck()
		h5 = Hand(d5)
		self.assertEqual(type(h5.get_suits_available()),type([]))

	# Testing that get_rank_available method returns a list
	def test_get_rank_available(self):
		d6 = Deck()
		h6 = Hand(d6)
		self.assertEqual(type(h6.get_ranks_available()), type([]))

	# Testing that place_card method is an instance of the Card Class
	def test_place_card(self):
		d7 = Deck()
		h7 = Hand(d7)
		self.assertEqual(type(h7.place_card()), type(Card()))

	# Testing that if a card is added to a hand successfully
	def test_add_card_part_2(self):
		d8 = Deck()
		h8 = Hand(d8)
		added_card = d8.pop_card()
		h8.add_card(added_card)
		self.assertIn(added_card, h8.cards_in_hand)

	# Testing that the specific_card method successfully works and printing it using the string method 
	def test_specific_card_string_output(self):
		d9 = Deck()
		h9 = Hand(d9,52)
		specific_card = h9.specific_card("Spades", 10)
		self.assertEqual(specific_card.__str__(), "10 of Spades")
	
	# Testing that the string method in the Hand class returns a string
	def test_string_method(self):
		d10 = Deck()
		h10 = Hand(d10)
		self.assertTrue(h10.__str__(), type(str))


unittest.main(verbosity=2) 